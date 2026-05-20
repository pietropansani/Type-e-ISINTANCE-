# EX1
# Use a função type() para verificar
# o tipo da variável "ano" com valor 2024.
print("Exercicio 1:")
print("=====================")

ano = 2024
print(type(ano))

# EX2
# Verifique se o número 3.14159
# é do tipo float usando isinstance().
print("Exercicio 2:")
print("=====================")

numero = 3.14159
resultado = isinstance(numero, float)
print(resultado)

# EX3
# Compare se o tipo de 100
# é igual ao tipo de True.
print("Exercicio 3:")
print("=====================")

resultado = type(100) ==type(True)
print(resultado)
print(f"Tipo de 100: {type(100)}")
print(f"Tipo de True: {type(True)}")

# EX4
# Use isinstance() para verificar
# se True pode ser considerado int.
print("Exercicio 4:")
print("=====================")

resultado = isinstance(True, int)

print(resultado)
# EX5
# Verifique se o resultado de 5/2
# é do tipo float usando type() e isinstance().
print("Exercicio 5:")
print("=====================")

resultado_divisao = 5 / 2

eh_float_type = type(resultado_divisao) == float

eh_float_isinstance = isinstance(resultado_divisao, float)

print(f"Resultado da divisão: {resultado_divisao}")
print(f"É float usando type()? {eh_float_type}")
print(f"É float usando isinstance()? {eh_float_isinstance}")

# EX6
# Crie uma função que recebe um valor
# e imprime "É número!" se for int, float ou complex.
print("Exercicio 6:")
print("=====================")

def verificar_se_eh_numero(valor):
    # Passamos uma tupla com os tipos permitidos para o isinstance
    if isinstance(valor, (int, float, complex)):
        print("É número!")
    else:
        print("Não é um número suportado.")

# --- Testando a função ---
verificar_se_eh_numero(10)
verificar_se_eh_numero(3.14)        
verificar_se_eh_numero(2 + 3j)      
verificar_se_eh_numero("Texto")     
    

# EX7
# Compare type() e isinstance()
# para verificar se um booleano
# é considerado inteiro.

print("Exercicio 7:")
print("=====================")

valor = True

resultado_type = type(valor) == int
resultado_isinstance = isinstance(True, int)

print("Resultado com type():", resultado_type)
print("Resultado com isinstance():", resultado_isinstance)

# EX8
# Descubra o tipo do número 3+4j
# usando type().
print("Exercicio 8:")
print("=====================")

valor = 3 + 4j
print(type(valor))

# EX9
# Verifique se o valor None
# é do tipo NoneType usando isinstance().
print("Exercicio 9:")
print("=====================")

valor = None
resultado_isinstance = isinstance(valor, type(None))
print(resultado_isinstance)

# EX10
# Verifique se o número 3.0
# é int, float ou complex usando isinstance()
# e depois teste especificamente se é int.

print("Exercicio 10:")
print("=====================")

valor = 3.0

if isinstance(valor, (int, float, complex)):
    print(f"O valor {valor} é um número válido (int, float ou complex).")

if isinstance(valor, int):
    print("É um número inteiro!")
else:
    print("Não é um número inteiro!")