import os

from dotenv import load_dotenv
from openai import OpenAI

from gitsource import GithubRepositoryDataReader
from minsearch import Index
from rag_helper import RAGBase

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

COMMIT = "8c1834d"

reader = GithubRepositoryDataReader(
    repo_owner="DataTalksClub",
    repo_name="llm-zoomcamp",
    commit_id=COMMIT,
    allowed_extensions={"md"},
    filename_filter=lambda path: "/lessons/" in path,
)

documents = [file.parse() for file in reader.read()]

index = Index(
    text_fields=["content"],
    keyword_fields=["filename"],
)
index.fit(documents)

rag = RAGBase(
    index=index,
    llm_client=client,
    model="models/gemini-2.5-flash",
)

if __name__ == "__main__":
    query = "How does the agentic loop keep calling the model until it stops?"
    answer = rag.rag(query)
    print(answer)