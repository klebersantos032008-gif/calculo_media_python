# Projeto exemplo: calculadora de media do aluno
def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2

print("==== sistema de notas do aluno ===")
n1 = float(input("digite a primeira nota:"))
n2 = float(input("digite a segunda nota:"))
media = calcular_media(n1,n2)
print(f"A media final é: {media:.2f}")
if media >= 7.0:
    print("Status: APROVADO! ")
else:
    print("Status: REPRIOVADO.")


