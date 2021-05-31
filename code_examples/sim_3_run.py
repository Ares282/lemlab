import os
import sys

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import lemlab


if __name__ == "__main__":
    sim_name = "test_sim"

    simulation = lemlab.ScenarioExecutor(path_scenario=f"../scenarios/{sim_name}",
                                         path_results=f"../simulation_results/{sim_name}")
    simulation.run()
