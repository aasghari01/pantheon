import pandas as pd
import matplotlib.pyplot as plt
import os

data_dir = 'data'
plot_dir = 'plots'
os.makedirs(plot_dir, exist_ok=True)

schemes = ['cubic', 'bbr', 'copa']
profiles = ['50mbps', '1mbps']

colors = {
    'cubic': 'blue',
    'bbr': 'green',
    'copa': 'orange'
}

def plot_metric(metric, ylabel, filename):
    for profile in profiles:
        plt.figure(figsize=(10, 6))
        for scheme in schemes:
            df = pd.read_csv(f"{data_dir}/{scheme}_{profile}.csv")
            plt.plot(df['time'], df[metric], label=scheme.upper(), color=colors[scheme])
        plt.xlabel("Time (s)")
        plt.ylabel(ylabel)
        plt.title(f"{ylabel} over Time ({profile})")
        plt.legend()
        plt.grid(True)
        plt.savefig(f"{plot_dir}/{filename}_{profile}.png")
        plt.close()

# Throughput, RTT, Loss plots
plot_metric('throughput_mbps', 'Throughput (Mbps)', 'throughput_comparison')
plot_metric('rtt_ms', 'RTT (ms)', 'rtt_comparison')
plot_metric('loss_rate', 'Loss Rate', 'loss_comparison')

# RTT vs Throughput Summary Graph
rtt_summary = []
for scheme in schemes:
    for profile in profiles:
        df = pd.read_csv(f"{data_dir}/{scheme}_{profile}.csv")
        avg_rtt = df['rtt_ms'].mean()
        avg_tp = df['throughput_mbps'].mean()
        rtt_summary.append((scheme.upper(), profile, avg_rtt, avg_tp))

plt.figure(figsize=(10, 6))
for name, profile, rtt, tp in rtt_summary:
    label = f"{name} ({profile})"
    plt.scatter(rtt, tp, label=label, s=100)
    plt.text(rtt + 1, tp, name, fontsize=9)

plt.xlabel("RTT (ms) — Lower is Better")
plt.ylabel("Throughput (Mbps) — Higher is Better")
plt.title("Protocol Performance Summary")
plt.legend()
plt.grid(True)
plt.savefig(f"{plot_dir}/summary_rtt_vs_throughput.png")
plt.close()
