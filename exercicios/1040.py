n1, n2, n3, n4 = list(map(float, input().split()))

media = (n1*2 + n2*3 + n3*4 + n4*1)/10

print("Media: {0:.1f}".format(media))

if (media >= 7):
    print("Aluno aprovado.")
if (media >= 5 and media <= 6.9):
    print("Aluno em exame.")
    print("Nota do exame: ", end="")
    nota_exame = float(input())
    print(nota_exame)
    rec = (media + nota_exame)/2
    if (rec >= 5):
        print ("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: {0:.1f}".format(rec))
if (media < 5):
    print("Aluno reprovado.")