from human import Human


class Workout:
    """
        운동에 대한 추상화 클래스

        Attributes :
            # human (Human()) : Human 클래스의 인스턴스여야한다.
            # intensity : 운동강도
    """
    days = 0

    def __init__(self, human, intensity):
        self.human = human
        self.intensity = intensity

    # TODO 181109 유산소와 근력운동으로 분할해서 운동을 시행하도록 수정
    def exercise(self):
        pass

    def rest(self):
        pass

class WeightTraining(Workout):
    muscle_standard_for_NOVICE = 30
    muscle_growth_rate_for_NOVICE = 0.05
    muscle_standard_for_NORMAL = 40
    muscle_growth_rate_for_NORMAL = 0.04
    muscle_growth_rate_for_MUSCULAR = 0.02

    def exercise(self):
        human = self.human
        intensity = self.intensity
        if human.muscle < self.muscle_standard_for_NOVICE:
            human.muscle += self.muscle_growth_rate_for_NOVICE * intensity
            human.fatigue += human.calculate_fatigue()
        elif human.muscle < self.muscle_standard_for_NORMAL:
            human.muscle += self.muscle_growth_rate_for_NORMAL * intensity
            human.fatigue += human.calculate_fatigue()
        else:
            human.muscle += self.muscle_growth_rate_for_MUSCULAR * intensity
            human.fatigue += human.calculate_fatigue()

    def rest(self):
        human = self.human
        human.fatigue -= 30


class Cardio(Workout):




if __name__ == '__main__':
    human = Human(
        id=1,
        height=177,
        muscle=50,
        fat=30,
        fatigue=20,
        endurance=2,
    )
    # workout = Workout(10, human)
    workout = WeightTraining(human, 10)
    print(workout.human)

    # while workout.pt_count > 0:
    #     human = workout.human
    #     if round(human.bmi) == 23:
    #         workout.exercise()
    #         print("{}일만에 Diet를 성공하셨네요!!! 남은 pt는 {}회 입니다.".format(workout.days, workout.pt_count))
    #         break
    #
    #     if human.fatigue < 90:
    #         workout.days += 1
    #         workout.pt_count -= 1
    #         print("운동을 시작하지")
    #         workout.exercise()
    #     else:
    #         workout.days += 1
    #         print("오늘은 좀 쉬어보자")
    #         workout.rest()
    #     # while문이 끝난 경우
    #     if workout.pt_count == 0:
    #         print("{}일 동안 열심히 했지만 아직 목표치에 도달하지 못했네요 ㅠㅠ "
    #               "조금 더 노력하면 목표치에 도착할 수 있을거에요!!".format(workout.days))
