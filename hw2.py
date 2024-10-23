import re

# Функція для генерації чисел з тексту
def generator_numbers(text: str):
    for number in re.findall(r"\d+\.\d+", text):
        yield float(number)

# Функція для підсумовування чисел з генератора
def sum_profit(text: str, func):
    return sum(func(text))

# Приклад використання
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income:.2f}")

