def create_matrix(key):
    matrix = []
    key = ''.join(sorted(set(key), key=lambda x: key.index(x)))
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    for char in key:
        if char not in matrix:
            matrix.append(char)
            
    for char in alphabet:
        if char not in matrix:
            matrix.append(char)
            
    return [matrix[i:i + 5] for i in range(0, len(matrix), 5)]

def table_encrypt(text, key):
    matrix = create_matrix(key)
    encrypted_text = []
    
    for char in text.upper():
        if char.isalpha():
            for i, row in enumerate(matrix):
                if char in row:
                    row_index = i
                    col_index = row.index(char)
                    encrypted_text.append(matrix[(row_index + 1) % 5][col_index])
                    break
        else:
            encrypted_text.append(char)
            
    return ''.join(encrypted_text)

def table_decrypt(encrypted_text, key):
    matrix = create_matrix(key)
    decrypted_text = []
    
    for char in encrypted_text:
        if char.isalpha():
            for i, row in enumerate(matrix):
                if char in row:
                    row_index = i
                    col_index = row.index(char)
                    decrypted_text.append(matrix[(row_index - 1) % 5][col_index])
                    break
        else:
            decrypted_text.append(char)
            
    return ''.join(decrypted_text)

# Використання:
text = "The artist is the creator of beautiful things. To reveal art and conceal the artist is art's aim. The critic is he who can translate into another manner or a new material his impression of beautiful things. The highest, as the lowest, form of criticism is a mode of autobiography. Those who find ugly meanings in beautiful things are corrupt without being charming. This is a fault. Those who find beautiful meanings in beautiful things are the cultivated. For these there is hope. They are the elect to whom beautiful things mean only Beauty. There is no such thing as a moral or an immoral book. Books are well written, or badly written. That is all. The nineteenth-century dislike of realism is the rage of Caliban seeing his own face in a glass. The nineteenth-century dislike of Romanticism is the rage of Caliban not seeing his own face in a glass. The moral life of man forms part of the subject matter of the artist, but the morality of art consists in the perfect use of an imperfect medium. No artist desires to prove anything. Even things that are true can be proved. No artist has ethical sympathies. An ethical sympathy in an artist is an unpardonable mannerism of style. No artist is ever morbid. The artist can express everything. Thought and language are to the artist instruments of an art. Vice and virtue are to the artist materials for an art. From the point of view of form, the type of all the arts is the art of the musician. From the point of view of feeling, the actor's craft is the type. All art is at once surface and symbol. Those who go beneath the surface do so at their peril. Those who read the symbol do so at their peril. It is the spectator, and not life, that art really mirrors. Diversity of opinion about a work of art shows that the work is new, complex, vital. When critics disagree the artist is in accord with himself. We can forgive a man for making a useful thing as long as he does not admire it. The only excuse for making a useless thing is that one admires it intensely. All art is quite useless."
key = "MATRIX"

# Шифрування
encrypted = table_encrypt(text, key)
print(f"Оригінальний текст: {text}")
print(f"Ключ: {key}")
print(f"Зашифрований текст: {encrypted}")

# Дешифрування
decrypted = table_decrypt(encrypted, key)
print(f"Розшифрований текст: {decrypted}")

# Перевірка
print(f"Перевірка успішна: {text.upper() == decrypted}")