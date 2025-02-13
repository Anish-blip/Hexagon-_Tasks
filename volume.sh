#!/bin/bash

r=5
volume=$(echo "scale=3; (4/3) * 3.14159 * ($r^3)" | bc -l)
echo "The volume of the sphere is: $volume"
