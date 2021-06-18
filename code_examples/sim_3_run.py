import os
import sys

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import lemlab


if __name__ == "__main__":
    # sim_name_list = ["v4_wind_with_controllable", "v4_wind_with_forecast", "v4_wind_with_halferror", "v4_wind_with_perfect", "v4_wind_with_out"]
    sim_name_list = ["v5_wind_with_forecast"]

    for sim_name in sim_name_list:
        simulation = lemlab.ScenarioExecutor(path_scenario=f"../scenarios/{sim_name}",
                                            path_results=f"../simulation_results/{sim_name}")
        simulation.run()
