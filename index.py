def cifrar_cesar(texto, desplazamiento):
    resultado = ""

    for letra in texto:
        if letra.isalpha():
            if letra.isupper():
                nueva = chr((ord(letra) - 65 + desplazamiento) % 26 + 65)
            else:
                nueva = chr((ord(letra) - 97 + desplazamiento) % 26 + 97)
            resultado += nueva
        else:
            resultado += letra

    return resultado


def descifrar_fuerza_bruta(texto):
    print("\n=== POSIBLES DESCIFRADOS ===\n")

    for i in range(1, 26):
        intento = cifrar_cesar(texto, -i)
        print(f"Giro {i}: {intento}")


# 🔥 PROGRAMA PRINCIPAL
print("=== DESCIFRADOR CÉSAR 🔓 ===")

texto = input("Escribe el texto cifrado: ")

descifrar_fuerza_bruta(texto)