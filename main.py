
import geopandas as gpd
from fiona import listlayers
from utils.extract import convert_kml

areabacia = "dados/area.json"
metadados = "dados/geoft_bho_ach_otto_nivel_07.gpkg"
gdf = gpd.read_file(metadados)

# Conversor KML para CSV

input_path = "AreaDelimitada.kml"

output_path = "dados/pontos_sirgas2000.csv"

convert_kml(input_path, output_path, output_format="csv")