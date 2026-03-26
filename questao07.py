n1=float(input("Escreva 4 números reais."))
n2=float(input())
n3=float(input())
n4=float(input())
s=n1+n2+n3+n4
m=s/4
menor=min(n1,n2,n3,n4)
maior=max(n1,n2,n3,n4)
diff=maior-menor
print(f"A média aritmética é: {m}\nA diferença entre o maior e o menor valor é: {diff}")