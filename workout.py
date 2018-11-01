from abc import *


class Workout(metaclass=ABCMeta):

    @abstractmethod
    def do(self, human, workout_mount):
        pass

    @abstractmethod
    def rest(self, human):
        pass


class WeightTraining(Workout):

    def do(self, human, workout_mount):
        human.get_muscle(workout_mount)
        human.get_fat(workout_mount)

    def rest(self, human):
        human.lose_muscle()
        human.get_fat()
        human.lose_total_workout()

    # TODO:Default 값을 넣는 방법이 맞는지 확인 필요
    def check(self, human, workout_mount=1):
        if human.limit > workout_mount:
            self.do(human, workout_mount)
        self.rest(human)


class Cardio(Workout):
    def do(self, human, workout_mount=1):
        human.lose_muscle(workout_mount)
        human.lose_fat(workout_mount)

    def rest(self, human):
        human.lose_muscle()
        human.get_fat()
        human.lose_total_workout()

    def check(self, human, workout_mount=1):
        if human.limit > workout_mount:
            self.do(human, workout_mount)
        self.rest(human)