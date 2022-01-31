import pytest
from chia.consensus.default_constants import DEFAULT_CONSTANTS
from chia.types.blockchain_format.coin import Coin
from chia.types.blockchain_format.program import Program, SerializedProgram
from chia.types.spend_bundle import SpendBundle
from chia.util.byte_types import hexstr_to_bytes
from chia.util.hash import std_hash
from clvm.casts import int_from_bytes, int_to_bytes

from src.driver import func
from src.utils.sim import load_clsp_relative

load_clsp_relative("src/clsp/custom_puzzle.clsp")


def test_driver() -> None:
    func()
    assert True
