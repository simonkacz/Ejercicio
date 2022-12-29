def calcularIMC(peso, alturaEnMetros):
    Imc = peso / (alturaEnMetros*alturaEnMetros)
    return Imc

def pedirElIMC():
    peso = float(input("Ingrese su peso en kg: "))
    alturaEnCM = int(input("Ingrese su altura en cm: "))
    alturaEnMetros = alturaEnCM / 100 #Pasa la altura a metros(en este caso)!!!!

    Imc = calcularIMC(peso, alturaEnMetros)


    print("Su IMC es de " + str(Imc))

    if Imc < 20:
        print("Estado de delgadez")
    if Imc >= 20 and Imc < 26:
        print("Peso normal")
    if Imc >= 26 and Imc < 30:
        print("Estado de sobrepeso")
    if Imc > 30:
        print("Estado de obesidad")

print("Calcular el IMC de la persona")
pedirElIMC()