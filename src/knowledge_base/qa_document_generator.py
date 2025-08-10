from langchain_pinecone import PineconeVectorStore


class QADocumentGenerator:
    def __init__(self, vectorstore: PineconeVectorStore):
        self.vectorstore = vectorstore
