import csv

path_arquivo = "../vendas.csv"

def ler_csv(nome_arquivo_csv: str) -> [dict] :
    lista = []
    with open(nome_arquivo_csv, mode="r", encoding="utf-8") as arquvivo:
        leitor = csv.DictReader(arquvivo)
        for linha in leitor:
           lista.append(linha)
    return lista  

def filtrar_produtos_nao_entregues(lista: list[dict]) -> list[dict] :
    lista_com_produtos_filtrados = []
    for produto in lista:
        if(produto.get("entregue") == "True"):
            lista_com_produtos_filtrados.append(produto)
    return lista_com_produtos_filtrados

def somar_valores_dos_produtos(lista: list[dict]) -> int :
    valor_total = 0
    for produto in lista:
        valor_total += int(produto.get("price"))

    return valor_total



if __name__ == "__main__":

    csv_lido = ler_csv(path_arquivo)
    produtos_entregue = filtrar_produtos_nao_entregues(csv_lido)
    produtos_somados = somar_valores_dos_produtos(produtos_entregue)

    print(produtos_somados)