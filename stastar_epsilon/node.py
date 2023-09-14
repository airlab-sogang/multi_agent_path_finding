from dataclasses import dataclass
from typing import List
from common.point import Point


@dataclass
class Node:
    point: Point
    time: int
    g_score: int = 0
    h_score: int = 0
    f_score: int = 0
    d_score: int = 0
    parent: "Node" = None

    def __lt__(self, other):
        if self.d_score == other.d_score:
            return self.f_score < other.f_score
        return self.d_score < other.d_score

    def __hash__(self):
        return hash((self.point, self.time))

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.point == other.point and self.time == other.time
        return False
