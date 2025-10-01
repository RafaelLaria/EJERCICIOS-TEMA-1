def voltear_texto(texto):
    return texto[::-1]
def limpiar_texto(texto):
    return "".join(c for c in texto if c.isalpha() or c.isspace())
texto = input("Escribe el texto a decodificar: ")
texto_volteado = voltear_texto(texto)
texto_decodificado = limpiar_texto(texto_volteado)

print("Texto original=>", texto)
print("Texto invertido=>", texto_volteado)
print("Texto decodificado=>", texto_decodificado)