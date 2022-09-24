import time

import pybullet as p

import src.utils.constants as constants
from src.compute_command.compute_command import dummy_command
from src.utils.create_simulation import create_simulation

if __name__ == '__main__':
    client, robot = create_simulation()
    for i in range(constants.MAX_SIMULATION_STEPS):
        if (i % constants.COMMAND_PERIOD_STEPS) == 0:
            joint_positions = robot.get_positions()
            command = dummy_command(joint_positions)
            robot.send_command(command)
        p.stepSimulation()
        time.sleep(constants.TIMESTEP)
    p.disconnect()
