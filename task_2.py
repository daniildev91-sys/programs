import math

def get_positive_integer():
    """Запрашивает у пользователя положительное целое число с полной валидацией."""
    while True:
        user_input = input("Введите положительное целое число: ").strip()
        
        # Проверка пустого ввода
        if not user_input:
            print("Ошибка: введена пустая строка. Пожалуйста, введите число.")
            continue
        
        # Попытка преобразовать в целое число
        try:
            num = int(user_input)
        except ValueError:
            # Уточняем, была ли попытка ввести дробь
            try:
                float(user_input)
                print("Ошибка: введено дробное число. Требуется целое число.")
            except ValueError:
                print("Ошибка: введены нечисловые символы. Введите целое число.")
            continue
        
        # Проверка на положительность (строго > 0)
        if num < 0:
            print("Ошибка: введено отрицательное число. Требуется положительное.")
            continue
        elif num == 0:
            # 0! = 1 по математическому определению — разрешаем, но уточняем
            print("Замечание: 0 не является положительным, но 0! = 1. Принимаю ввод.")
            return 0
        else:
            return num

def calculate_factorial(n):
    """Вычисляет факториал числа n с использованием math.factorial (оптимизировано)."""
    try:
        return math.factorial(n)
    except (ValueError, OverflowError) as e:
        raise RuntimeError(f"Не удалось вычислить факториал для {n}: {e}")

def main():
    print("Программа для вычисления факториала")
    print("──────────────────────────────────────")
    
    n = get_positive_integer()
    result = calculate_factorial(n)
    print(f"\n {n}! = {result}")

if __name__ == "__main__":
    main()
