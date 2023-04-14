import numpy as np
from sidrpy.classes import Point, Vector
import math


def point_location_from_vec(p0: Point, p1: Point, p2: Point):
    locationDet = np.linalg.det([[p2.x - p1.x, p2.y - p1.y], [p0.x - p1.x, p0.y - p1.y]])
    if locationDet == 0:
        return "on line"
    elif locationDet < 0:
        return "right"
    elif locationDet > 0:
        return "left"

def vector_product(p0: Point, p1: Point, p2: Point):
    return np.cross([p2.x - p1.x, p2.y - p1.y], [p0.x - p1.x, p0.y - p1.y])

def are_on_the_same_line(p1, p2, p3):
    if max(p1.x, p3.x >= p2.x >= min(p1.x, p3.x) and \
            max(p1.y, p3.y) >= p2.y >= min(p1.y, p3.y)):
        return True
    return False


def is_point_on_line(p1: Point, p2: Point, p3: Point) -> bool:
    d = np.linalg.det([[p3.x - p2.x, p3.y - p2.y], [p1.x - p2.x, p1.y - p2.y]])
    if d > 0:
        return False
    elif d < 0:
        return False
    else:
        return True


def are_two_lines_intersect(p1: Point, p2: Point, p3: Point, p4: Point) -> bool:
    d1 = np.linalg.det([[p4.x - p3.x, p4.y - p3.y], [p1.x - p3.x, p1.y - p3.y]])
    d2 = np.linalg.det([[p4.x - p3.x, p4.y - p3.y], [p2.x - p3.x, p2.y - p3.y]])
    d3 = np.linalg.det([[p2.x - p1.x, p2.y - p1.y], [p3.x - p1.x, p3.y - p1.y]])
    d4 = np.linalg.det([[p2.x - p1.x, p2.y - p1.y], [p4.x - p1.x, p4.y - p1.y]])

    if d1 * d2 <= 0 and d3 * d4 <= 0:
        return True
    else:
        return False


def calc_angle(v1: Vector, v2: Vector):
    arc = np.round(np.arccos((v1.x * v2.x + v1.y * v2.y) / (v1.norm() * v2.norm())) * 180 / np.pi)
    if point_location_from_vec(p2, z, p1) == "right":
        return 360 - arc
    else:
        return arc


def calc_octane(v: Vector) -> int:
    if 0 <= v.y < v.x:
        return 1
    elif 0 < v.x <= v.y:
        return 2
    elif 0 <= -v.x < v.y:
        return 3
    elif 0 < v.y <= -v.x:
        return 4
    elif 0 <= -v.y < -v.x:
        return 5
    elif 0 < -v.x <= -v.y:
        return 6
    elif 0 <= v.x < -v.y:
        return 7
    elif 0 < -v.y <= v.x:
        return 8

def calc_area(p0: Point, p1: Point, p2: Point):
    return np.linalg.det([[p2.x - p1.x, p2.y - p1.y], [p0.x - p1.x, p0.y - p1.y]])