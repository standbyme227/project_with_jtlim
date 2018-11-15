import random
import ast
# 사람들과 운동이 있으면, 자동으로 갱신되도록 해주는 클래스
# 사람과 운동을 매칭시키고
# 성공과 실패로 나눠서 txt에 저장시킨다.

from human import Human
from workout import Workout

MIN_HEIGHT = 150
MAX_HEIGHT = 200

MIN_WEIGHT = 40
MAX_WEIGHT = 120

CURRENT_PATH = '/Users/shsf/Study/Project_with_jtlim/fifth'
FILE_PATH = CURRENT_PATH + '/data/human_data_list.txt'


class Simulator:
    """시뮬레이션을 위한 클래스

        Attributes:
            # workout (Workout())
            # human_list (Human()의 List)

    """

    def __init__(self, number_of_people=0):
        """
        한명뿐만이 아니라 다수에 사람에대해서 시뮬레이션을 해야하는 클래스이기에
        인원수아니면 리스트형식으로 다중데이터를 소화하기위해서 구현하였다.

        :param (int) number_of_people: 인원수
        :param human_data_list: dict형식으로 이뤄진 List
        """
        self.human_list = self.init_human_list(number_of_people)
        self.success = []
        self.failure = []

    def check_file(self, FILE_PATH):
        try:
            read_file = open(FILE_PATH, 'r')
        except FileNotFoundError:
            return None

        lines = read_file.readlines()
        read_file.close()
        return lines

    def write_file(self, human):
        human_data = self.get_human_str(human)
        write_f = open(FILE_PATH, 'a')
        write_f.write(str(human_data) + '\n')
        write_f.close()

    def check_id(self, human):
        try:
            read_f = open(FILE_PATH, 'r')
        except FileNotFoundError:
            read_f = None

        if read_f:
            while True:
                line = read_f.read()
                if not line: break
                if "'id': " + str(human.id) + ',' in line:
                    pass
                else:
                    self.write_file(human)
            read_f.close()
        else:
            self.write_file(human)

    def get_human_str(self, human):
        data = {
            'id': human.id,
            'height': human.height,
            'weight': human.weight
        }
        return data

    def get_human_list(self, human_data_list):
        human_list = []
        print(human_data_list)
        for human_data in human_data_list:
            human_data = ast.literal_eval(human_data)
            human = Human(
                id=human_data['id'],
                height=human_data['height'],
                weight=human_data['weight'],
            )
            human_list.append(human)
        return human_list

    # 일단 txt파일에 저장되어있는지 확인
    # 있다면 그 파일의 내용을 불러와서 사용
    # 없다면 새로운 human_list를 만들고, txt파일에 저장.

    def init_human_list(self, number_of_people):

        lines = self.check_file(FILE_PATH)

        if lines and len(lines) == number_of_people:
            return self.get_human_list(lines)

        # [{id:id, height:height, weight:weight, fatigue:fatigue}, ]
        else:
            human_id_list = [human_id for human_id in range(1, number_of_people + 1)]
            height_list = [height for height in range(MIN_HEIGHT, MAX_HEIGHT)]
            weight_list = [weight for weight in range(MIN_WEIGHT, MAX_WEIGHT)]

        human_list = []
        for human_id in human_id_list:
            # random을 사용하면서 문제가 있었다. random suffle은 일종의 return값이 존재하지않는다.
            # 단순히 list를 섞을 뿐인데
            # x = random(x) 이렇게 사용했을시에 위에 말햇듯 반환값이 없어서 None이 선언된다.
            random.shuffle(height_list)
            random.shuffle(weight_list)

            # TODO 181106 원래는 Human class의 객체를 여기서 집어넣었으나
            # 이 부분은 말그대로 Human에 대한 정보 list를 만들기위한 로직이기에
            # dict형식으로 변경했다.

            # TODO 181106 Human class로 적용하기로 다시 변환
            human = Human(human_id, height_list[0], weight_list[0])
            human_list.append(human)

            # self.write_file(human)
            self.check_id(human)
            # self.read_file()

        return human_list

    def simulate(self):
        human_list = self.human_list
        for human_data in human_list:
            workout = Workout(20, human_data)

            while workout.pt_count > 0:
                if round(human_data.bmi) == 23:
                    workout.exercise()
                    print("{}번 님, {}일만에 Diet를 성공하셨네요!!! 남은 pt는 {}회 입니다.".format(
                        workout.human.id, workout.days, workout.pt_count))
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
                    print("{}번 님, {}일 동안 열심히 했지만 아직 목표치에 도달하지 못했네요 ㅠㅠ "
                          "조금 더 노력하면 목표치에 도착할 수 있을거에요!!".format(workout.human.id, workout.days))
                    self.failure.append(workout.human)


if __name__ == '__main__':
    simulator = Simulator(100)
    simulator.simulate()
    print(
        "{}명 성공, {}명 실패".format(len(simulator.success), len(simulator.failure))
    )
