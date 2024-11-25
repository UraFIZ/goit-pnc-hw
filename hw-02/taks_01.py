def extend_key(text, key):
    """Розширює ключ до довжини тексту"""
    key = list(key)
    if len(text) == len(key):
        return ''.join(key)
    else:
        extended_key = key * (len(text) // len(key)) + key[:len(text) % len(key)]
        return ''.join(extended_key)

def vigenere_encrypt(text, key):
    """Шифрує текст за допомогою шифру Віженера"""
    key = extend_key(text, key)
    cipher_text = []
    
    for i in range(len(text)):
        if text[i].isalpha():
            # Визначаємо зсув на основі символу ключа
            shift = ord(key[i].upper()) - ord('A')
            # Якщо символ у верхньому регістрі
            if text[i].isupper():
                cipher_text.append(chr((ord(text[i]) - ord('A') + shift) % 26 + ord('A')))
            # Якщо символ у нижньому регістрі
            else:
                cipher_text.append(chr((ord(text[i]) - ord('a') + shift) % 26 + ord('a')))
        else:
            cipher_text.append(text[i])
            
    return ''.join(cipher_text)

def vigenere_decrypt(cipher_text, key):
    """Дешифрує текст, зашифрований шифром Віженера"""
    key = extend_key(cipher_text, key)
    plain_text = []
    
    for i in range(len(cipher_text)):
        if cipher_text[i].isalpha():
            # Визначаємо зсув на основі символу ключа
            shift = ord(key[i].upper()) - ord('A')
            # Якщо символ у верхньому регістрі
            if cipher_text[i].isupper():
                plain_text.append(chr((ord(cipher_text[i]) - ord('A') - shift) % 26 + ord('A')))
            # Якщо символ у нижньому регістрі
            else:
                plain_text.append(chr((ord(cipher_text[i]) - ord('a') - shift) % 26 + ord('a')))
        else:
            plain_text.append(cipher_text[i])
            
    return ''.join(plain_text)

def main():
    # Текст з передмови до "Портрет Доріана Грея"
    text = "The artist is the creator of beautiful things. To reveal art and conceal the artist is art's aim."
    key = "CRYPTOGRAPHY"
    
    # Шифруємо текст
    encrypted_text = vigenere_encrypt(text, key)
    print(f"Оригінальний текст: {text}")
    print(f"Ключ шифрування: {key}")
    print(f"Зашифрований текст: {encrypted_text}")
    
    # Дешифруємо текст
    decrypted_text = vigenere_decrypt(encrypted_text, key)
    print(f"Розшифрований текст: {decrypted_text}")
    
    # Перевіряємо, чи співпадає розшифрований текст з оригінальним
    print(f"\nПеревірка успішна: {text == decrypted_text}")

if __name__ == "__main__":
    main()