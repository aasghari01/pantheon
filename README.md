# pantheon
A network performance benchmarking suite to evaluate congestion control algorithms under varied conditions.
NetFlowEval
A network performance benchmarking suite to evaluate congestion control algorithms under varied conditions.

Table of Contents
Overview

Installation

Usage

Experiments

Data Analysis

Contributing

Overview
NetFlowEval provides a framework for benchmarking and comparing various congestion control (CC) algorithms under different network conditions. This tool integrates with Pantheon and MahiMahi to simulate realistic network environments, allowing you to evaluate algorithms' performance in terms of throughput, latency, packet loss, and other key metrics.

With this suite, you can easily run experiments and analyze performance data to understand which CC algorithm performs best under different network scenarios.

Installation
To use NetFlowEval, follow these steps:

Clone the Repository:
git clone https://github.com/yourusername/NetFlowEval.git
cd NetFlowEval
Dependencies:
Pantheon: A community-driven platform that integrates multiple congestion control algorithms. Pantheon GitHub

MahiMahi: A network emulation tool for simulating realistic network conditions. MahiMahi GitHub

Make sure you are using Linux or a Linux Virtual Machine.

Install Pantheon Dependencies:
Follow the instructions in the Pantheon README to install the necessary dependencies for your environment.

Install MahiMahi:
For Ubuntu, you can install MahiMahi with the following command:

sudo apt-get install mahimahi
Usage
Running Experiments:
To start an experiment comparing CC algorithms, run the provided scripts with your desired configurations. Here's an example of running a test between TCP Cubic and BBR:


python run_experiment.py --algorithms cubic,bbr --duration 60 --scenario low_latency
This command will:

Run the experiment for 60 seconds.

Compare the Cubic and BBR algorithms.

Use the low-latency network scenario (50 Mbps, 10 ms RTT).

Analyzing Results:
After completing an experiment, you can analyze the results using the provided analysis scripts. For example:


python analyze_results.py --data results/cubic_bbr_low_latency.csv
This will generate performance graphs (throughput, RTT, and loss) and statistical comparisons.

Experiments
This repository includes several predefined network profiles for testing congestion control algorithms:

Low-latency, high-bandwidth:

Example: 50 Mbps, 10 ms RTT

High-latency, constrained-bandwidth:

Example: 1 Mbps, 200 ms RTT

You can add more profiles or modify the existing ones in the network_profiles/ directory.

Adding a New CC Algorithm:
To add a new congestion control algorithm, you will need to:

Implement the algorithm in Pantheon.

Add support for the algorithm in the run_experiment.py script.

Data Analysis
After running experiments, you'll have a set of performance metrics such as throughput, latency, and packet loss. Here’s how you can analyze the data:

Throughput over time:
Plot the throughput for each algorithm to visualize ramp-up behaviors.

Loss rate:
Analyze the packet loss to evaluate how each algorithm reacts under different network conditions.

RTT Comparison:
Compare the average and 95th-percentile RTTs across various test scenarios.

RTT vs Throughput:
Create a scatter plot comparing RTT against throughput for all algorithms tested.

You can use the data_analysis.py script to automate the analysis of your experiment results and generate graphs.

Contributing
Feel free to contribute! Here's how you can help:

Fork the repository and create a new branch for your feature or fix.

Open a Pull Request with a clear description of your changes and the results of your experiments.

Report Issues: If you encounter bugs or performance issues, open an issue, and we’ll investigate it together!

Acknowledgments
Pantheon: A project by Stanford University to study congestion control algorithms. Pantheon GitHub

MahiMahi: A tool for network emulation used in this project. MahiMahi GitHub
