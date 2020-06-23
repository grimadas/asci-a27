from typing import Optional

from python_project.backbone.block import PlexusBlock
from python_project.backbone.datastore.block_store import BaseBlockStore
from python_project.backbone.datastore.chain_store import (
    BaseChain,
    FrontierDiff,
    Frontier,
    BaseChainFactory,
)
from python_project.backbone.datastore.database import BaseDB
from python_project.backbone.datastore.utils import Dot, Links


class MockBlockStore(BaseBlockStore):
    def add_block(self, block_hash: bytes, block_blob: bytes) -> None:
        pass

    def get_block_by_hash(self, block_hash: bytes) -> Optional[bytes]:
        pass

    def add_tx(self, block_hash: bytes, tx_blob: bytes) -> None:
        pass

    def add_dot(self, dot: bytes, block_hash: bytes) -> None:
        pass

    def get_hash_by_dot(self, dot: bytes) -> Optional[bytes]:
        pass

    def get_tx_by_hash(self, block_hash: bytes) -> Optional[bytes]:
        pass


class MockDBManager(BaseDB):
    def get_chain(self, chain_id) -> Optional[BaseChain]:
        pass

    def add_block(self, block: PlexusBlock, block_serializer) -> None:
        pass

    def get_block_blob_by_dot(self, chain_id: bytes, block_dot: Dot) -> Optional[bytes]:
        pass

    def get_tx_blob_by_dot(self, chain_id: bytes, block_dot: Dot) -> Optional[bytes]:
        pass


class MockChain(BaseChain):
    def add_block(self, block: PlexusBlock) -> Dot:
        pass

    def reconcile(self, frontier: Frontier) -> FrontierDiff:
        pass

    @property
    def frontier(self) -> Frontier:
        pass

    @property
    def consistent_terminal(self) -> Links:
        pass

    def get_next_links(self, block_dot: Dot) -> Optional[Links]:
        pass

    def get_prev_links(self, block_dot: Dot) -> Optional[Links]:
        pass


class MockChainFactory(BaseChainFactory):
    def create_personal_chain(self, **kwargs) -> BaseChain:
        return MockChain()

    def create_community_chain(self, **kwargs) -> BaseChain:
        return MockChain()