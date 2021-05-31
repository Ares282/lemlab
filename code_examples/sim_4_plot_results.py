import os
import sys

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import lemlab


if __name__ == "__main__":
    sim_name = "test_sim"

    analysis = lemlab.ScenarioAnalyzer(path_results=f"../simulation_results/{sim_name}",
                                       show_figures=True,
                                       save_figures=True)
    analysis.run_analysis()
