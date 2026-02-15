from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.openai import OpenAI
import os

_index = None
_query_engine = None

def load_index():
    global _index, _query_engine

    if _index is None:
        documents = SimpleDirectoryReader("data").load_data()
        llm = OpenAI(model="gpt-4o-mini")
        _index = VectorStoreIndex.from_documents(documents)
        _query_engine = _index.as_query_engine(llm=llm)

def query_documents(query: str) -> str:
    try:
        load_index()
        return str(_query_engine.query(query))
    except Exception as e:
        return f"Document system unavailable: {str(e)}"