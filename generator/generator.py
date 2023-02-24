import os
import random
from data.data import Person, Color, Date
from faker import Faker

faker_ru = Faker('ru_RU')
fake_en = Faker('En')
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_ru.name_nonbinary(),
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        email=faker_ru.email(),
        age=random.randint(18, 80),
        salary=random.randint(50000, 150000),
        department=faker_ru.job(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        mobile=faker_ru.msisdn(),
    )


def generated_file():
    root_dir = os.path.dirname(os.path.dirname(__file__))
    path = rf'{root_dir}\data\filetest_{random.randint(0, 999)}.txt'
    file = open(path, 'w+')
    file.write(f'Hello World {random.randint(0, 999)}')
    file.close()
    file_name = os.path.basename(path)
    return file_name, path


def generated_color():
    yield Color(
        color_name=["Red", "Blue", "Green", "Yellow", "Purple", "Black", "White", "Voilet", "Indigo", "Magenta", "Aqua"]
    )


def generated_date():
    yield Date(
        year=fake_en.year(),
        month=fake_en.month_name(),
        day=fake_en.day_of_month(),
        time="12:00"
    )
