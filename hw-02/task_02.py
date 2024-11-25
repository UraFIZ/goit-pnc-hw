def get_permutation_order(key):
    """
    Створює порядок перестановки на основі ключового слова
    Наприклад, для 'SECRET' порядок буде [3, 1, 0, 2, 4, 5]
    """
    # Створюємо список індексів
    order = list(range(len(key)))
    # Сортуємо індекси на основі символів ключа
    order.sort(key=lambda i: key[i])
    return order

def pad_text(text, block_size):
    """Доповнює текст пробілами до кратності розміру блоку"""
    padding_length = (block_size - (len(text) % block_size)) % block_size
    return text + ' ' * padding_length

def create_matrix(text, key):
    """Створює матрицю для перестановки"""
    width = len(key)
    height = (len(text) + width - 1) // width
    matrix = [[' ' for _ in range(width)] for _ in range(height)]
    
    for i, char in enumerate(text):
        row = i // width
        col = i % width
        matrix[row][col] = char
    
    return matrix

def simple_encrypt(text, key):
    """
    Рівень 1: Шифрування простою перестановкою
    """
    padded_text = pad_text(text, len(key))
    matrix = create_matrix(padded_text, key)
    order = get_permutation_order(key)
    
    result = []
    for row in matrix:
        # Застосовуємо перестановку до кожного рядка
        encrypted_row = ''.join(row[i] for i in order)
        result.append(encrypted_row)
    
    return ''.join(result)

def simple_decrypt(encrypted_text, key):
    """
    Рівень 1: Дешифрування простою перестановкою
    """
    width = len(key)
    height = len(encrypted_text) // width
    order = get_permutation_order(key)
    
    # Створюємо зворотній порядок
    reverse_order = [0] * width
    for i, pos in enumerate(order):
        reverse_order[pos] = i
    
    # Розбиваємо текст на рядки
    rows = [encrypted_text[i:i+width] for i in range(0, len(encrypted_text), width)]
    
    result = []
    for row in rows:
        # Відновлюємо оригінальний порядок символів
        decrypted_row = [''] * width
        for i, char in enumerate(row):
            decrypted_row[reverse_order[i]] = char
        result.append(''.join(decrypted_row))
    
    return ''.join(result).rstrip()

def double_encrypt(text, key1, key2):
    """
    Рівень 2: Шифрування подвійною перестановкою
    """
    # Шифруємо спочатку ключем key1
    temp = simple_encrypt(text, key1)
    # Потім шифруємо результат ключем key2
    return simple_encrypt(temp, key2)

def double_decrypt(encrypted_text, key1, key2):
    """
    Рівень 2: Дешифрування подвійною перестановкою
    """
    # Дешифруємо спочатку ключем key2
    temp = simple_decrypt(encrypted_text, key2)
    # Потім дешифруємо результат ключем key1
    return simple_decrypt(temp, key1)

def main():
    # Тестовий текст
    text = "The artist is the creator of beautiful things"
    print(f"Оригінальний текст: {text}")
    
    # Рівень 1: Проста перестановка
    print("\nРівень 1: Проста перестановка")
    key = "SECRET"
    print(f"Ключ: {key}")
    
    encrypted = simple_encrypt(text, key)
    print(f"Зашифрований текст: {encrypted}")
    
    decrypted = simple_decrypt(encrypted, key)
    print(f"Розшифрований текст: {decrypted}")
    print(f"Перевірка рівня 1: {text == decrypted}")
    
    # Рівень 2: Подвійна перестановка
    print("\nРівень 2: Подвійна перестановка")
    key1 = "SECRET"
    key2 = "CRYPTO"
    print(f"Ключ 1: {key1}")
    print(f"Ключ 2: {key2}")
    
    double_encrypted = double_encrypt(text, key1, key2)
    print(f"Зашифрований текст: {double_encrypted}")
    
    double_decrypted = double_decrypt(double_encrypted, key1, key2)
    print(f"Розшифрований текст: {double_decrypted}")
    print(f"Перевірка рівня 2: {text == double_decrypted}")

# Тестування коду
if __name__ == "__main__":
    main()