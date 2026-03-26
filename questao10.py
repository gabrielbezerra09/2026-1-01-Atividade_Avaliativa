n1=int(input("Escreva 4 números inteiros."))
n2=int(input())
n3=int(input())
n4=int(input())
s=n1+n2+n3+n4
m=s/4
if m >= 6:
    situação= "Aprovado(a)!"
else:
    situação= "Reprovado(a)."
print(f"A sua média é: {m}.\nSituação: {situação}")