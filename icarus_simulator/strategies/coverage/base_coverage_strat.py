#  2020 Tommaso Ciussani and Giacomo Giuliari
"""
Base strategy class for a specific task.
This class is open for custom extension, in order to create different execution strategies for this task.
See BaseStrategy for more details.
"""
from abc import abstractmethod

from icarus_simulator.strategies.base_strat import BaseStrat
from icarus_simulator.structure_definitions import GridPos, SatPos, Coverage


class BaseCoverageStrat(BaseStrat):
    @abstractmethod
    def compute(self, grid_pos: GridPos, sat_pos: SatPos) -> Coverage:
        raise NotImplementedError
