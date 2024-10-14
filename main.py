import pickle

# Базовый класс Animal
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        return "Животное издает звук"

    def eat(self):
        return f"{self.name} ест."


# Подкласс Bird
class Bird(Animal):
    def __init__(self, name, age, can_fly=True):
        super().__init__(name, age)
        self.can_fly = can_fly

    def make_sound(self):
        return f"{self.name} чирикает."


# Подкласс Mammal
class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        return f"{self.name} рычит."


# Подкласс Reptile
class Reptile(Animal):
    def __init__(self, name, age, is_poisonous):
        super().__init__(name, age)
        self.is_poisonous = is_poisonous

    def make_sound(self):
        return f"{self.name} шипит."


# Функция, демонстрирующая полиморфизм
def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())


# Класс для сотрудников
class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}")


class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}")


# Класс Zoo (композиция)
class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Добавлено животное: {animal.name}")

    def add_staff(self, staff):
        self.staff.append(staff)
        print(f"Добавлен сотрудник: {staff.name}")

    def display_animals(self):
        print("\nЖивотные в зоопарке:")
        for animal in self.animals:
            print(f"{animal.name}, Возраст: {animal.age}")

    def display_staff(self):
        print("\nСотрудники зоопарка:")
        for staff in self.staff:
            print(staff.name)

    # Метод для сохранения состояния зоопарка в файл
    def save_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)
        print(f"Информация о зоопарке сохранена в файл: {filename}")

    # Статический метод для загрузки состояния зоопарка из файла
    @staticmethod
    def load_from_file(filename):
        try:
            with open(filename, 'rb') as file:
                zoo = pickle.load(file)
                print(f"Информация о зоопарке загружена из файла: {filename}")
                return zoo
        except FileNotFoundError:
            print(f"Файл {filename} не найден.")
            return None


# Пример использования программы
if __name__ == "__main__":
    # Создание зоопарка
    zoo = Zoo()

    # Создание животных
    bird = Bird("Попугай", 3, can_fly=True)
    mammal = Mammal("Лев", 5, fur_color="Золотой")
    reptile = Reptile("Змея", 2, is_poisonous=True)

    # Добавление животных в зоопарк
    zoo.add_animal(bird)
    zoo.add_animal(mammal)
    zoo.add_animal(reptile)

    # Создание сотрудников
    keeper = ZooKeeper("Алексей")
    vet = Veterinarian("Марина")

    # Добавление сотрудников в зоопарк
    zoo.add_staff(keeper)
    zoo.add_staff(vet)

    # Демонстрация полиморфизма
    print("\nЗвуки животных:")
    animal_sound(zoo.animals)

    # Сотрудники выполняют свои обязанности
    keeper.feed_animal(mammal)
    vet.heal_animal(reptile)

    # Сохранение информации о зоопарке в файл
    zoo.save_to_file("zoo_data.pkl")

    # Загрузка информации о зоопарке из файла
    loaded_zoo = Zoo.load_from_file("zoo_data.pkl")

    # Отображение загруженной информации
    if loaded_zoo:
        loaded_zoo.display_animals()
        loaded_zoo.display_staff()
