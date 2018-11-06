import random


class Human:
    """
        운동할 사람(?)에 대한 클래스.
        property를 사용해서 0이하의 값이나 실존가능한 최대값을 한정지었다.

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
        # TODO 181106 : 예시를 보고했으나, 이렇게 넣어도 되는건지 확실치가 않다.
        self.bmi = self.set_bmi()

    # TODO 181106 : 좀 더 객체의 내용을 알기 쉽도록 __str__을 구현했다.
    def __str__(self):
        return "id : {}, height : {}, weight : {}, fatigue : {}, bmi : {}".format(
            self.id, self.height, self.weight, self.fatigue, self.bmi)

    @property
    def height(self):
        return self._height

    @property
    def weight(self):
        return self._weight

    @property
    def fatigue(self):
        return self._fatigue

    @height.setter
    def height(self, height):
        if height < 0 or height > 250:
            raise ValueError("height below 0 or above 250 are not possible")
        self._height = height

    @weight.setter
    def weight(self, weight):
        if weight < 0 or weight > 600:
            raise ValueError("weight below 0 or above 600 are not possible")
        self._weight = weight

    # 피로도는 100에 가까울수록 좋지않다.
    @fatigue.setter
    def fatigue(self, fatigue):
        if fatigue < 0:
            return
        self._fatigue = 0

    # 비만도를 계산해서 넣어주는 로직이다.
    def set_bmi(self):
        print(1)
        self.bmi = round(self.weight / ((self.height / 100) ** 2), 1)
        print("{}의 BMI는 {}".format(self.id, self.bmi))
        return self.bmi


class Workout:
    """
        운동에 대한 클래스

        Attributes :
            # human (Human()) : Human 클래스의 인스턴스여야한다.
            # pt_count = 운동할 횟수를 지정 할 수 있다.
    """
    days = 0

    def __init__(self, pt_count):
        self.human = None
        self.pt_count = pt_count

    def calculate_fatigue(self, human):
        weight = human.weight
        if weight > 80:
            fatigue = round(weight * 0.2)
        else:
            fatigue = round(weight * 0.15)
        return fatigue

    def exercise(self, human):
        # set_bmi 부분을 Decorator로 구현할 수 있을 거 같다.
        bmi = human.bmi
        weight = human.weight
        fatigue = human.fatigue
        human.set_bmi()
        if round(bmi) < 23:
            weight += 0.2
            fatigue += self.calculate_fatigue(human)
            human.set_bmi()
            print(weight)
        elif round(bmi) > 23:
            weight -= 0.2
            fatigue += self.calculate_fatigue(human)
            human.set_bmi()
            print(weight)
        else:
            print("운동 끝!!!!!!")

    def rest(self, human):
        human.set_bmi()
        human.fatigue -= 20
        print(round(human.weight))


# 사람들과 운동이 있으면, 자동으로 갱신되도록 해주는 클래스
# 사람과 운동을 매칭시키고
# 성공과 실패로 나눠서 txt에 저장시킨다.

# TODO 181106 : Simulator를 구현하는 중이다.
class Simulator:
    # 운동이 들어가고
    # 사람의 숫자 또는 사람들에대한 리스트가 들어갈 수 있다고 판단했다.
    def __init__(self, workout, number_of_people=0, human_list=[]):
        self.workout = workout
        self.human_list = self.set_people(number_of_people, human_list)


    def set_people(self, number_of_people, human_list):
        # [{id:id, height:height, weight:weight, fatigue:fatigue}, ]
        id_list = []
        height_list = []
        weight_list = []
        fatigue_list = []
        if len(human_list) > 0:
            return human_list
        else:
            id_list = [id_value for id_value in range(1, number_of_people + 1)]
            height_list = [height for height in range(150, 200)]
            weight_list = [weight for weight in range(40, 120)]
            fatigue_list = [fatigue for fatigue in range(0, 60)]

        human_list = []
        for id in id_list:
            # random을 사용하면서 문제가 있었다. random suffle은 일종의 return값이 존재하지않는다.
            # 단순히 list를 섞을 뿐인데
            # x = random(x) 이렇게 사용했을시에 위에 말햇듯 반환값이 없어서 None이 선언된다.
            random.shuffle(height_list)
            random.shuffle(weight_list)
            random.shuffle(fatigue_list)

            # TODO 181106 원래는 Human class의 객체를 여기서 집어넣었으나
            # 이 부분은 말그대로 Human에 대한 정보 list를 만들기위한 로직이기에
            # dict형식으로 변경했다.

            # human = Human(id, height_list[0], weight_list[0], fatigue_list[0])

            human = {
                'id' : id,
                'height' : height_list[0],
                'weight' : weight_list[0],
                'fatigue' : fatigue_list[0],
            }
            human_list.append(human)
        return human_list

    def simulate(self):
        people = self.human_list
        workout = self.workout
        for human_data in people:
            human = Human(
                id = human_data['id'],
                height = human_data['height'],
                weight = human_data['weight'],
                fatigue= human_data['fatigue'],
            )

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



if __name__ == '__main__':
    # human = Human(1, 177, 75, fatigue=20)
    # human.set_bmi()
    #
    workout = Workout(10)
    #
    # while workout.pt_count > 0:
    #     if round(human.bmi) == 23:
    #         workout.exercise(human)
    #         print("{}일만에 Diet를 성공하셨네요!!! 남은 pt는 {}회 입니다.".format(workout.days, workout.pt_count))
    #         break
    #
    #     if human.fatigue < 90:
    #         workout.days += 1
    #         workout.pt_count -= 1
    #         print("운동을 시작하지")
    #         workout.exercise(human)
    #     else:
    #         workout.days += 1
    #         print("오늘은 좀 쉬어보자")
    #         workout.rest(human)
    simulator = Simulator(workout, 2)
    simulator.simulate()
