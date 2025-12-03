# Controle de Estoque Simplificado

estoque = {}

def adicionar_produto():
    nome = input("┈┈➤  Nome do produto: ")
    qtd = int(input("┈┈➤ Quantidade: "))
    preco = float(input("┈┈➤ Preço unitário: "))
    estoque[nome] = {"qtd": qtd, "preco": preco}

def entrada():
    nome = input("┈┈➤ Produto: ")
    if nome in estoque:
        qtd = int(input("┈┈➤ Quantidade a adicionar: "))
        estoque[nome]["qtd"] += qtd
    else:
        print("Produto não encontrado.")

def saida():
    nome = input("┈┈➤ Produto: ")
    if nome in estoque:
        qtd = int(input("┈┈➤ Quantidade a retirar: "))
        if qtd <= estoque[nome]["qtd"]:
            estoque[nome]["qtd"] -= qtd
        else:
            print("Quantidade insuficiente.")
    else:
        print("Produto não encontrado.")

def atualizar_preco():
    nome = input("┈┈➤ Produto: ")
    if nome in estoque:
        preco = float(input("┈┈➤ Novo preço: "))
        estoque[nome]["preco"] = preco
    else:
        print("Produto não encontrado.")

def listar_estoque():
    for nome, dados in estoque.items():
        print(f" {nome} 𝄃𝄃𝄂𝄂𝄀𝄁𝄃𝄂𝄂𝄃\n⤷ {dados['qtd']} unidades\n⤷ R${dados['preco']:.2f} cada")

def valor_total():
    total = sum(d["qtd"] * d["preco"] for d in estoque.values())
    print(f"Valor total do estoque: R${total:.2f}")

def menu():
    opcoes = {
        "1": adicionar_produto,
        "2": entrada,
        "3": saida,
        "4": listar_estoque,
        "5": valor_total,
        "6": atualizar_preco
    }
    while True:
        print("─── ⋆✩ 𝐂𝐨𝐧𝐭𝐫𝐨𝐥𝐞 𝐝𝐞 𝐄𝐬𝐭𝐨𝐪𝐮𝐞 ✩⋆ ──")
        
        print("╰┈➤ 1-Adicionar\n╰┈➤ 2-Entrada\n╰┈➤ 3-Saída\n╰┈➤ 4-Listar\n╰┈➤ 5-Valor Total\n╰┈➤ 6-Atualizar Preço\n╰┈➤ 0-Sair")
        op = input("Opção: ")
        if op == "0": break
        func = opcoes.get(op)
        if func: func()
        else: print("Opção inválida.")

menu()