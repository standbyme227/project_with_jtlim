import random

# 사람들과 운동이 있으면, 자동으로 갱신되도록 해주는 클래스
# 사람과 운동을 매칭시키고
# 성공과 실패로 나눠서 txt에 저장시킨다.

# TODO 181106 : Simulator를 구현하는 중이다.
from human import Human
from workout import Workout


class Simulator:
    """
        시뮬레이션을 위한 클래스

        Attributes:
            # workout (Workout())
            # human_list (Human()의 List)
    """

    def __init__(self, number_of_people=0, human_list=[]):
        """
        한명뿐만이 아니라 다수에 사람에대해서 시뮬레이션을 해야하는 클래스이기에
        인원수아니면 리스트형식으로 다중데이터를 소화하기위해서 구현하였다.

        :param workout:
        :param number_of_people:
        :param human_list:
        """
        self.human_list = self.init_human_list(number_of_people, human_list)
        self.success = []
        self.failure = []

    def init_human_list(self, number_of_people, human_list):
        # [{id:id, height:height, weight:weight, fatigue:fatigue}, ]
        human_id_list = []
        height_list = []
        weight_list = []
        fatigue_list = []
        if len(human_list) > 0:
            return human_list
        else:
            human_id_list = [human_id for human_id in range(1, number_of_people + 1)]
            height_list = [height for height in range(150, 200)]
            weight_list = [weight for weight in range(40, 120)]
            fatigue_list = [fatigue for fatigue in range(0, 60)]

        human_list = []
        for human_id in human_id_list:
            # random을 사용하면서 문제가 있었다. random suffle은 일종의 return값이 존재하지않는다.
            # 단순히 list를 섞을 뿐인데
            # x = random(x) 이렇게 사용했을시에 위에 말햇듯 반환값이 없어서 None이 선언된다.
            random.shuffle(height_list)
            random.shuffle(weight_list)
            random.shuffle(fatigue_list)

            # TODO 181106 원래는 Human class의 객체를 여기서 집어넣었으나
            # 이 부분은 말그대로 Human에 대한 정보 list를 만들기위한 로직이기에
            # dict형식으로 변경했다.

            human = Human(human_id, height_list[0], weight_list[0], fatigue_list[0])
            # TODO 181106 Human class로 적용
            human_list.append(human)
        return human_list

    def simulate(self):
        human_list = self.human_list
        for human_data in human_list:
            workout = Workout(20, human_data)

            while workout.pt_count > 0:
                if round(human_data.bmi) == 23:
                    workout.exercise()
                    print("{}일만에 Diet를 성공하셨네요!!! 남은 pt는 {}회 입니다.".format(workout.days, workout.pt_count))
                    self.success.append(workout.human)
                    break

                if human_data.fatigue < 90:
                    workout.days += 1
                    workout.pt_count -= 1
                    workout.exercise()
                else:
                    workout.days += 1
                    workout.rest()

                # while문이 끝난 경우
                if workout.pt_count == 0:
                    print("{}일 동안 열심히 했지만 아직 목표치에 도달하지 못했네요 ㅠㅠ "
                          "조금 더 노력하면 목표치에 도착할 수 있을거에요!!".format(workout.days))
                    self.failure.append(workout.human)


if __name__ == '__main__':
    simulator = Simulator(10000)
    simulator.simulate()
    print(
        "{}명 성공, {}명 실패".format(len(simulator.success), len(simulator.failure))
    )
