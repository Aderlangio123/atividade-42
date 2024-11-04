# Faça um programa que leia um número
# indeterminado de notas. Após esta entrada de
# dados, faça o seguinte:
# • Mostre a quantidade de notas que foram lidas.
# • Exiba todas as notas na ordem em que foram
# informadas.
# • Exiba todas as notas na ordem inversa à que
# foram informadas, uma abaixo do outra.
# • Calcule e mostre a soma das notas.
# • Calcule e mostre a média das notas.
# • Calcule e mostre a quantidade de notas acima
# da média calculada.

notas = []
while True:
    nota = float(input("digite as notas (-1 para parar):  "))
    if nota == -1:
        break
    notas.append(nota)

print(" ")
print("a quantidade de notas lidas foram: ",len(notas))
print(" ")
print("as notas digitadas são:", notas)
print(" ")
notas.reverse()
print("as notas de modo invertido é: ",notas) 
print(" ")
print("a soma das notas digitadas é", sum(notas))
print(" ")
med = sum(notas) / len(notas)
print("a média das notas é", med )
print(" ")
acima_media = []
for n in notas:
    if n > med:
        acima_media.append(n)    
print("as notas acima da media das notas é", acima_media)