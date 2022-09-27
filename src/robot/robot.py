from typing import Any

import pybullet as p


class RobotIiwa:
    def __init__(
            self,
            robot_urdf: str,
            initial_pos: list[float],
            initial_orientation: list[float]) -> None:
        self.id = p.loadURDF(robot_urdf, initial_pos, initial_orientation)

        self.__control_mode = p.POSITION_CONTROL
        self.__joint_ids = list(range(p.getNumJoints(self.id)))

    def send_command(self, command: list[float]) -> None:
        assert len(command) == len(self.__joint_ids)
        p.setJointMotorControlArray(
            self.id,
            self.__joint_ids,
            self.__control_mode,
            targetPositions=command)

    def get_states(self) -> Any:
        return p.getJointStates(self.id, self.__joint_ids)

    def get_positions(self) -> list[float]:
        return [state[0] for state in self.get_states()]

    def get_velocities(self) -> list[float]:
        return [state[1] for state in self.get_states()]
