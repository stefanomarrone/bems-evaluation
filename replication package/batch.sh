#!/bin/bash

./Sim_new full_summer.fspn > /dev/null
./Sim_new full_winter.fspn > /dev/null
./Sim_new partial_summer.fspn > /dev/null
./Sim_new partial_winter.fspn > /dev/null
./Sim_new sensitivity_1.fspn > /dev/null
./Sim_new sensitivity_2.fspn > /dev/null
./Sim_new sensitivity_3.fspn > /dev/null
./Sim_new sensitivity_4.fspn > /dev/null

python3 plot_generation.py