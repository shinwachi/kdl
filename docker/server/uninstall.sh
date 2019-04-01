#!/bin/bash
# uninstall tool
# e.g., uninstall org.knime.features.ext.chem.tools.feature.group
./knime -application org.eclipse.equinox.p2.director -nosplash -consolelog \
  -r $REPOSITORIES \
  -u $1 \
  -d $DESTINATION
echo $?
