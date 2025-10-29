# Cadastro de Produtos
# Peça o nome e preço de 5 produtos usando um laço for.
# Ao final, exiba o nome de todos e a soma total dos preços.

produtos = []
valores = 0.0
for i in range(0, 5):
    produto = input("Digite o nome do produto: ")
    valor = float(input("Digite o valor: $ "))
    produtos.append(produto)
    valores += valor

print(f"\nOs Produtos São:")

for nome in produtos:
    import time
    print(f"-{nome}")
    time.sleep(0.7)
    
print(f"\nA soma total dos valores é {valores}")
