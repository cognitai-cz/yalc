from abc import ABC, abstractmethod

from pydantic import BaseModel

from yalc.clients.schemas import ClientCall


class ClientMetadataStrategy[T: BaseModel](ABC):
    @abstractmethod
    def handle(self, call: ClientCall, context: T | None):
        pass
