import threading
import time
from colorama import init, Fore
import os

# Объект блокировки для синхронизации вывода в консоль
lock = threading.Lock()

def timer_function(name, interval):
    """
    функция работы таймера
    """
    with lock:
        print(Fore.RED + f"Таймер {name}: ожидание...")

    time.sleep(1)  # для эффекта ожидания

    with lock:
        print(Fore.YELLOW + f"Таймер {name}: отсчет...")

    for remaining in range(interval, 0, -1):
        with lock:
            print(Fore.BLUE + f"Таймер {name}: осталось {remaining} секунд")
        time.sleep(1)


    with lock:
        print(Fore.GREEN + f"Таймер {name}: сработал!")

    # звук по окончании таймера (должен быть скачен на пк)
    try:
        os.startfile("soundofcar.mp3")
    except Exception as e:
        with lock:
            print(Fore.RED + f"Ошибка воспроизведения звука для таймера {name}: {e}")

def run():
    """
    функция запуска работы таймера
    """
    try:
        num_timers = int(input("Введите количество таймеров (от 1 до 10): "))
        if not 1 <= num_timers <= 10:
            print(Fore.MAGENTA + "Количество таймеров должно быть от 1 до 10.")
            return
    except ValueError:
        print(Fore.RED + "Пожалуйста, введите целое число от 1 до 10.")
        return

    timers = []
    for i in range(1, num_timers + 1):
        try:
            interval = int(input(f"Введите желаемое время работы таймера {i} (в секундах): "))
            if interval <= 0:
                print(Fore.RED + "Необходимо ввести целое положительное число!")
                return
            t = threading.Thread(target=timer_function, args=(f"#{i}", interval))
            timers.append(t)
        except ValueError:
            print(Fore.RED + "Необходимо ввести целое положительное число!")
            return

    for t in timers:
        t.start()

    for t in timers:
        t.join()

    print(Fore.RESET + "Все таймеры завершили свой цикл.")

run()
