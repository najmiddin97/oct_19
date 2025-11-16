from faker import Faker

fake = Faker(locale='ru_RU')
print(fake.sentence(nb_words=6))
