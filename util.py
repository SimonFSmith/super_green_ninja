import math


def distance(point_1=(0, 0), point_2=(0, 0)):
    return math.sqrt((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2)


def collides_with(first_object, second_object):
    collision_distance = first_object.width / 2 + second_object.width / 2
    actual_distance = distance(first_object.position, second_object.position)

    return (actual_distance <= collision_distance)
