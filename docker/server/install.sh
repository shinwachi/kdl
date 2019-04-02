#!/bin/bash
# uninstall tool
# e.g., install org.knime.features.ext.chem.tools.feature.group
"$DESTINATION"/knime -application $P2 -nosplash -consolelog -d $DESTINATION -r $REPOSITORIES \
  -i $1 && echo $?
echo $?
