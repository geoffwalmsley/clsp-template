import pytest
from chia.consensus.default_constants import DEFAULT_CONSTANTS
from chia.types.blockchain_format.coin import Coin
from chia.types.blockchain_format.program import Program, SerializedProgram
from chia.types.spend_bundle import SpendBundle
from chia.util.byte_types import hexstr_to_bytes
from chia.util.hash import std_hash
from chia.wallet.puzzles.p2_delegated_puzzle_or_hidden_puzzle import (  # standard_transaction
    DEFAULT_HIDDEN_PUZZLE_HASH,
    calculate_synthetic_secret_key,
    puzzle_for_pk,
)
from clvm.casts import int_from_bytes, int_to_bytes

from src.driver import func
from src.utils.sim import load_clsp_relative, setup_node_only

CLSP = load_clsp_relative("src/clsp/custom_puzzle.clsp")


@pytest.fixture
async def node():
    node = await setup_node_only()
    yield node
    await node.close()


@pytest.fixture
async def alice(node):
    wallet = node.make_wallet("alice")
    await node.farm_block(farmer=wallet)
    return wallet


@pytest.fixture
async def bob(node):
    wallet = node.make_wallet("bob")
    await node.farm_block(farmer=wallet)
    return wallet


class TestPuzzle:
    @pytest.mark.asyncio
    async def test_clsp(self, alice):
        amount = 101
        found_coin = await alice.choose_coin(amount)
        assert found_coin.amount >= amount
