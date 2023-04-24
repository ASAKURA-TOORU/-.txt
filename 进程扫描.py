import psutil

# 获取所有进程对象
all_processes = psutil.process_iter()

# 遍历进程对象并打印信息
for process_list in all_processes:
    print(f"进程名称: {process_list.name()}, 进程ID: {process_list.pid}")

# 获取用户输入的进程名称或进程ID
process_name_or_id = input("请输入要扫描的进程名称或进程ID：")

# 尝试将用户输入的值转换为整数，如果能够转换成功则说明用户输入的是进程ID
try:
    process_id = int(process_name_or_id)
    process = psutil.Process(process_id)
except ValueError:
    # 如果无法转换为整数，则说明用户输入的是进程名称
    processes = [p for p in psutil.process_iter() if p.name() == process_name_or_id]
    if processes:
        process = processes[0]
    else:
        process = None

if process is not None:

    # 扫描进程内存
    memory_info = process.memory_info()

    # 解释内存信息
    pmem = {
        "常驻集 (RSS)": memory_info.rss / 1024 / 1024,
        "虚拟内存 (VMS)": memory_info.vms / 1024 / 1024,
        "页面故障数": memory_info.num_page_faults,
        "物理内存峰值": memory_info.peak_wset / 1024 / 1024,
        "实际物理内存 (WSS)": memory_info.wset / 1024 / 1024,
        "分页池峰值": memory_info.peak_paged_pool / 1024 / 1024,
        "分页池": memory_info.paged_pool / 1024 / 1024,
        "非分页池峰值": memory_info.peak_nonpaged_pool / 1024 / 1024,
        "非分页池": memory_info.nonpaged_pool / 1024 / 1024,
        "页面文件": memory_info.pagefile / 1024 / 1024,
        "页面文件峰值": memory_info.peak_pagefile / 1024 / 1024,
        "私有内存": memory_info.private / 1024 / 1024
    }

    # 输出内存信息
    for k, v in pmem.items():
        print(f"{k}: {v:.2f} MB")
else:
    print(f"没有找到名为'{process_name_or_id}'的进程或进程ID")