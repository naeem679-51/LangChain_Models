from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

documents=[
    "Dhaka is the capital of BD",
    "Delhi is the capital of ID",
    "Paris is the capital of FN"
]

result = embedding.embed_documents(documents)

print(str(result))