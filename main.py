#Задание: Применение Принципа Открытости/Закрытости (Open/Closed Principle) в Разработке Простой Игры
# Цель: Цель этого домашнего задание - закрепить понимание и навыки применения принципа открытости/закрытости (Open/Closed Principle),
# одного из пяти SOLID принципов объектно-ориентированного программирования. Принцип гласит,
# что программные сущности (классы, модули, функции и т.д.) должны быть открыты для расширения, но закрыты для модификации.
# Задача: Разработать простую игру, где игрок может использовать различные типы оружия для борьбы с монстрами.
# Программа должна быть спроектирована таким образом, чтобы легко можно было добавлять новые типы оружия,
# не изменяя существующий код бойцов или механизм боя.

# Исходные данные:
# - Есть класс `Fighter`, представляющий бойца.
## - Есть класс `Monster`, представляющий монстра.
## - Игрок управляет бойцом и может выбирать для него одно из вооружений для боя.
## Шаг 1:Создайте абстрактный класс для оружия
## - Создайте абстрактный класс `Weapon`, который будет содержать абстрактный метод `attack()`.
## Шаг 2: Реализуйте конкретные типы оружия
## - Создайте несколько классов, унаследованных от `Weapon`, например, `Sword` и `Bow`.
# Каждый из этих классов реализует метод `attack()` своим уникальным способом.if __name__ == "__main__":
#
# Создаем бойца и монстра
#     fighter = Fighter("Герой")
#     monster = Monster()
#
#     # Выбираем меч
#     fighter.change_weapon(Sword())
#     battle(fighter, monster)
#
#     # Восстанавливаем здоровье монстра для следующего раунда
#     monster.health = 100
#
#     # Выбираем лук
#     fighter.change_weapon(Bow())
#     battle(fighter, monster)
#
#     # Добавляем новое оружие (дубинку) без изменения существующего кода
#     fighter.change_weapon(Club())
#     battle(fighter, monster)
## Шаг 3: Модифицируйте класс `Fighter`
## - Добавьте в класс `Fighter` поле, которое будет хранить объект класса `Weapon`.
## - Добавьте метод `change_weapon()`, который позволяет изменить оружие бойца.
## Шаг 4: Реализация боя
## - Реализуйте простой механизм для демонстрации боя между бойцом и монстром, исходя из выбранного оружия.
## Требования к заданию:
## - Код должен быть написан на Python.
## - Программа должна демонстрировать применение принципа открытости/закрытости: новые типы оружия можно легко добавлять, не изменяя существующие классы бойцов и механизм боя.
## - Программа должна выводить результат боя в консоль.
## Пример результата:
## Боец выбирает меч.
## Боец наносит удар мечом.
## Монстр побежден!
## Боец выбирает лук.
# Боец наносит удар из лука.
## Монстр побежден!


from abc import ABC, abstractmethod


class Weapon ():
    @abstractmethod
    def attack(self):
        pass


class Fighter():
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon=Weapon):  # метод `change_weapon()`, позволяет изменить оружие бойца
        self.weapon = weapon
        print(f"{self.name} выбрал {weapon.__class__.__name__}.")

    def attack_monster(self, monster):
        if not self.weapon:
            print(f"{self.name} не имеет оружия")

        action = self.weapon.attack()
        print(f"{self.name} атакует")
        monster.take_damage()


class Monster ():
    def __init__(self, health=100):
        self.health = health

    def take_damage(self):
        self.health -= 20
        if self.health <= 0:
            print("Монстр побежден!")
        else:
            print(f"У монстра осталось {self.health} здоровья.")


class Sword(Weapon):
    def attack(self):
        return "наносит удар мечом"

class Bow(Weapon):
    def attack(self):
        return "стреляет из лука"

class Club(Weapon):
    def attack(self):
        return "ударяет дубинкой"


# Реализация боя
def battle(figter, monster):
   while monster.health > 0:
        figter.attack_monster(monster)
        if monster.health <= 0:
            break


# Пример игры

if __name__ == "__main__":
    # Создаем бойца и монстра
    fighter = Fighter("Герой")
    monster = Monster()

    # Выбираем меч
    fighter.change_weapon(Sword())
    battle(fighter, monster)

    # Восстанавливаем здоровье монстра для следующего раунда
    monster.health = 100

    # Выбираем лук
    fighter.change_weapon(Bow())
    battle(fighter, monster)

    # Добавляем новое оружие (дубинку) без изменения существующего кода
    fighter.change_weapon(Club())
    battle(fighter, monster)
