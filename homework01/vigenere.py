def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    keyword_length = len(keyword)

    # Счетчик для букв ключа
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            # Находим текущую букву ключа и определяем её сдвиг (0 для A, 1 для B и т.д.)
            key_char = keyword[key_index % keyword_length]
            shift = ord(key_char.upper()) - ord("A")

            if char.isupper():
                ciphertext += chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
            elif char.islower():
                ciphertext += chr((ord(char) - ord("a") + shift) % 26 + ord("a"))

            # Переходим к следующей букве ключа только если зашифровали букву
            key_index += 1
        else:
            # Символы вроде пробелов и знаков препинания просто переносятся
            ciphertext += char

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    keyword_length = len(keyword)
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            key_char = keyword[key_index % keyword_length]
            # Сдвиг определяется точно так же, как и при шифровании
            shift = ord(key_char.upper()) - ord("A")

            if char.isupper():
                # При дешифровании вычитаем shift вместо прибавления
                plaintext += chr((ord(char) - ord("A") - shift) % 26 + ord("A"))
            elif char.islower():
                plaintext += chr((ord(char) - ord("a") - shift) % 26 + ord("a"))

            key_index += 1
        else:
            plaintext += char

    return plaintext
