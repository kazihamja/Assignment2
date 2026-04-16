def encrypt(text, s1, s2):
    result = []

    for ch in text:
        if ch.islower():
            pos = ord(ch) - 97

            if pos <= 12:
                new_pos = (pos + (s1 * s2)) % 26
                result.append(chr(new_pos + 97) + "#")
            else:
                new_pos = (pos - (s1 + s2)) % 26
                result.append(chr(new_pos + 97) + "$")

        else:
            result.append(ch)

    return "".join(result)


def decrypt(text, s1, s2):
    result = []
    i = 0

    while i < len(text):
        ch = text[i]

        if ch.islower() and i + 1 < len(text):
            mark = text[i+1]
            pos = ord(ch) - 97

            if mark == "#":
                pos = (pos - (s1 * s2)) % 26
            elif mark == "$":
                pos = (pos + (s1 + s2)) % 26

            result.append(chr(pos + 97))
            i += 2
        else:
            result.append(ch)
            i += 1

    return "".join(result)


# MAIN
s1 = int(input("Enter shift1: "))
s2 = int(input("Enter shift2: "))

with open("raw_text.txt", "r") as f:
    original = f.read()

enc = encrypt(original, s1, s2)

with open("encrypted_text.txt", "w") as f:
    f.write(enc)

dec = decrypt(enc, s1, s2)

with open("decrypted_text.txt", "w") as f:
    f.write(dec)

if original.strip() == dec.strip():
    print("Decryption successful")
else:
    print("Decryption failed")
