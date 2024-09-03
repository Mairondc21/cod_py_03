from etl import ler_csv, filtrar_produtos_nao_entregues, somar_valores_dos_produtos

path_arquivo = "../vendas.csv"

csv_lido = ler_csv(path_arquivo)
produtos_entregue = filtrar_produtos_nao_entregues(csv_lido)
produtos_somados = somar_valores_dos_produtos(produtos_entregue)

print(produtos_somados)