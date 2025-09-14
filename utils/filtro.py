import geopandas as gpd
from fiona import listlayers

caminho = "dados/geoft_bho_ach_otto_nivel_07.gpkg"

# listar camadas disponíveis
print(listlayers(caminho))

# carregar a camada
gdf = gpd.read_file(caminho)
print(gdf.head())


def carregar_arquivo():
    return None