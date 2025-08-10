from dataclasses import dataclass
from typing import Any


class EmbeddingsConfig(dataclass):
    model_name: str
    model_kwargs: dict[str, Any] | None = None
    encode_kwargs: dict[str, Any] | None = None
