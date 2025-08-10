from time import sleep

from pinecone import Pinecone, ServerlessSpec


class PineconeClient:
    def __init__(self, api_key: str, index_name: str):
        self.index_name = index_name
        self.client = Pinecone(api_key=api_key)

    def get_index(self) -> Pinecone.Index:
        if not self.client.has_index(self.index_name):
            raise ValueError(f"Index {self.index_name} does not exist. Create and populate it first.")
        # add logging self.client.describe_index(self.index_name)
        return self.client.Index(self.index_name)

    def create_index(self, dimension: int = 1024, metric: str = "cosine", spec: ServerlessSpec | None = None) -> None:
        if self.client.has_index(self.index_name):
            raise ValueError(f"Index {self.index_name} already exists.")

        if spec is None:
            spec = ServerlessSpec(cloud="aws", region="us-east-1")

        self.client.create_index(
            name=self.index_name,
            dimension=dimension,
            metric=metric,
            spec=spec,
        )
        while not self.client.describe_index(self.index_name).status["ready"]:
            # TODO: add logging here
            sleep(1)
        # TODO: add index creation logging
        # print(f"Index {self.index_name} created successfully.")
