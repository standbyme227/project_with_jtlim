class Human:
    """
        운동할 사람(?)에 대한 클래스.

        Attributes :
            # id (int): 구분자 역할.
            # height (int) : 키
            # weight (int) : 몸무게
            # fatigue (int) : 운동을 할때 피로도로 그 횟수를 제한할 수 있게 구현.
            # bmi : 비만도

    """

    def __init__(self, id, height, weight, fatigue):
        self.id = id
        self.height = height
        self.weight = weight
        self.fatigue = fatigue
        self.bmi = None

    def set_bmi(self):
        self.bmi = round(self.weight / ((self.height / 100) ** 2), 1)
        print("{}의 BMI는 {}".format(self.id, self.bmi))


class Workout:
    """
        운동에 대한 클래스
    """
    days = 0

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
            print(round(human.weight, 1))
        elif round(human.bmi) > 23:
            human.weight -= 0.2
            human.fatigue += 10
            human.set_bmi()
            print(round(human.weight, 1))
        else:
            print("운동 끝!!!!!!")

    def rest(self, human):
        human.set_bmi()
        human.fatigue -= 20
        print(round(human.weight))


if __name__ == '__main__':
    human = Human(1, 177, 75.0, fatigue=20)
    human.set_bmi()

    workout = Workout(10)

    while workout.pt_count > 0:
        if round(human.bmi) == 23:
            workout.exercise(human)
            print("{}일만에 Diet를 성공하셨네요!!! 남은 pt는 {}회 입니다.".format(workout.days, workout.pt_count))
            break

        if human.fatigue < 90:
            workout.days += 1
            workout.pt_count -= 1
            print("운동을 시작하지")
            workout.exercise(human)
        else:
            workout.days += 1
            print("오늘은 좀 쉬어보자")
            workout.rest(human)
        # while문이 끝난 경우
        if workout.pt_count == 0:
            print("{}일 동안 열심히 했지만 아직 목표치에 도달하지 못했네요 ㅠㅠ "
                  "조금 더 노력하면 목표치에 도착할 수 있을거에요!!".format(workout.days))
