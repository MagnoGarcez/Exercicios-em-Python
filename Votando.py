# Em uma eleição os votos são informados pelos seguintes códigos:

# 1, 2, 3, 4  - Votos para os respectivos candidatos 
# 5 - Voto Nulo
# 6 - Voto em Branco

# Faça um programa que calcule e mostre:
# >> O total de votos para cada candidato;
# >> O total de votos nulos;
# >> O total de votos em branco;
# >> A porcentagem de votos nulos sobre o total de votos;
# >> A porcentagem de votos em branco sobre o total de votos. 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import getpass

votos_validos = ['1', '2', '3', '4', '5', '6']
candidatos = ['Celio Moro', 'Ciro Pontes', 'Jair Santana',
 'Lula dos Santos', 'Nulo', 'Branco']
todos_votos = []

print("\n\n\n# Bem vindo a votacao 2022 #\n# Seu voto sera mantido em oculto ! #")
print("\tCandidatos\n1 - Celio Moro\n2 - Ciro Pontes\n3 - Jair Santana\n",
"\r4 - Lula dos Santos\n5 - Nulo\n6 - Branco")
print("# # # # # # # # # # # # #")

voto = '1'
contador_votos = 1
while voto != '0':
    print("* Voto de numero", contador_votos)
    voto = getpass.getpass("Digite a sua opcao: ")
    print("(secreto) *\n - - - - -")
    if voto == '0':
        break
    else:
        while voto not in votos_validos:
            print("<Digite um codigo entre 1 e 6 !>")
            voto = getpass.getpass("Qual candidato menos desagradavel ? : ")
            print("(secreto) *\n - - - - -")        
        todos_votos.append(int(voto))
    contador_votos += 1

candidato_index = 0
print(" - - - - - - - - - - - -")
for i in range(len(candidatos)):
    print("Votos para", candidatos[candidato_index], end=": ")
    if todos_votos.count == 0:
       candidato_index += 1
    else:
        print(todos_votos.count(candidato_index + 1))
        candidato_index += 1
porcent_nulo = (todos_votos.count(5) / len(todos_votos)) * 100
porcent_branco = (todos_votos.count(6) / len(todos_votos)) * 100
print("\nRazao de votos nulos : ", round(porcent_nulo, 2), end="%")
print("\nRazao de votos brancos : ", round(porcent_branco, 2), end="%")
print("\n")

with open("resultado_vota.txt","w") as resultados:
    candidato_index = 0
    resultados.write("\tResultados da eleicao\n\n")
    for i in range(len(candidatos)):
        resultados.write("Votos para " + str(candidatos[candidato_index]) + ": ")
        if todos_votos.count == 0:
            candidato_index += 1
        else:
            resultados.write(str(todos_votos.count(candidato_index + 1)) + "\n")
            candidato_index += 1
            porcent_nulo = (todos_votos.count(5) / len(todos_votos)) * 100
            porcent_branco = (todos_votos.count(6) / len(todos_votos)) * 100
    resultados.write("\nRazao de votos nulos : " + str(round(porcent_nulo, 2)) +"%")
    resultados.write("\nRazao de votos brancos : " + str(round(porcent_branco, 2)) +"%")
    