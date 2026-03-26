import random  # Подключаем модуль для случайного выбора

print("--- Добро пожаловать в игру Камень-Ножницы-Бумага! ---")

# Список вариантов
options = ["камень", "ножницы", "бумага"]

# Начинаем бесконечный цикл, чтобы играть много раз
while True:
    # 1. Ход пользователя
    user_choice = input("\nТвой ход (камень, ножницы, бумага) или 'выход' для завершения: ").lower()

    if user_choice == "выход":
        print("Спасибо за игру! До встречи.")
        break  # Выходим из цикла

    if user_choice not in options:
        print("Ой, кажется, ты ошибся в слове. Попробуй еще раз!")
        continue  # Возвращаемся в начало цикла

    # 2. Ход компьютера (Мозг программы)
    computer_choice = random.choice(options)
    print(f"Компьютер выбрал: {computer_choice}")

    # 3. Логика победы
    if user_choice == computer_choice:
        print("Ничья! 🤝")
    elif (user_choice == "камень" and computer_choice == "ножницы") or \
         (user_choice == "ножницы" and computer_choice == "бумага") or \
         (user_choice == "бумага" and computer_choice == "камень"):
        print("Ты победил! 🎉")
    else:
        print("Компьютер победил! 🤖")