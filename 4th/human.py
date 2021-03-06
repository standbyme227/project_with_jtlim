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

    def __init__(self, id, height, weight, fatigue=0):
        self.id = id
        self.height = height
        self.weight = weight
        self.fatigue = fatigue
        # TODO 181106 : 예시를 보고했으나, 이렇게 넣어도 되는건지 확실치가 않다.
        self.bmi = self.set_bmi()

    # TODO 181106 : 좀 더 객체의 내용을 알기 쉽도록 __str__을 구현했다.
    def __str__(self):
        return "id : {}, height : {}, weight : {}, fatigue : {}".format(
            self.id, self.height, self.weight, self.fatigue)

    # 비만도를 계산해서 넣어주는 로직이다.
    def set_bmi(self):
        self.bmi = round(self.weight / ((self.height / 100) ** 2), 1)
        # print("{}의 BMI는 {}".format(self.id, self.bmi))
        return self.bmi


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
        self._weight = round(weight, 1)

    # 피로도는 100에 가까울수록 좋지않다.
    @fatigue.setter
    def fatigue(self, fatigue):
        if fatigue < 0:
            return
        self._fatigue = 0


if __name__ == '__main__':
    human1 = Human(
        id=1,
        height=177,
        weight=77,
        fatigue=20
    )
    human2 = Human(
        id=2,
        height=178,
        weight=79,
        fatigue=21
    )

    print(
        "첫번째 사람은 {}, "
        "두번째 사람은 {}. ".format(human1, human2)
    )
