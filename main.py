import time
# установка таймера на 25 минут в секундах
setting_the_timer = 25 * 60
# время старта таймера
start_time = time.time()
while True:
    # вычислить сколько секунд осталось до окончания таймера
    remaining_time = setting_the_timer - (time.time() - start_time)
    # выводим оставшееся время в консоль
    print(f"Осталось {remaining_time} секунд.")
    # ждем одну секунду
    time.sleep(1)
    # если время вышло, то выходим из цикла
    if remaining_time <= 0:
        break
print("Таймер завершен")
