import tkinter as tk
import psutil

# Создаем главное окно
root = tk.Tk()
root.title("Системный монитор")
root.geometry("500x300")
root.resizable(False, False)

# Заголовки и метки для отображения информации
cpu_label = tk.Label(root, text="CPU: ", font=("Arial", 12))
cpu_label.pack(pady=10)

cpu_canvas = tk.Canvas(root, width=350, height=20, bg='white')
cpu_canvas.pack()

memory_label = tk.Label(root, text="Память: ", font=("Arial", 12))
memory_label.pack(pady=10)

memory_canvas = tk.Canvas(root, width=350, height=20, bg='white')
memory_canvas.pack()

disk_label = tk.Label(root, text="Диск: ", font=("Arial", 12))
disk_label.pack(pady=10)

disk_canvas = tk.Canvas(root, width=350, height=20, bg='white')
disk_canvas.pack()


def update_canvas(canvas, percent):
    """Обновляет прогресс-бар на холсте"""
    canvas.delete("all")
    fill_width = (percent / 100) * 350
    canvas.create_rectangle(0, 0, fill_width, 20, fill='blue')
    canvas.create_rectangle(0, 0, 350, 20, outline='black', width=1)


def update_stats():
    """Обновляет показатели системы"""
    # Получение данных
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage('/').percent

    # Обновление текста
    cpu_label.config(text=f"CPU: {cpu_percent}%")
    memory_label.config(text=f"Память: {memory_percent}%")
    disk_label.config(text=f"Диск: {disk_percent}%")

    # Обновление прогрессбаров
    update_canvas(cpu_canvas, cpu_percent)
    update_canvas(memory_canvas, memory_percent)
    update_canvas(disk_canvas, disk_percent)

    # Планируем следующий вызов через 1 секунду
    root.after(1000, update_stats)


# Запуск обновления
update_stats()

# Запуск главного цикла
root.mainloop()
