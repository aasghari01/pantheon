import os
import re
import csv

log_dir = 'logs'
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

def parse_log_file(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()

    data = []
    for line in lines:
        match = re.match(r"(\d+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)", line)
        if match:
            time = int(match.group(1))
            throughput = float(match.group(2))
            rtt = float(match.group(3))
            loss = float(match.group(4))
            data.append([time, throughput, rtt, loss])
    return data

def convert_all_logs():
    for filename in os.listdir(log_dir):
        if filename.endswith('.log'):
            scheme_profile = filename.replace('.log', '')
            print(f"Parsing {scheme_profile}...")
            parsed_data = parse_log_file(os.path.join(log_dir, filename))
            with open(os.path.join(data_dir, scheme_profile + '.csv'), 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['time', 'throughput_mbps', 'rtt_ms', 'loss_rate'])
                writer.writerows(parsed_data)

if __name__ == "__main__":
    convert_all_logs()
