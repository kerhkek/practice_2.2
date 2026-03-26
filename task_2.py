import psutil
import time

def get_cpu_usage():
    return psutil.cpu_percent(interval=3)

def get_memory_usage():
    mem = psutil.virtual_memory()
    return mem.percent

def get_disk_usage():
    disk = psutil.disk_usage('/')
    return disk.percent

def main():
    while True:
        cpu = get_cpu_usage()
        memory = get_memory_usage()
        disk = get_disk_usage()

        print(f"Загрузка CPU: {cpu}%")
        print(f"Использованная оперативная память: {memory}%")
        print(f"Загруженность диска (раздел '/'): {disk}%")
        print("-" * 40)
        time.sleep(1)

if __name__ == "__main__":
    main()