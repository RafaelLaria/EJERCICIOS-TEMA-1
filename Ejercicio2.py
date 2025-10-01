cantidad_inicial = float(input("Escriba la cantidad inicial:"))
cantidad_mensual = float(input("Escriba la cantidad mensual:"))
número_de_meses = int(input("Escriba el número de meses:"))
def salario_por_numerodemeses(mensual, meses):
    return mensual * meses
Ahorros= sum([cantidad_inicial, salario_por_numerodemeses(cantidad_mensual, número_de_meses)])
print("Ahorros totales =>", Ahorros)
if Ahorros >= 5000:
    print("Felicidades por ser tan tacaño!!!")
else:
    pass