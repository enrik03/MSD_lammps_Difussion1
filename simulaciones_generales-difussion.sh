#!/bin/bash
lammps < 90-10.in
python3 -c'import MSD1; MSD1.MSD(10000 + 1000,100000,1000000,1000,posicion9_1.xyz)'
python3 MSD2.py
#lammps < 80-20.in
#lammps < 70-30.in
#lammps < 60-40.in

