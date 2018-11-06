from abc import *
from random import *


class Human:
    def __init__(self, id, weight, height, age, fat, muscle,
                 target_fat, target_muscle, target_weight,
                 ):
        self.id = id
        self.age = age
        self.height = height

        # 개인의 수치
        self.weight = weight
        self.fat = fat
        self.muscle = muscle

        # 개인의 목표치
        self.target_fat = target_fat
        self.target_muscle = target_muscle
        self.target_weight = target_weight

        # 개인의 운동량 한계치
        self.limit = None

        # 개인의 운동량
        self.total_workout = None

    # 근육량과 지방량의 변화를 위한 메소드
    def get_muscle(self, mount):
        self.muscle += mount
        self.weight += mount

    def lose_muscle(self, mount):
        self.muscle -= mount
        self.weight -= mount

    def get_fat(self, mount):
        self.fat += mount
        self.weight += mount

    def lose_fat(self, mount):
        self.fat -= mount
        self.weight -= mount

    # 그 사람의 한계치와 총운동량을 비교해서, 쉬어야되는 타임 / 포기하는 시점을 나타내기 위함.

    # 한 사람의 한계치를 세팅하는 메소드
    def set_limit(self):
        limit_list = [x for x in range(10, 100)]
        limit_list = random.shuffle(limit_list)
        self.limit = limit_list.pop()

    # TODO:여기에 있는게 맞는걸까??? 일단은 workout으로 이동 (181102)
    # # 총 운동량을 더하는 메소드
    # def get_total_workout(self, workout_mount):
    #     self.total_workout += workout_mount
    #
    # # 총 운동량을 줄이는 메소드
    # def lose_total_workout(self):
    #     self.total_workout -= 10

    def check_BMI(self, height, weight):
        self.BMI = weight // (height ** 2)



