print("hola te sumaré dos números cualesquiera")
primerInput = input("Escribe tu primer número\n")
if(primerInput.isnumeric()):
    segundoInput = input("Escribe tu segundo número\n")
    if(primerInput.isnumeric() and segundoInput.isnumeric()):
        print("La suma es",int(primerInput) + int(segundoInput), " ")
    else:
        print("Solo puedo sumar números jiji")
else:
    ...
segundoInput = input("Escribe tu segundo número\n")
if(primerInput.isnumeric() and segundoInput.isnumeric()):
    print("La suma es",int(primerInput) + int(segundoInput), " ")
else:
    print("Solo puedo sumar números jiji")