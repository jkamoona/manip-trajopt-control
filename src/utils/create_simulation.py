from typing import Any

import pybullet as p
import pybullet_data
from src.robot.robot import RobotIiwa

PHYSICS_CLIENT = Any


def create_simulation() -> tuple[PHYSICS_CLIENT, RobotIiwa]:
    physicsClient = p.connect(p.GUI)  # or p.DIRECT for non-graphical version
    p.setAdditionalSearchPath(pybullet_data.getDataPath())  # optionally
    p.setGravity(0, 0, -9.81)
    startPos = [0., 0, 0]
    startOrientation = p.getQuaternionFromEuler([0, 0, 0])
    robot = RobotIiwa("kuka_iiwa/model.urdf", startPos, startOrientation)
    return physicsClient, robot
