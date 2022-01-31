import pytest
from src.driver import func
from src.utils.sim import load_clsp_relative

load_clsp_relative("src/clsp/custom_puzzle.clsp")


def test_driver() -> None:
    func()
    assert True
