import math
import random
import matplotlib.pyplot as plt
from sidrpy.utils import point_location_from_vec
from MyPoint import Point
from MyVector import Vector2d

MIN = 0
MAX = 500


# инициализируем точки
def initPoints(n) -> list:
    X = [random.randint(MIN, MAX) for _ in range(n)]
    Y = [random.randint(MIN, MAX) for _ in range(n)]
    points = []
    for i in range(len(X)):
        el = Point(X[i], Y[i], i)
        for j in range(len(points)):
            if el.equals(points[j]):
                el.x = random.randint(MIN, MAX)
                el.y = random.randint(MIN, MAX)
        points.append(el)
    return points




def changePositions(points):
    i = 0
    for point in points:
        point.pos = i
        i += 1
    return points


def angleBetweenVectors(vect1, vect2):
    return math.acos(Vector2d.scalar_product(vect1, vect2) / (vect1.getLen() * vect2.getLen()))




def sortPointsByY(points):
    sorted_points = points.copy()
    for i in range(1, len(sorted_points)):
        point_to_insert = sorted_points[i]
        j = i - 1
        while j >= 0 and sorted_points[j].y > point_to_insert.y:
            sorted_points[j + 1] = sorted_points[j]
            j -= 1
        sorted_points[j + 1] = point_to_insert
    return sorted_points


def findNearestPoint(points, point1, point2):
    maxAngle = -1
    maxPos = -1
    for i, item in enumerate(points):
        fstVector = Vector2d(item.x - point1.x, item.y - point1.y)
        sndVector = Vector2d(item.x - point2.x, item.y - point2.y)
        if not ((item.x == point1.x and item.y == point1.y) or (item.x == point2.x and item.y == point2.y)):
            angle = angleBetweenVectors(fstVector, sndVector)
            if angle > maxAngle:
                maxAngle = angle
                maxPos = i
    return maxPos


def startTriangulation(points, tri):  # первый шаг триангуляции
    maxPos = findNearestPoint(points, points[0], points[1])  # находим ближайшую точку к самым нижним
    tmp = [points[0].pos, points[1].pos, points[maxPos].pos]
    tri.append(tmp)  # добавить  в массив треугольников
    if point_location_from_vec(points[0], points[1],points[maxPos]) == "right":
        # если правее
        triangulation(points, points[1], points[maxPos], tri)
        triangulation(points, points[maxPos], points[0], tri)
    else:
        # если левее
        triangulation(points, points[0], points[maxPos], tri)
        triangulation(points, points[maxPos], points[1], tri)
    return tri


def triangleExist(arr, tri):  # проверка на существование треугольника в массиве треугольников
    flag = False
    for item in tri:
        if item[0] == arr[0] and item[1] == arr[1] and item[2] == arr[2]:
            flag = True
    return flag


def triangulation(points, point1, point2, tri):
    higherPoints = []  # точки которые лежат выше(по факту левее) прямой(вектора) (point1, point2)

    for item in points:  # ищем те, что выше(левее) и добавляем их в массив
        # if point_location_from_vec(point1, point2, item) == "left":
        if point_location_from_vec(point1, point2,item) == "left":
            higherPoints.append(item)

    if len(higherPoints):  # если нашлись точки, то продолжаем рекурсию
        point = findNearestPoint(higherPoints, point1, point2)
        triangle = [point1.pos, point2.pos, higherPoints[point].pos]
        if not triangleExist(triangle, tri):  # если такого треугольника нет, то продолжаем
            tri.append(triangle)  # добавляем в массив треугольников
            triangulation(points, point1, higherPoints[point], tri)
            triangulation(points, higherPoints[point], point2, tri)




# рисуем точки
def draw(points):
    points_y = []
    points_x = []
    for p in points:
        points_x.append(p.x)
        points_y.append(p.y)
    plt.scatter(points_x, points_y)
    plt.show()


def draw_polygon(points):
    n = len(points)
    for i in range(0, n - 1):
        plt.plot([points[i].x, points[i + 1].x], [points[i].y, points[i + 1].y], color="black")
    plt.plot([points[n - 1].x, points[0].x], [points[n - 1].y, points[0].y], color="black")



n = 10
points = initPoints(n)
tri = []
points = sortPointsByY(points)
# addPositions
points = changePositions(points)
# startTriangulation
tri = startTriangulation(points, tri)

for item in tri:
    pol = map(lambda x: points[x], item)
    polList = list(pol)
    draw_polygon(polList)

draw(points)

