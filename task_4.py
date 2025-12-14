import random

def guess_the_number():
    secret = random.randint(1, 100)
    max_attempts = 7
    print("Программа 'Угадай число' ")
    print(f"Я загадал число от 1 до 100. У вас есть {max_attempts} попыток, чтобы угадать его!\n")

    for attempt in range(1, max_attempts + 1):
        # Запрос и валидация ввода
        while True:
            user_input = input(f"Попытка {attempt}/{max_attempts}. Ваш вариант: ").strip()
            if not user_input:
                print("Пустой ввод. Пожалуйста, введите число.")
                continue
            try:
                guess = int(user_input)
                if guess < 1 or guess > 100:
                    print("Число должно быть от 1 до 100. Попробуйте снова.")
                else:
                    break
            except ValueError:
                print("Это не число. Введите целое число от 1 до 100.")

        # Проверка и подсказки
        if guess < secret:
            print("Слишком маленькое!")
        elif guess > secret:
            print("Слишком большое!")
        else:
            print(f"\n Поздравляю! Вы угадали число {secret} с {attempt}-й попытки!")
            return

    # Если попытки закончились
    print(f"\n Попытки исчерпаны. Загаданное число было: {secret}.")

if __name__ == "__main__":
    guess_the_number()
