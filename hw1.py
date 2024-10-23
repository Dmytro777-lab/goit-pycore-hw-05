def caching_fibonacci():
    cache = {}  # Створюємо порожній словник для кешування

    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]  # Повертаємо значення з кешу, якщо воно вже було обчислено

        # Обчислюємо та зберігаємо результат у кеші
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci  # Повертаємо функцію fibonacci

# Приклад використання:
# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
