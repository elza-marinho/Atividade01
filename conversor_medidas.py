user_opcao = int(input("Conversor de medidas. Digite o número da opção desejada:\n1. Quilômetros e Milhas.\n2. Quilos e Libras\nOpção escolhida foi (número apenas): "))

# Caso usuário escolha conversão entre km/milhas

if user_opcao == 1:
    print("\nVocê escolheu conversão entre quilômetros e milhas.")
    print("1. Quilômetros → Milhas")
    print("2. Milhas → Quilômetros")
    km_milhas = int(input("\nQual opção desejada?\n1. Quilômetros para milhas.\n2. Milhas para quilômetros.\nOpção desejada (número apenas): "))

    if km_milhas == 1:
        km = float(input("Número de quilômetros: "))
        print(f"{km} km é/são {km * 0.6213712:.2f} milhas.")

    elif km_milhas == 2:
        milhas = float(input("Número de milhas: "))
        print(f"{milhas} milhas é/são {milhas / 0.6213712:.2f} km.")

    else:
        print("Opção inválida de conversão para quilômetros e milhas.")
# Caso usuário escolha conversão entre quilos/libras

elif user_opcao == 2:
    print("\nVocê escolheu conversão entre quilos e libras.")
    print("1. Quilos → Libras")
    print("2. Libras → Quilos")
    kg_libras = int(input("\nDigite a opção desejada: "))

    kg = float(input("Número de quilos: "))
   
    kg_libras = int(input("Qual opção desejada?\n1. Quilos para Libras.\n2. Libras para quilos.\nOpção desejada (número apenas): "))

    if kg_libras == 1:
        print(f"{kg} kg convertidos para libras são {kg * 2.20462262:.2f} libras.")

    elif kg_libras == 2:
       print(f"{kg} kg convertidos para kilos são {kg * 2.20462262:.2f} kilos.")

else:
    print("Favor entrar um número válido.")