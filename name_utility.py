# Gera uma string para visualização
def generate_string(order):
    output_string = ""
    for c in order:
        output_string += c + " "
    return output_string

# Retorna uma lista com as letras ordenadas
def get_order(names):
    # Lista vazia onde as letras serão inseridas
    order = []
    # Esse loop passa por cada caractere presente na lista de nomes, lower() é pra não ter caracteres em caps aqui.
    for c in names.upper():
        # Caso o caractere não esteja presente na lista ele será inserido se não for uma new-line ou espaço.
        if c not in order and c not in ['\n', ' ']:
            order.append(c)
    # Retornando a lista
    return order

# Retorna o texto contido no arquivo selecionado
def get_names(filename):
    with open(filename) as f:
        file_content = f.read().rstrip("\n")
        return file_content

# Caso você não rode o programa como um módulo ele só mostrará a lista de letras
# dos nomes em names.txt
if __name__ == "__main__":
    names = get_names("names.txt")
    order = get_order(names)
    print(generate_string(order))