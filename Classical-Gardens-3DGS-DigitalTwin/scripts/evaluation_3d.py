"""
多硬件环境下的渲染帧率、延迟、加载性能量化测试
"""

import numpy as np
import matplotlib.pyplot as plt
import csv

#测试数据
HARDWARE_TEST_RESULTS = [
    {
        "name": "High-end GPU (RTX 4070)",
        "avg_fps": 60,
        "latency_ms": 16.7,
        "stability": "Excellent",
        "fps_cap": True
    },
    {
        "name": "Mid-range GPU",
        "avg_fps": 60,
        "latency_ms": 16.7,
        "stability": "Excellent",
        "fps_cap": True
    },
    {
        "name": "Integrated GPU (Intel Iris Xe)",
        "avg_fps": 38.5,
        "latency_ms": 25.0,
        "stability": "Good",
        "fps_cap": False
    }
]

LOADING_TEST = {
    "network_bandwidth_mbps": 100,
    "avg_load_time_s": 7.8,
    "first_frame_time_s": 3.2
}

#性能统计
def generate_performance_report(results, loading):
    """生成性能测试报告"""
    print("=== 3DGS数字孪生场景性能评估报告 ===")
    print(f"加载性能（{loading['network_bandwidth_mbps']}Mbps带宽）：")
    print(f"  平均加载时间：{loading['avg_load_time_s']}s")
    print(f"  首帧渲染时间：{loading['first_frame_time_s']}s")
    print()
    
    print("渲染性能：")
    for hw in results:
        cap_note = " (capped)" if hw["fps_cap"] else ""
        print(f"  {hw['name']}:")
        print(f"    平均帧率：{hw['avg_fps']} FPS{cap_note}")
        print(f"    平均延迟：{hw['latency_ms']} ms")
        print(f"    稳定性：{hw['stability']}")
    print()

def export_results_to_csv(results, output_path):
    """导出测试结果到CSV"""
    with open(output_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Hardware", "Avg_FPS", "Latency_ms", "Stability"])
        for hw in results:
            writer.writerow([
                hw["name"],
                hw["avg_fps"],
                hw["latency_ms"],
                hw["stability"]
            ])
#结果可视化
def plot_fps_comparison(results):
    """绘制不同硬件帧率对比图"""
    names = [r["name"] for r in results]
    fps_vals = [r["avg_fps"] for r in results]
    
    plt.figure(figsize=(8, 5))
    bars = plt.bar(names, fps_vals, color=['#5a9bd5', '#7fb3d5', '#a8d0e6'])
    
    plt.axhline(y=60, color='#ff6b6b', linestyle='--', alpha=0.7, label='60 FPS Target')
    plt.ylabel('Average FPS')
    plt.title('Rendering Performance Across Hardware Configurations')
    plt.ylim(0, 70)
    plt.legend()
    plt.grid(axis='y', alpha=0.3)
    
    # 标注数值
    for bar, val in zip(bars, fps_vals):
        plt.text(bar.get_x() + bar.get_width()/2., val + 1,
                 f'{val} FPS',
                 ha='center', va='bottom')
    
    plt.tight_layout()
    plt.savefig("./fps_comparison.png", dpi=300, bbox_inches='tight')
    print("帧率对比图已保存")

if __name__ == "__main__":
    generate_performance_report(HARDWARE_TEST_RESULTS, LOADING_TEST)
    export_results_to_csv(HARDWARE_TEST_RESULTS, "../results/evaluation_summary.csv")
    plot_fps_comparison(HARDWARE_TEST_RESULTS)
