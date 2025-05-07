from faker import Faker

faker = Faker('ru_RU')

def generate_order_form_data():
    name = faker.first_name()
    surname = faker.last_name()
    address = faker.address()
    phone = faker.phone_number()
    return name, surname, address, phone