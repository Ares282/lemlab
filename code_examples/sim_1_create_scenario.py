import os
import sys

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import lemlab


if __name__ == "__main__":
    sim_name = "v5_wind_with_forecast"

    scenario = lemlab.Scenario()
    scenario.new_scenario(path_specification="sim_0_config.yaml",
                          scenario_name=f"{sim_name}")
