class Human:
    # success = 0
    # failure = 0

    def __init__(self, id, height, weight, fatigue):
        self.id = id
        self.height = height
        self.weight = weight
        self.fatigue = fatigue
        self.bmi = None

    def set_bmi(self):
        self.bmi = round(self.weight / ((self.height / 100) ** 2), 1)
        print("{}의 BMI는 {}".format(self.id, self.bmi))

    # def add_success(self):
    #     if round(self.bmi, 1) == 23:
    #         self.success += 1
    #
    # def add_failure(self):
    #     if self.fatigue == 100:
    #         self.failure += 1


class Workout:
    def __init__(self, pt_count):
        self.human = None
        self.pt_count = pt_count

    def exercise(self, human):
        # set_bmi 부분을 Decorator로 구현할 수 있을 거 같다.
        human.set_bmi()
        if round(human.bmi) < 23:
            human.weight += 0.2
            human.fatigue += 10
            human.set_bmi()
            print(round(human.weight))
        elif round(human.bmi) > 23:
            human.weight -= 0.2
            human.fatigue += 10
            human.set_bmi()
            print(round(human.weight))
        else:
            print("운동 끝!!!!!!")


    def rest(self, human):
        human.set_bmi()
        human.fatigue -= 20
        print(round(human.weight))


# class Scheduler:
#     def __init__(self, human, weekdays=None):
#         self.human = human
#         if not weekdays:
#             print('요일을 지정해주세요')
#             pass
#         else:
#             self.weekdays = weekdays
#
#     def set_schedule(self, human):


if __name__ == '__main__':
    human = Human(1, 177, 75, fatigue=20)
    print(human.height)
    human.set_bmi()
    print(human.bmi)
    print(human.weight)
    workout = Workout(10)
    while workout.pt_count > 0:
        if human.fatigue < 90:
            workout.pt_count -= 1
            print("운동을 시작하지")
            workout.exercise(human)
        elif round(human.bmi) == 23:
            workout.exercise(human)
            print(workout.pt_count)
            break
        else:
            print("오늘은 좀 쉬어보자")
            workout.rest(human)
    human.set_bmi()
    print(human.bmi)
