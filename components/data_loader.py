# components/data_loader.py

import geopandas as gpd

# Ajuste aqui para o caminho completo do seu arquivo .gpkg, 
# mas mantendo-o em data/ para não precisar mudar mais tarde.
GPKG_PATH = r"C:\Users\iatag\OneDrive\Área de Trabalho\Dados Amazonia\prodes_amazonia_legal.gpkg"
LAYER_NAME = "yearly_deforestation"

def load_deforestation_gdf():
    """
    Lê o GeoPackage do PRODES e retorna o GeoDataFrame da camada 'yearly_deforestation'.
    """
    gdf = gpd.read_file(GPKG_PATH, layer=LAYER_NAME)
    # Convertemos 'year' para inteiro (caso venha float) e 'area_km' para float.
    gdf["year"] = gdf["year"].astype(int)
    gdf["area_km"] = gdf["area_km"].astype(float)
    return gdf