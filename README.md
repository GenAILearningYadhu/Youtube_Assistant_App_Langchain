YouTube Assistant

YouTube Assistant is an interactive Streamlit app powered by a Large Language Model (LLM) that allows users to ask questions about any YouTube video. By leveraging transcript extraction, embeddings, and advanced LLM reasoning, this tool provides concise answers to your queries.

Features:
Ask Questions on Any YouTube Video: Enter a YouTube URL and ask specific questions about the video content.
Transcript Analysis: Automatically loads the video transcript for understanding the content.
AI-Powered Responses: Provides detailed answers using an LLM with embeddings for context.
Easy-to-Use Interface: Streamlit-based frontend for simple interaction.

Install dependencies:
pip install -r requirements.txt
Libraries Used
LangChain: OllamaLLM, PromptTemplate, StrOutputParser for LLM queries and prompts.
LangChain Community: YoutubeLoader, FAISS, OllamaEmbeddings for video loading and vector search.
Text Splitters: RecursiveCharacterTextSplitter for handling large transcripts.
Streamlit: For building the interactive web interface.
Custom Modules: langchain_helper and config for prompt templates and helper functions.

Usage:
Run the Streamlit app: streamlit run app.py
In the sidebar, enter: 
YouTube Video URL
Your Query
Click Submit and view the AI-generated answer in the main panel.

Example Input:
YouTube URL: https://www.youtube.com/watch?v=7ARBJQn6QkM
Query: What is Jensen Huang’s overall vision for the future of computing?

Output: Attached snap

