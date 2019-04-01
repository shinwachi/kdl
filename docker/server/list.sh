#!/bin/bash
# listInstalledRoots
"$DESTINATION"/knime -application $P2 -nosplash -consolelog \
  -listInstalledRoots \
  -d $DESTINATION | grep org.knime.features
