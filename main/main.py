import random
import string


def is_valid_input(value):
    try:
        length = int(value)
        if 8 <= length <= 64:
            return True
    except ValueError:
        pass
    return False


def generate_strong_password(length=12):
    all_chars = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase + string.ascii_lowercase
    return ''.join(random.choices(all_chars, k=length))


def main():
    while True:
        length = input("Введите необходимую длину пароля (от 8 до 64 символов): ")
        if not is_valid_input(length):
            continue
        break

    strong_password = generate_strong_password(int(length))
    print(f"Сгенерированный пароль: {strong_password}")

if __name__ == "__main__":
    main()
