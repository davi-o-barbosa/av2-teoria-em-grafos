# Módulo para obter a ordem das letras
import name_utility
# Biblioteca para eu não precisar programar a estrutura de árvore binária
from binarytree import Node


# Função que será executada caso o programa seja executado, em vez de usado como módulo
def main():
    # Arquivo de onde os nomes serão lidos
    FILENAME = "names.txt"
    # Lista de nomes
    name_list = name_utility.get_names(FILENAME)

    # Ordem das letras, ou nós da árvore
    nodes = name_utility.get_order(name_list)

    print(f"\nLetras ordenadas:\n{name_utility.generate_string(nodes)}\n")

    # A ordem das letras agora precisa ser convertida para números,
    # já que a biblioteca não aceita letras.

    # Para isso, esse loop vai por todos os index da lista de letras
    # e obtem o valor da letra em inteiro, e após isso se subtrai 64,
    # o que faz a letra ter o valor que tem na ordem do nosso alfabeto.

    # Exemplo: 'A' em inteiro é 65, subtraindo 64 temos 1.
    for i in range(len(nodes)):
        nodes[i] = ord(nodes[i]) - 64

    print("1)------------------------------------------------------")
    print(f'\n"{convert_to_letter(nodes[0])}" será inserido na árvore')
    # Gerando o primeiro nó da árvore, e o removendo da lista
    root = Node(nodes.pop(0))
    print_tree(root)

    # Para cada número da nossa lista, ele será inserido na árvore
    for node in nodes:
        print(f"{nodes.index(node)+2})------------------------------------------------------")
        print(f'\n"{convert_to_letter(node)}" será inserido na árvore')
        root = insert(node, root)
        print_tree(root)


# Inserção básica para uma árvore binária de busca
# Se um valor for maior que o nó que ele está sendo inserido,
# será colocado a direita, se for menor, a esquerda.
# Isso é recursivo, pois você deve procurar uma folha na árvore.
def insert(e, node):
    if not node:
        node = Node(e)
    elif e < node.value:
        node.left = insert(e, node.left)
    elif e > node.value:
        node.right = insert(e, node.right)

    if not node.is_balanced:
        print_tree(node)
        print(f"Nó a ser balanceado: {convert_to_letter(node.value)}")
        node = fix_balance(node)

    return node


# Essa função deve corrigir qualquer erro de balanço na árvore
def fix_balance(node):
    # Pegando a altura para os dois lados do nó
    h_left, h_right = get_heights(node)
    # Calculando o balanço
    balance = h_left-h_right
    # Balanço do nó a ser rotacionado
    print(f"Balanço: {balance}")

    # Aplicando as regras que o professor ensinou para as rotações

    # Balanço > 1
    if h_left > h_right:
        # Calculando os mesmos valores, porém para o nó filho à esquerda
        aux = node.left
        ah_left, ah_right = get_heights(aux)

        # EU NÃO SEI PORQUE, porém, o que o professor ensinou no texto de apoio se aplica aqui, porém não na outra parte

        # Aplicando uma rotação pra direita caso essas condições estejam certas, não vou explicar porque consta no texto de apoio
        # da matéria
        if ah_left > ah_right:
            print("Rotação: Direita")
            node = right_rotate(node)
        # Aplicando uma rotação dupla direita, que é uma rotação pra esquerda no nó filho
        # e uma rotação pra direita no nó raiz
        elif ah_left < ah_right:
            print("Rotação: Dupla direita")
            node.left = left_rotate(node.left)
            node = right_rotate(node)

    # Balanço < -1
    elif h_left < h_right:
        # Calculando os mesmos valores, porém para o nó filho à direita
        aux = node.right
        ah_left, ah_right = get_heights(aux)

        # Por algum motivo isso aqui tá invertido do que o professor ensinou
        # MAS É O CORRETO!!

        # Rotação dupla esquerda consta basicamente como:
        # Uma rotação a direita do nó filho a esquerda
        # Uma rotação a esquerda do nó raiz
        if ah_left > ah_right:
            print("Rotação: Dupla esquerda")
            node.right = right_rotate(node.right)
            node = left_rotate(node)
        # Uma rotação a esquerda
        elif ah_left < ah_right:
            print("Rotação: Esquerda")
            node = left_rotate(node)

    return node


# Função para realizar a rotação para a esquerda
# De acordo com o que o professor fez no texto de apoio
def left_rotate(node):
    aux_node = node.right
    node.right = aux_node.left
    aux_node.left = node
    return aux_node


# Mesma coisa, só que pra uma rotação para a direita
def right_rotate(node):
    aux_node = node.left
    node.left = aux_node.right
    aux_node.right = node
    return aux_node


# Essa função calcula a altura do lado direito e esquerdo de um nó
def get_heights(node):
    # Os valores começam zerados
    h_left, h_right = 0, 0
    # Caso o node a esquerda ou direita exista,
    # o valor é substituído pela altura
    if node.left:
        h_left = node.left.height + 1

    if node.right:
        h_right = node.right.height + 1
    # Caso um lado não tenha um node o valor da altura é mantido como 0
    return h_left, h_right


# Função pra converter um valor para caractere, não sei porque fiz isso.
def convert_to_letter(value):
    return chr(value + 64)


# Essa função converte os valores numéricos da árvore para letras
# (A biblioteca que usei para as árvores binárias não aceita letras, apenas números)
def print_tree(root):
    # Texto que representa a árvore (usando números)
    text = root.__str__()
    # Esse buffer vai armazenar um número, como pode ter mais de um dígito eu pensei nessa solução
    buffer = ''
    # Para cada caractere no texto
    for c in text:
        # Se o caractere for um dígito ele será armazenado no buffer
        if c.isdigit():
            buffer += c
        # Se o caractere não for um dígito, o buffer será convertido para a letra correspondente
        if not c.isdigit() and buffer != '':
            # O tamanho do número é importante pra arrumar o espaço que sobra
            # O número 10 usa dois espaços, porém ele representaria a letra 'J', que só um espaço
            size = len(buffer) - 1
            # Convertendo o número para a letra e adicionando o espaço para corrigir a posição
            # Um caractere de espaço vazio ' ' está sendo multiplicando pelo tamanho do número - 1
            # Então se for 10, em vez de 'J' será 'J '
            letter = chr(int(buffer) + 64) + " " * size
            # Substituindo o número pela letra na string
            text = text.replace(buffer, letter, 1)
            # Zerando o buffer
            buffer = ''

    # Imprimindo a árvore após substituir pelas letras
    print(text)


if __name__ == "__main__":
    main()
