from chia.wallet.puzzles import p2_delegated_puzzle_or_hidden_puzzle
from chia.wallet.puzzles.load_clvm import load_clvm
from chia.types.blockchain_format.program import Program

from src.utils.sim import load_clsp_relative

PUZ = load_clsp_relative("src/clsp/custom_puzzle.clsp", ["src/include/"])


def func() -> None:
    sol = Program.to([])
    PUZ.run(sol)
