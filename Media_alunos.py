# Faça um programa que calcule o número médio de alunos por turma. 
# Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma.
# As turmas não podem ter mais de 40 alunos.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

alunos_por_turma = []
num_da_turma = 1
turmas = int(input("Quantas turmas temos ? : "))

for i in range(turmas):
    print("* Turma", num_da_turma)
    alunos = int(input("Quantos alunos são ? : "))
    while alunos > 40:
        print("* Turma ", num_da_turma, " <Não temos turmas com mais de 40 alunos !>")
        alunos = int(input("Quantos alunos são ? : "))
    num_da_turma += 1
    alunos_por_turma.append(alunos)

media = sum(alunos_por_turma) / len(alunos_por_turma)
print("A media das turmas e de : ", media)