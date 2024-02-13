from __future__ import annotations

import os
from typing import TYPE_CHECKING

import streamlit as st
from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain_community.callbacks import StreamlitCallbackHandler
from langchain_community.vectorstores import Pinecone
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

if TYPE_CHECKING:
    from langchain.chains.retrieval_qa.base import BaseRetrievalQA


def initialize_vectorstore() -> Pinecone:
    index_name = os.environ["PINECONE_INDEX"]
    embeddings = OpenAIEmbeddings()
    return Pinecone.from_existing_index(index_name, embeddings)


def create_qa_chain() -> BaseRetrievalQA:
    vectorstore = initialize_vectorstore()
    callback = StreamlitCallbackHandler(st.container())

    llm = ChatOpenAI(  # type: ignore[call-arg]
        model_name=os.environ["OPENAI_API_MODEL"],
        temperature=float(os.environ["OPENAI_API_TEMPERATURE"]),
        streaming=True,
        callbacks=[callback],
    )

    return RetrievalQA.from_llm(llm=llm, retriever=vectorstore.as_retriever())


def main() -> None:
    load_dotenv()
    st.title("DLSite recommendation LLM")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("今日のおかずはなんですか?")

    if not prompt:
        return

    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        qa_chain = create_qa_chain()
        response = qa_chain.invoke(prompt)  # type: ignore[arg-type]

    st.session_state.messages.append({"role": "assistant", "content": response["result"]})


if __name__ == "__main__":
    main()
