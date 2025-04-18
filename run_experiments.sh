#!/bin/bash

SCHEMES=("cubic" "bbr" "copa")
PROFILES=("50mbps_10ms" "1mbps_200ms")
DURATION=60

for PROFILE in "${PROFILES[@]}"; do
  case $PROFILE in
    "50mbps_10ms")
      RATE="50Mbps"
      DELAY="5ms"  # one-way
      ;;
    "1mbps_200ms")
      RATE="1Mbps"
      DELAY="100ms"  # one-way
      ;;
  esac

  for SCHEME in "${SCHEMES[@]}"; do
    echo "Running $SCHEME in $PROFILE profile..."

    pantheon $SCHEME \
      --uplink-trace="mm-link --uplink-rate=$RATE --uplink-delay=$DELAY" \
      --downlink-trace="mm-link --downlink-rate=$RATE --downlink-delay=$DELAY" \
      --run-time=$DURATION \
      --save-log="logs/${SCHEME}_${PROFILE}.log"

    echo "Saved logs to logs/${SCHEME}_${PROFILE}.log"
  done
done
