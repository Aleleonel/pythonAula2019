produtos = {'Pera': 3.00, 'Uva': 5.00, 'Maça': 8.00, 'kiwi': 6.00}
lprodutos = list(produtos.keys())
lprodutos.sort()

#for key in lprodutos:
#    print(key, '=', produtos[key])

for key in sorted(produtos):
    print(key, '=', produtos[key])

total = []
soma = []
totalize = 1
totalgeral = 0
lista = [50, 20, 10, 5, 2, 1, 0.50, 0.25]
while True:
    while totalize == 1:
        item = float(input('digite o valor do item:\n'))
        total.append(item)
        totalize = int(input('Deseja finalizar o pedido? [0] para Sim e [1] para Não:\n'))
        if totalize == 0:

            totalgeral = sum(total)
            print("Valor Total da Compra:", totalgeral)
            recebimento = float(input('Digite o valor recebido:\n'))
            troco = recebimento - totalgeral

            for t in range(len(lista)):
                if troco <= troco:
                    cinquenta = troco//50
                    resto = troco % 50
                    vinte = resto//20
                    resto1 = resto % 20
                    dez = resto1 // 10
                    resto2 = resto1 % 10
                    cinco = resto2 // 5
                    resto3 = resto2 % 5
                    dois = resto3 // 2
                    resto4 = resto3 % 2
                    um = resto4 // 1
                    resto5 = resto4 % 1
                    vintecincoCentavos = resto5 // 0.25



            print(cinquenta, 'Notas de 50 Reais')
            print(vinte, 'Notas de 20 Reais')
            print(dez, 'Notas de 10 Reais')
            print(cinco, 'Notas de 5 Reais')
            print(dois, 'Notas de 2 Reais')
            print(um, 'Notas de 1 Real')
            print(vintecincoCentavos, 'Moeda de 0.50 Centavos')



