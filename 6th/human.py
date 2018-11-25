class Human:
    """운동할 사람(?)에 대한 클래스.

    Note: property를 사용해서 0이하의 값이나 실존가능한 최대값을 한정지었다.


    """

    # TODO 20181108 Human에 대한 주석 처리 _done
    # TODO 20181108 Human에 근육량 추가(required). _done
    # TODO 20181108 Human에 지방량 추가(optional). _done
    # TODO 20181108 Human에 근육량과 지방량으로 weight를 산출하는 로직 추가 _done
    # TODO 20181108 Workout에 근육량이 증가하는 로직 추가 _done
    # TODO 20181119 전체적인 주석 처리 수정(alms에 맞게)
    def __init__(
            self, id, height,
            muscle, fat,
            endurance, fatigue=0,
    ):
        """
        Human이 생성될때 기본적으로 갖추어야될 부분.

        Args :
            id:
            height:
            muscle : 제지방량 or 근육량 (골격근량 X)
            fat : 지방량
            endurance:
            fatigue:

        Attributes :
            # id (int): 구분자 역할.
            # muscle : 근육량
            # fat : 지방량
            # height (int) : 키
            # weight (int) : 몸무게
            # endurance (int) : 인내력
            # fatigue (int) : 운동을 할때 피로도로 그 횟수를 제한할 수 있게 구현.
            # bmi : 비만도
        """
        self.id = id
        self.height = height
        self.muscle = muscle
        self.fat = fat
        self.weight = self.get_calculated_weight()
        self.fatigue = fatigue
        self.endurance = endurance
        self.bmi = self.get_calculated_bmi()

    # TODO 181106 : 좀 더 객체의 내용을 알기 쉽도록 __str__을 구현했다.
    def __str__(self):
        # TODO 181109 : formatting을 할때 Default 글자수를 지정할 수가 있다.
        return "id : {:<5}, height : {:<4}, weight : {:<4}, fatigue : {:<5}, bmi : {:<5}".format(
            self.id, self.height, self.weight, self.fatigue, self.bmi)

    def get_calculated_weight(self):
        """instance의 체중을 계산해서 반환하는 함수

        Notes:
            instance attribute를 바탕으로 동작하는 함수라서 arguments없이 동작합니다.

        Args:
            -

        Returns:
            weight (float)

        """
        # 인간이 가지고 있는 무기질의 양.
        mineral = 3.2

        weight = self.muscle + self.fat + mineral
        return weight

    def get_calculated_standard_weight(self):
        """instance의 표준 몸무게는 계산해서 반환하는 함수

        Notes:
            instance attribute를 바탕으로 동작하는 함수라서 arguments없이 동작합니다.

        Args:
            -

        Returns:
            standard_weight (float)

        """
        standard_weight = (self.height - 100) * 0.95

        return standard_weight

    # 비만도를 계산해서 넣어주는 로직이다.
    def get_calculated_bmi(self):
        """비만도를 계산해서 self.bmi에 할당하는 함수.

        Notes:
            instance attribute를 바탕으로 동작하는 함수라서 arguments없이 동작합니다.

        Args:
            -

        Returns:
            -

        """

        bmi = round(self.weight / ((self.height / 100) ** 2), 1)
        self.bmi = bmi

    # endurance를 0으로 되돌리는 로직이다.
    # TODO 20181108 한달에 한번씩 reset시켜야하기 때문에
    def get_reseted_endurance(self):
        """endurance를 0으로 reset해서 self.bmi에 할당하는 함수

        Notes:

        Returns:
        """
        reseted_endurance = 0
        self.endurance = reseted_endurance

    def add_endurance(self):
        self.endurance += 1

    def calculate_fatigue(self):
        weight = self.weight
        if weight > 120:
            fatigue = round(weight * 0.25)
        elif weight > 100:
            fatigue = round(weight * 0.22)
        elif weight > 80:
            fatigue = round(weight * 0.20)
        elif weight > self.get_calculated_standard_weight() - 10:
            fatigue = round(weight * 0.15)
        else:
            fatigue = round(weight * 0.22)
        return fatigue

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height < 0 or height > 250:
            raise ValueError("height below 0 or above 250 are not possible")
        self._height = height

    @property
    def muscle(self):
        return self._muscle

    @muscle.setter
    def muscle(self, muscle):
        if muscle < 20 or muscle > self.height / 2:
            raise ValueError("muscle below 20 or above height/2 are not possible")
        self._muscle = round(muscle, 1)

    @property
    def fat(self):
        return self._fat

    @fat.setter
    def fat(self, fat):
        if fat < 0 or fat > 450:
            raise ValueError("fat below 0 or above 450 are not possible")
        self._fat = round(fat, 1)

    @property
    def fatigue(self):
        return self._fatigue

    # 피로도는 100에 가까울수록 좋지않다.
    @fatigue.setter
    def fatigue(self, fatigue):
        if fatigue < 0:
            return
        self._fatigue = 0

    @property
    def endurance(self):
        return self._endurance

    @endurance.setter
    def endurance(self, endurance):
        if endurance < 0:
            return
        self._endurance = 0


if __name__ == "__main__":
    human1 = Human(
        id=1,
        height=177,
        muscle=50,
        fat=30,
        fatigue=20,
        endurance=2,
    )
    human2 = Human(
        id=2,
        height=178,
        muscle=50,
        fat=20,
        fatigue=21,
        endurance=2
    )

    print(
        "첫번째 사람은 {}, \n"
        "두번째 사람은 {}. ".format(human1, human2)
    )
