"""
Python re-implementation of the original C# “ProfMarblesTaskList”.
"""

from __future__ import annotations
from enum import Enum, auto
from typing import List, Sequence


class MarblePosition(Enum):
    """Enumeration matching the C# enum `MarblePosition`."""
    RED = auto()
    YELLOW = auto()
    GREEN = auto()
    EMPTY = auto()


# Short aliases so the task definitions stay readable
m = MarblePosition
r, y, g, e = m.RED, m.YELLOW, m.GREEN, m.EMPTY


class TestTube(list):
    """
    A `TestTube` is simply a list of `MarblePosition`s, but having a
    dedicated class makes future extensions (e.g. helper methods)
    straightforward and keeps type hints clear.
    """
    pass


class MarbleTask:
    def __init__(
        self,
        start_conditions: List[TestTube],
        goal: List[TestTube],
        moves: int,
        name: int,
    ) -> None:
        self.StartConditions = start_conditions
        self.Goal = goal
        self.Moves = moves
        self.Name = name


class ProfMarblesTaskList:
    """Direct Python translation of the original `ProfMarblesTaskList`."""

    def __init__(self) -> None:
        self.GameTasks: List[MarbleTask] = []

        # ------------------------------------------------------------------
        # Helper lambdas so the level definitions read almost like in C#.
        # ------------------------------------------------------------------
        Tubes = self.Tubes         # alias for brevity
        Tube = self.Tube

        self.GameTasks.append(MarbleTask(
            Tubes(Tube(r, r, r, y), Tube(3), Tube(2)),
            Tubes(Tube(y, e, e)),
            2, 1))

        self.GameTasks.append(MarbleTask(
            Tubes(Tube(r, y, r, y, r), Tube(e, e, e, e), Tube(e, e)),
            Tubes(Tube(y, r)),
            2, 2))

        self.GameTasks.append(MarbleTask(
            Tubes(Tube(y, r, e, e), Tube(r, r, e), Tube(2)),
            Tubes(Tube(y, e)),
            2, 3))

        self.GameTasks.append(MarbleTask(
            Tubes(Tube(e, e, e, e), Tube(r, r, y), Tube(2)),
            Tubes(Tube(r, r)),
            2, 4))

        self.GameTasks.append(MarbleTask(
            Tubes(Tube(r, r, r, y), Tube(3), Tube(2)),
            Tubes(Tube(y, e)),
            3, 5))

        self.GameTasks.append(MarbleTask(
            Tubes(Tube(r, y, y, r, r, y, e), Tube(4), Tube(2)),
            Tubes(Tube(r, y, e, e, e, e, e), Tube(r, y, e, e), Tube(r, y)),
            3, 6))

        self.GameTasks.append(MarbleTask(
            Tubes(Tube(r, y, r, y, r), Tube(4), Tube(3)),
            Tubes(Tube(r, r, e, e, e)),
            3, 7))

        self.GameTasks.append(MarbleTask(
            Tubes(Tube(4, r), Tube(3, r), Tube(y, r)),
            Tubes(Tube(4, r), Tube(3, r), Tube(r, y)),
            3, 8))

        self.GameTasks.append(MarbleTask(
            Tubes(Tube(4, g), Tube(3, y), Tube(2, r)),
            Tubes(Tube(g, y, r)), 
            3, 9))

        self.GameTasks.append(MarbleTask(
            Tubes(Tube(5, r, y), Tube(4, r, r), Tube(r, r)),
            Tubes(Tube(5, r, r), Tube(4, r, r), Tube(r, y)),
            3, 10))

        self.GameTasks.append(MarbleTask(
            Tubes(Tube(r, y, y, e), Tube(g, g, r), Tube(2)),
            Tubes(Tube(4, r, r), Tube(3, y, y), Tube(g, g)),
            4, 11))
        self.GameTasks.append(MarbleTask(
            Tubes(Tube(r, r, r, y, y), Tube(3), Tube(2)),
            Tubes(Tube(y, r, y)),
            4, 12))
        self.GameTasks.append(MarbleTask(
            Tubes(Tube(r, y, r, y, r), Tube(4), Tube(2)),
            Tubes(Tube(r, r)),
            4, 13))
        self.GameTasks.append(MarbleTask(
            Tubes(Tube(5, r, r, r), Tube(y, r, r), Tube(2)),
            Tubes(Tube(5, r, r, y), Tube(r, r, r)),
            4, 14))
        self.GameTasks.append(MarbleTask(
            Tubes(Tube(4), Tube(r, r, e), Tube(r, y)),
            Tubes(Tube(4, r), Tube(3, r), Tube(r, y)),
            4, 15))
        self.GameTasks.append(MarbleTask(
            Tubes(Tube(r, y, y, r, r, y, e), Tube(5), Tube(2)),
            Tubes(Tube(7, y, r), Tube(5, y, r), Tube(y, r)),
            5, 16))
        self.GameTasks.append(MarbleTask(
            Tubes(Tube(5, r), Tube(r, y, r), Tube(r, e)),
            Tubes(Tube(5, r), Tube(r, r, y), Tube(r, e)),
            5, 17))
        self.GameTasks.append(MarbleTask(
            Tubes(Tube(4, r), Tube(3, y), Tube(g, g)),
            Tubes(Tube(4, g), Tube(3, g), Tube(y, r)),
            5, 18))
        self.GameTasks.append(MarbleTask(
            Tubes(Tube(7, y, r, g), Tube(5, y, r), Tube(y, r)),
            Tubes(Tube(7, y, r), Tube(5, y, r, g), Tube(y, r)),
            5, 19))
        self.GameTasks.append(MarbleTask(
            Tubes(Tube(r, y, r, r), Tube(3), Tube(2)),
            Tubes(Tube(4, y)),
            5, 20))
        
        self.GameTasks.append(MarbleTask(
            Tubes(Tube(y, r, r, r, r, g), Tube(3), Tube(4)),
            Tubes(Tube(6, y), Tube(r, r, r, r), Tube(3, g)),
            5, 21))
        self.GameTasks.append(MarbleTask(
            Tubes(Tube(r, g, y, r), Tube(3), Tube(2)),
            Tubes(Tube(4, g), Tube(3, y), Tube(r, r)),
            6, 22))
        self.GameTasks.append(MarbleTask(
            Tubes(Tube(r, r, y, r, r, r), Tube(3), Tube(2)),
            Tubes(Tube(3, y)),
            6, 23))
        self.GameTasks.append(MarbleTask(
            Tubes(Tube(y, r, r, r, y, y), Tube(4), Tube(3)),
            Tubes(Tube(r, r, r)),
            6, 24))
        self.GameTasks.append(MarbleTask(
            Tubes(Tube(5, y, r), Tube(r, r, r), Tube(2)),
            Tubes(Tube(r, r, r, r, e)),
            6, 25))
        self.GameTasks.append(MarbleTask(
            Tubes(Tube(5), Tube(r, y, r), Tube(2)),
            Tubes(Tube(y, e)),
            6, 26))
        self.GameTasks.append(MarbleTask(
            Tubes(Tube(4, g), Tube(y, y, y), Tube(r, e)),
            Tubes(Tube(g, y, r)),
            6, 27))
        self.GameTasks.append(MarbleTask(
            Tubes(Tube(r, r, r, r, r, r, y), Tube(4), Tube(3)),
            Tubes(Tube(y, r, r, r, r, r, r)),
            7, 28))
        self.GameTasks.append(MarbleTask(
            Tubes(Tube(7, r, r, r, r, r), Tube(5), Tube(y, r, e)),
            Tubes(Tube(3, y)),
            7, 29))
        self.GameTasks.append(MarbleTask(
            Tubes(Tube(4), Tube(g, r, y), Tube(g, r)),
            Tubes(Tube(4, y), Tube(g, r, e), Tube(g, r)),
            7, 30))
        self.GameTasks.append(MarbleTask(
            Tubes(Tube(4, r), Tube(r, y, y), Tube(r, e)),
            Tubes(Tube(4, y), Tube(r, r, r), Tube(y, e)),
            7, 31))
        self.GameTasks.append(MarbleTask(
            Tubes(Tube(4, r, y), Tube(3, r), Tube(r, r)),
            Tubes(Tube(4, y)),
            7, 32))
        self.GameTasks.append(MarbleTask(
            Tubes(Tube(5, y, r), Tube(r, r, r), Tube(2)),
            Tubes(Tube(y, e)),
            7, 33))
        self.GameTasks.append(MarbleTask(
            Tubes(Tube(r, y, r, r, r, r, r, r), Tube(5), Tube(4)),
            Tubes(Tube(5, y)),
            8, 34))
        self.GameTasks.append(MarbleTask(
            Tubes(Tube(r, r, r, r, y, y, y, y), Tube(6), Tube(3)),
            Tubes(Tube(r, r, y, y, r, r)),
            8, 35))
        self.GameTasks.append(MarbleTask(
            Tubes(Tube(6, y, y), Tube(4, g, g), Tube(r, r, r)),
            Tubes(Tube(6, g, g), Tube(4, y, y), Tube(r, r, r)),
            8, 36))
        self.GameTasks.append(MarbleTask(
            Tubes(Tube(r, r, r, y, y, g), Tube(4), Tube(3)),
            Tubes(Tube(6, g), Tube(4, y, y), Tube(r, r, r)),
            8, 37))
        self.GameTasks.append(MarbleTask(
            Tubes(Tube(y, y, r, r, r), Tube(3), Tube(2)),
            Tubes(Tube(r, y, r, y, r)),
            9, 38))
        self.GameTasks.append(MarbleTask(
            Tubes(Tube(g, r, r, r, r, r, y), Tube(4), Tube(3)),
            Tubes(Tube(y, r, r, r, r, r, g)),
            9, 39))
        self.GameTasks.append(MarbleTask(
            Tubes(Tube(r, y, r, g, y, r, y), Tube(5), Tube(2)),
            Tubes(Tube(7, r, y, g), Tube(5, r, y), Tube(r, y)),
            2, 40))
        self.GameTasks.append(MarbleTask(
            Tubes(Tube(5, g, r), Tube(g, r, y), Tube(2)),
            Tubes(Tube(5, r, r), Tube(3, y), Tube(g, g)),
            9, 41))
        self.GameTasks.append(MarbleTask(
            Tubes(Tube(4, g), Tube(y, y, y), Tube(r, e)),
            Tubes(Tube(4, r), Tube(y, y, y), Tube(g, e)),
            9, 42))
        self.GameTasks.append(MarbleTask(
            Tubes(Tube(r, r, r, r, y, y, y, y), Tube(5), Tube(3)),
            Tubes(Tube(y, y, r, r, y, y, r, r)),
            10, 43))
        self.GameTasks.append(MarbleTask(
            Tubes(Tube(r, y, g, r, y, g, r), Tube(5), Tube(3)),
            Tubes(Tube(r, r, r, y, y)),
            10, 44))
        self.GameTasks.append(MarbleTask(
            Tubes(Tube(g, r, r, r, r, y), Tube(4), Tube(3)),
            Tubes(Tube(6, y), Tube(r, r, r, r), Tube(3, g)),
            10, 45))
        self.GameTasks.append(MarbleTask(
            Tubes(Tube(6, r), Tube(y, y, y, y), Tube(3, g)),
            Tubes(Tube(6, g), Tube(y, y, y, y), Tube(3, r)),
            11, 46))
        self.GameTasks.append(MarbleTask(
            Tubes(Tube(8, r, r, r, r, r, g), Tube(7, y, y), Tube(3)),
            Tubes(Tube(8, r, r, r, r, g, r), Tube(7, y, y)),
            11, 47))
        self.GameTasks.append(MarbleTask(
            Tubes(Tube(r, g, r, y, r, g, r, y), Tube(6), Tube(3)),
            Tubes(Tube(y, r, r, r, r, y)),
            11, 48))
        self.GameTasks.append(MarbleTask(
            Tubes(Tube(r, y, r, r, g, r), Tube(4), Tube(3)),
            Tubes(Tube(6, y), Tube(r, r, r, r), Tube(3, g)),
            11, 49))
        self.GameTasks.append(MarbleTask(
            Tubes(Tube(7, y, r, r), Tube(6, r, g, r), Tube(r, r, y)),
            Tubes(Tube(7, g), Tube(y, r, r, r, r, r), Tube(y, r, e)),
            11, 50))
        self.GameTasks.append(MarbleTask(
            Tubes(Tube(8, r, r, y, y), Tube(6, y, r, y, r), Tube(3)),
            Tubes(Tube(8, r, r, y, y), Tube(6, r, r, y, y)),
            12, 51))
        self.GameTasks.append(MarbleTask(
            Tubes(Tube(y, y, r, r, g, g, g, g), Tube(5), Tube(3)),
            Tubes(Tube(g, y, r)),
            12, 52))
        self.GameTasks.append(MarbleTask(
            Tubes(Tube(8, r, y, g), Tube(7, r, y, g), Tube(r, y, g)),
            Tubes(Tube(8, g, g, g), Tube(7, y, y, y), Tube(r, r, r)),
            13, 53))
        self.GameTasks.append(MarbleTask(
            Tubes(Tube(8, r, r, r, r, r), Tube(7, g, y, y), Tube(3)),
            Tubes(Tube(8, r, g, r, r, r, r), Tube(7, y, y)),
            13, 54))
        self.GameTasks.append(MarbleTask(
            Tubes(Tube(r, r, r, r, y, y, y, y), Tube(5), Tube(4)),
            Tubes(Tube(r, y, r, y, r, y, r, y)),
            14, 55))
        self.GameTasks.append(MarbleTask(
            Tubes(Tube(7, g), Tube(r, y, r, y, r), Tube(g, y, g)),
            Tubes(Tube(7, g, g, g), Tube(5, y, y, y), Tube(r, r, r)),
            14, 56))
        self.GameTasks.append(MarbleTask(
            Tubes(Tube(8, g, g, g), Tube(7, y, y, y), Tube(r, r, r)),
            Tubes(Tube(8, g, y, r), Tube(7, g, y, r), Tube(g, y, r)),
            16, 57))
        self.GameTasks.append(MarbleTask(
            Tubes(Tube(r, y, r, r, r, r, y, g), Tube(5), Tube(4)),
            Tubes(Tube(8, g), Tube(r, r, r, r, r), Tube(4, y, y)),
            16, 58))
        self.GameTasks.append(MarbleTask(
            Tubes(Tube(r, r, g, g, y, r, y), Tube(4), Tube(3)),
            Tubes(Tube(7, g, g), Tube(4, y, y), Tube(r, r, r)),
            17, 59))
        self.GameTasks.append(MarbleTask(
            Tubes(Tube(8, g, y, g, y), Tube(6, r, r, r, r), Tube(3)),
            Tubes(Tube(8, g, g, y, y), Tube(6, r, r, r, r)),
            18, 60))


        # Validate the newly built list
        fails: List[int] = []
        if not self.validate_tasks(fails):
            fail_list = ", ".join(map(str, fails))
            raise Exception(f"Some of the tasks are configured faulty: {fail_list}")

    # ----------------------------------------------------------------------
    # Validation helpers – kept as literal translations of the C# originals
    # ----------------------------------------------------------------------
    def validate_tasks(self, fails: List[int]) -> bool:
        fails.clear()
        for task in self.GameTasks:
            if not self._validate(task.StartConditions, task.Goal):
                fails.append(task.Name)
        return not fails  # returns True when list is empty

    def _validate(self, start: List[TestTube], goal: List[TestTube]) -> bool:
        r_s, y_s, g_s, e_s = self._get_count(start)
        r_g, y_g, g_g, e_g = self._get_count(goal)

        if (r_s + y_s + g_s + e_s) == (r_g + y_g + g_g + e_g):
            return r_s == r_g and y_s == y_g and g_s == g_g and e_s == e_g
        # Goal describes only a subset → start must contain at least those
        return r_s >= r_g and y_s >= y_g and g_s >= g_g and e_s >= e_g

    @staticmethod
    def _get_count(tubes: List[TestTube]) -> tuple[int, int, int, int]:
        """Counts all four marble types inside a tube list."""
        r_cnt = y_cnt = g_cnt = e_cnt = 0
        for tube in tubes:
            for marble in tube:
                if marble == m.RED:
                    r_cnt += 1
                elif marble == m.GREEN:
                    g_cnt += 1
                elif marble == m.YELLOW:
                    y_cnt += 1
                elif marble == m.EMPTY:
                    e_cnt += 1
                else:
                    raise ValueError(f"Unexpected marble: {marble}")
        return r_cnt, y_cnt, g_cnt, e_cnt

    # ----------------------------------------------------------------------
    # Helper factory functions (API identical to the C# version)
    # ----------------------------------------------------------------------
    @staticmethod
    def Tubes(*tubes: TestTube) -> List[TestTube]:
        """Returns a list of `TestTube`s (syntactic sugar)."""
        return list(tubes)

    @staticmethod
    def Tube(*args: m | int) -> TestTube:
        """
        Flexible factory that mimics the three C# overloads:

        * Tube(r, r, y)                size is implicit
        * Tube(4)                      size only; filled with EMPTY
        * Tube(4, r, y)                fixed size, pre-filled with given marbles
        """
        if not args:  # no arguments at all → invalid usage
            raise ValueError("Tube() requires at least one argument")

        # single int means “size, but empty”
        if len(args) == 1 and isinstance(args[0], int):
            size = args[0]
            positions: Sequence[m] = ()
        # int + more args means “size, plus initial positions”
        elif isinstance(args[0], int):
            size = int(args[0])
            positions = args[1:]
        # no int at front → size is the number of marbles passed
        else:
            size = len(args)
            positions = args

        if len(positions) > size:
            raise ValueError("More marbles than fit into the test tube")

        tube = list(positions) + [m.EMPTY] * (size - len(positions))
        return TestTube(tube)


# --------------------------------------------------------------------------
# Quick self-check – run this file directly to verify all tasks validate
# --------------------------------------------------------------------------
if __name__ == "__main__":
    ProfMarblesTaskList()
    print("All tasks validated successfully.")
