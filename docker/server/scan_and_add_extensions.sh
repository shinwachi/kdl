#!/bin/bash
kdlc -i /io/chem_example_2.knwf -o /dev/shm/temp_out.kdl
cat /dev/shm/temp_out.kdl | grep feature_symbolic_name | sed 's/.*: "\(.*\)\".*/\1/' > /dev/shm/temp_install.txt
cat /dev/shm/temp_install.txt | while read line; do
	/server/install.sh $line
done