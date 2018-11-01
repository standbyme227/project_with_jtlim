from Project_with_jtlim.human import Human


class Simulator:

    # TODO: 운동 강도에 제한 사항이 있어야할지 확인.
    # TODO: 운동 횟수는 7회로 제한한다. (일주일 기준)
    def __init__(self, human_id, intensity, workout_mount):
        self.human = Human(human_id)