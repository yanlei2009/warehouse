import threading

# 获取当前进程中的所有线程
threads = threading.enumerate()

# 打印所有线程的名称
for thread in threads:
    print(thread.name)