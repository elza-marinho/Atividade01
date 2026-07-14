id_venda = int(input("Digite o ID da venda: "))
data_venda = input("Digite a data da venda (dd/mm/aaaa): ")
vendedor = input("Digite o nome do vendedor: ")
cliente = input("Digite o nome do cliente: ")
produto = input("Digite o nome do produto: ")
categoria = input("Digite a categoria do produto: ")
quantidade = int(input("Digite a quantidade vendida: "))
if quantidade >100:
    print("Quantidade inválida. Não há esta quantidade de estoque.")
    quantidade = int(input("Digite a quantidade vendida: "))
preco_unitario = float(input("Digite o preço  unitário do produto: "))

valor_total = preco_unitario * quantidade

pagamento = input("Digite a forma de pagamento (1 para à vista ou 2 para a prazo): ")

valor_final = valor_total  

if pagamento == "1":
    desconto = valor_total * 0.05
    valor_final = valor_total - desconto
    forma_pagamento = "À vista"
    print("Desconto de 5%. Valor com desconto: R$ ", valor_final)
elif pagamento == "2":
    acrescimo = valor_total * 0.05
    valor_final = valor_total + acrescimo
    forma_pagamento = "A prazo"
    print("Acréscimo de 5%. Valor com acréscimo: R$ ", valor_final)
else:
    forma_pagamento = "Inválida"
    print("Opção de pagamento inválida.")

print("\nResumo da Venda: ")
print("__________________________________")
print("ID da Venda: ", id_venda)
print("Data: ", data_venda)
print("Vendedor: ", vendedor)
print("Cliente: ", cliente)
print("Produto: ", produto)
print("Categoria: ", categoria)
print("Quantidade: ", quantidade)
print(f"Preço Unitário: R$:  {preco_unitario:.2f}")
print("Forma de Pagamento: ", forma_pagamento)
print(f"Valor Final: R$  {valor_final:.2f}")
