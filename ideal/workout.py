from abc import *

# 추상화 클래스는 설계도를 위한 부분이다.
# 상속했을때 기본클래스의 메서드를 토대로 overriding하는것은 가능하지만
# 사용하는 것은 불가능하다(설계도일 뿐이니까.)

# class Workout(metaclass=ABCMeta):
#
#     @abstractmethod
#     def do(self, human, workout_mount):
#         pass
#
#     @abstractmethod
#     def rest(self, human):
#         pass

# Workout에는 공통적으로 사용되야하는 method가 존재한다.

class Workout:

    def do(self, human, workout_mount):
        pass

    def rest(self, human):
        pass

    # 운동을 시행하기 전에
    # TODO:Default 값을 넣는 방법이 맞는지 확인 필요 (o)
    def check(self, human, workout_mount=1):
        if human.limit > workout_mount:
            self.do(human, workout_mount)
        self.rest(human)

    # 총 운동량을 더하는 메소드
    def get_total_workout(self, human, workout_mount):
        human.total_workout += workout_mount

    # 총 운동량을 줄이는 메소드
    def lose_total_workout(self, human):
        human.total_workout -= 10


class WeightTraining(Workout):

    def do(self, human, workout_mount=1):
        human.get_muscle(workout_mount)
        human.get_fat(workout_mount)

    def rest(self, human):
        human.lose_muscle()
        human.get_fat()
        human.lose_total_workout()


class Cardio(Workout):
    def do(self, human, workout_mount=1):
        human.lose_muscle(workout_mount)
        human.lose_fat(workout_mount)

    def rest(self, human):
        human.lose_muscle()
        human.get_fat()
        human.lose_total_workout()
