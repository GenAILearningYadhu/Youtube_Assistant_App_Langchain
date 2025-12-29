from dotenv import load_dotenv
import os

# load_dotenv()


prompt_template="""
        You are a helpful assistant that answers questions
        using ONLY the provided YouTube transcript.

        Question:
        {question}

        Transcript:
        {context}

        Rules:
        - Use only the transcript content
        - If the answer is not found, say "I don't know"
        - Be clear and concise
        """




# https://www.youtube.com/watch?v=7ARBJQn6QkM
# What is Jensen Huang’s overall vision for the future of computing?

# How does Jensen Huang see AI transforming industries in the next decade?

# What role does NVIDIA aim to play in the future of artificial intelligence?

# How does Jensen Huang define the next computing revolution?