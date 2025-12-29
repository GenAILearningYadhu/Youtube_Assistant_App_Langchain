from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import YoutubeLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import prompt_template


embeddings= OllamaEmbeddings(model="nomic-embed-text:latest")

def create_vector_db_from_youtube_url(url:str) -> FAISS:
    # Fetches transcript text from the given YouTube video URL
    loader= YoutubeLoader.from_youtube_url(
        youtube_url=url,
        add_video_info=False
    )
    transcript= loader.load()

    # Breaks large text into smaller overlapping chunks
    text_splitter= RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )
    docs= text_splitter.split_documents(transcript)

    # Create Vector Database (FAISS)
    # Stores embeddings in a vector index for fast similarity search
    db= FAISS.from_documents(docs, embeddings)
    return db


def get_respponse_from_querry(db, query, k=4):
    # Retrieve Only Relevant Chunks from Vector DB
    docs= db.similarity_search(query, k=k)

    # Joins all retrieved transcript chunks into a single context
    context = "\n\n".join([doc.page_content for doc in docs])

    llm= OllamaLLM(
        model="llama3:latest",
        temperature=.4
    )

    prompt= PromptTemplate(
        input_variables=["question", "context"],
        template=prompt_template
    )

    chain = prompt | llm | StrOutputParser()

    response = chain.invoke({
        "question": query,
        "context": context
    })

    return response, docs

