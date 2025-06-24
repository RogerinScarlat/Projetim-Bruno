lista_compras=[]
def adicionar_produto():
    try:
        while True:
            nomeprodu = input("Digite o nome do produto: ").strip()
            if nomeprodu:
                nomeprodu = nomeprodu.capitalize()
                break
            else:
                print("❌ O nome do produto não pode estar vazio. Tente novamente.")
        while True:
            categoriaprodu = input("Digite a categoria do produto: ").strip()
            if categoriaprodu:
                categoriaprodu = categoriaprodu.capitalize()
                break
            else:
                print("❌ A categoria não pode estar vazia. Tente novamente.")
        quantiprodu=int(input("Digite a quantidade: "))
        produto={"nome":nomeprodu,"categoria":categoriaprodu,"quantidade":quantiprodu,"status":False}
        lista_compras.append(produto)
        print("Produto adicionado.\n")
    except ValueError:
        print("Entrada invalida❌. Digite um numero para a quantidade.\n")


def mostrar_lista():
    if len(lista_compras)==0:
        print('😭Nenhum Produto Cadastrado😭\n')
        return
    numero=1
    status = ""
    for x in lista_compras:
        if x["status"]==True:
            status="Comprado!"
        else:
            status="Não comprado!"
        print(f"[{[numero]}] nome: {x['nome']} | categoria: {x['categoria']} | "
              f"quantidade:{x['quantidade']} | Status: {status}")
        numero += 1
    print()


def busca_categoria():
    if len(lista_compras)==0:
        print('😭Nenhum produto Cadastrado😭\n')
        return
    produtos_encontrados=[]
    pergun_categoria=str(input("Digite qual categori deseja buscar: ")).capitalize()
    for produto in lista_compras:
            if "categoria" in produto and produto["categoria"] == pergun_categoria:
                produtos_encontrados.append(produto)
    if len(produtos_encontrados)==0:
        print("Nenhum produto com está categoria foi encontrado!\n")
    numero = 1
    status = ""
    for x in produtos_encontrados:
        if x["status"] == True:
            status = "Comprado!"
        else:
            status = "Não comprado!"
        print(f"[{[numero]}] nome: {x['nome']} | categoria: {x['categoria']} | "
              f"quantidade:{x['quantidade']} | Status: {status}")
        numero += 1
    print()


def marcar_comprado():
    mostrar_lista()
    if len(lista_compras)==0:
        print("😭Nenhum produto Cadastrado😭\n")
        return
    try:
        numero = int(input("Digite o numero da produto para marcar como realizado: "))
        indice = numero - 1
        if numero <= len(lista_compras):
            lista_compras[indice]["status"] = True
            print("O status do produto foi mundado com sucesso!✔\n")
        else:
            print("Numero invalido❌. Digite um numero da lista mostrada\n")
    except ValueError:
        print("Entrada invalida❌. Digite um numero da lista mostrada\n")


def menu_escolha():
    while True:
        print(f"Escolha uma das opções a baixo:\n1-para adicionar um produto\n2-para ver lista completa dos produtos\n3-para buscar pela categoria\n4-para marcar o o produto como comprado\n0-para sair")
        pergun=str(input(": "))
        if pergun=="0":
            print("Saindo do programa. Até mais.\n")
            break
        elif pergun=="1":
            adicionar_produto()
        elif pergun=="2":
            mostrar_lista()
        elif pergun=="3":
            busca_categoria()
        elif pergun=="4":
            marcar_comprado()
        else:
            print("entrada invalida❌. Digite um numero valido.\n")

print("Bem vindo a Lista de compras!\n")
menu_escolha()