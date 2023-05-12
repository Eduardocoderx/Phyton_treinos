N = int(input("Quantos numeros voce vai digitar"))

vet: [float] = [0 for x in range(N)]

for  i in range (0,n):
    # começando do 0 enquanto for menor que "N"
    vet[i] = float(input("Digite um numero: "))
    # Em cada posição vou fazer a leitura do meu vetor 
print()
print("Numeros Digitados: ")
for i in range (0 , N):
    print(f"{vet[i]:.1f}")
    #  {}- a interpolação 
    #:.1f são as casas decimais que ira pular no caso "1"
    #ele vai receber os valores e imprimir na tela 