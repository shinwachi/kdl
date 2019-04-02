#!/bin/bash
# listInstalledRoots
"$DESTINATION"/knime -application $P2 -nosplash  \
  -listInstalledRoots \
  -d $DESTINATION | grep org.knime.features
