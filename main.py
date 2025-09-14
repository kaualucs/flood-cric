
import geopandas as gpd
from fiona import listlayers

areabacia = "dados/area.json"
metadados = "dados/geoft_bho_ach_otto_nivel_07.gpkg"
gdf = gpd.read_file(caminho)