from human import Human


class Workout:
    """
        운동에 대한 클래스

        Attributes :
            # human (Human()) : Human 클래스의 인스턴스여야한다.
            # pt_count = 운동할 횟수를 지정 할 수 있다.
    """
    days = 0

    def __init__(self, pt_count, human):
        self.human = human
        self.pt_count = pt_count

    # TODO 181108 표준체중 산출하는 함수 추가. _done
    # 추가했었는데 human에 있는게 맞는가 같아서 이동
    # def calculate_standard_weight(self, human):
    #     return (human.height - 100) * 0.95

    # TODO 181108 fatigue 로직 정교하게 설계. _done
    # 이 부분도 human에 있는게 맞는 거 같아서 이동
    # def calculate_fatigue(self):
    #     human = self.human
    #     weight = human.weight
    #     if weight > 120:
    #         fatigue = round(weight * 0.25)
    #     elif weight > 100:
    #         fatigue = round(weight * 0.22)
    #     elif weight > 80:
    #         fatigue = round(weight * 0.20)
    #     elif weight > human.calculate_standard_weight() - 10:
    #         fatigue = round(weight * 0.15)
    #     else:
    #         fatigue = round(weight * 0.22)
    #     return fatigue


    # TODO 181109 유산소와 근력운동으로 분할해서 운동을 시행하도록 수정
    def exercise(self):
        human = self.human

        human.set_bmi()
        if round(human.bmi) < 23:
            human.weight += 0.2
            human.fatigue += human.calculate_fatigue()
            human.set_bmi()
            # print(human.weight)

        elif round(human.bmi) > 23:
            human.weight -= 0.2
            human.fatigue += human.calculate_fatigue()
            human.set_bmi()
            # print(human.weight)
        else:
            print("운동 끝!!!!!!")

    def rest(self):
        human = self.human
        human.set_bmi()
        human.fatigue -= 20
        # print(round(human.weight))


if __name__ == '__main__':
    human = Human(
        id=1,
        height=177,
        muscle=50,
        fat=30,
        fatigue=20,
        endurance=2,
    )
    workout = Workout(10, human)

    while workout.pt_count > 0:
        human = workout.human
        if round(human.bmi) == 23:
            workout.exercise()
            print("{}일만에 Diet를 성공하셨네요!!! 남은 pt는 {}회 입니다.".format(workout.days, workout.pt_count))
            break

        if human.fatigue < 90:
            workout.days += 1
            workout.pt_count -= 1
            print("운동을 시작하지")
            workout.exercise()
        else:
            workout.days += 1
            print("오늘은 좀 쉬어보자")
            workout.rest()
        # while문이 끝난 경우
        if workout.pt_count == 0:
            print("{}일 동안 열심히 했지만 아직 목표치에 도달하지 못했네요 ㅠㅠ "
                  "조금 더 노력하면 목표치에 도착할 수 있을거에요!!".format(workout.days))
