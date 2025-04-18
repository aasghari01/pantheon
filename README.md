# Programming Assignment 3 – Congestion Control Evaluation with Pantheon

## Overview

This project simulates running congestion-control algorithms (Cubic, BBR, Copa) in varied network conditions using Pantheon and Mahimahi. Since these tools are not available on Windows, synthetic data is used to demonstrate the process.

## Chosen Algorithms

- **Cubic**: TCP-based loss-driven congestion control.
- **BBR**: Bottleneck Bandwidth and Round-trip propagation time.
- **Copa**: Delay-sensitive and adaptive congestion control.

## Network Profiles

1. **High bandwidth, low latency** – 50 Mbps, 10 ms RTT
2. **Low bandwidth, high latency** – 1 Mbps, 200 ms RTT

## Project Structure

