import random

def generate_email():
    email = f"kira_mahotina-{random.randint(100,999)}@yandex.ru"
    return email

def generate_password():
    password = f"{random.randint(100000, 999999)}"
    return password
