#!/bin/bash

./Sim_new full_summer.fspn > /dev/null
echo "Summer Full"
./Sim_new full_winter.fspn > /dev/null
echo "Winter Full"
./Sim_new partial_summer.fspn > /dev/null
echo "Summer Partial"
./Sim_new partial_winter.fspn > /dev/null
echo "Winter Partial"
./Sim_new sensitivity_1.fspn > /dev/null
echo "Users 1"
./Sim_new sensitivity_2.fspn > /dev/null
echo "Users 2"
./Sim_new sensitivity_3.fspn > /dev/null
echo "Users 3"
./Sim_new sensitivity_4.fspn > /dev/null
echo "Users 4"
./Sim_new threshold_4.fspn > /dev/null
echo "Threshold 4"
./Sim_new threshold_6.fspn > /dev/null
echo "Threshold 6"
./Sim_new threshold_8.fspn > /dev/null
echo "Threshold 8"

python3 plot_generation.py
