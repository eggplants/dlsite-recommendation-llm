from __future__ import annotations

import os
import sys

from dotenv import load_dotenv
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.vectorstores import Pinecone
from langchain_openai import OpenAIEmbeddings


def initialize_vectorstore() -> Pinecone:
    index_name = os.environ["PINECONE_INDEX"]
    embeddings = OpenAIEmbeddings()
    return Pinecone.from_existing_index(index_name, embeddings)


def main() -> None:
    load_dotenv()

    loader = CSVLoader(sys.argv[1])
    raw_docs = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=30)
    docs = text_splitter.split_documents(raw_docs)

    vectorstore = initialize_vectorstore()
    vectorstore.add_documents(docs)


if __name__ == "__main__":
    main()
