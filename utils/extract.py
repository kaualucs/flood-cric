import geopandas as gpd

def convert_kml(input_path, output_path, output_format="csv"):
    
    gdf = gpd.read_file(input_path, driver="KML")

    gdf = gdf.to_crs(epsg=4674)

    gdf["latitude"] = gdf.geometry.y
    gdf["longitude"] = gdf.geometry.x

    if output_format == "csv":
        gdf.to_csv(output_path, index=False)
    elif output_format == "gpkg":
        gdf.to_file(output_path, driver="GPKG")
    else:
        raise ValueError("Formato não suportado: use 'csv' ou 'gpkg'")

    print(f"Arquivo convertido salvo em {output_path}")
