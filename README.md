# Programming Assignment 3: Congestion Control Protocol Analysis with Pantheon

**Course:** Computer Networks — Spring 2025  
**Due Date:** April 17, 2025 – 11:59PM  
**Author:** Atiqullah Asghari 
**GitHub Repo:** [https://github.com/aasghari01/pantheon.git](https://github.com/aasghari01/pantheon.git)

## Directory Structure

. ├── data/ # Parsed CSV results ├── logs/ # Raw log files from experiments ├── plots/ # All generated plots ├── parse_logs.py # Log parsing script ├── plot_results.py # Plotting and visualization script ├── run_experiment.sh # Main runner script for tests └── README.md # This file

##  Experiment Setup

 # equirements

- **OS:** Linux (native or via VM)
- **Tools:**
  - Pantheon: https://github.com/StanfordSNR/pantheon
  - Mahimahi: for network emulation
  - Python 3 + `pandas`, `matplotlib`
  - Bash

# Setup Instructions

1. **Clone Pantheon**
   git clone https://github.com/StanfordSNR/pantheon.git
   cd pantheon
   ./install_deps.sh
Install Mahimahi

sudo apt install mahimahi
Clone this assignment repository



git clone https://github.com/aasghari01/pantheon.git
cd pantheon
chmod +x run_experiment.sh
./run_experiment.sh
 Experiment Overview
Protocols Tested
Cubic

BBR

Copa

Network Conditions
Scenario A: 50 Mbps, 10 ms RTT

Scenario B: 1 Mbps, 200 ms RTT

Each test runs for 60 seconds and captures throughput, RTT, and loss rate.

Output & Analysis
Results Location
data/: Clean CSV files from parsed logs

logs/: Mahimahi + Pantheon raw logs

plots/:

Throughput over time

RTT over time

Loss rate over time

Summary graph (Throughput vs. RTT)

Key Insight: Summary Graph
X-axis: 95th percentile RTT (lower is better)

Y-axis: Throughput (higher is better)

Best-performing protocols appear top-right

Script Overview
run_experiment.sh: Automates all protocol tests in both scenarios

parse_logs.py: Extracts data for graphing

plot_results.py: Generates and saves all visualizations

All scripts are commented and runnable as-is on Linux.

Lessons Learned
Challenge: [e.g., Handling raw log formats, tuning Mahimahi, etc.]


Reproducibility

./run_experiment.sh
python3 parse_logs.py
python3 plot_results.py
All logs and plots will be created in their respective folders.


