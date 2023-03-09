print("hola te sumaré dos números cualesquiera")
primerNumero = input("Escribe tu primer número\n")
segundoNumero = input("Escribe tu segundo número\n")
if(primerNumero.isnumeric() and segundoNumero.isnumeric()):
    print("La suma es",int(primerNumero) + int(segundoNumero), " ")
else:
    print("Solo puedo sumar números jiji")