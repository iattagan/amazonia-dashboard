# components/choropleth_map.py

import geopandas as gpd
import plotly.express as px

def get_choropleth_figure():
    # Caminho para o arquivo GPKG
    caminho_gpkg = r"C:\Users\iatag\OneDrive\Área de Trabalho\Dados Amazonia\prodes_amazonia_legal.gpkg"

    # Carrega a camada desejada
    gdf = gpd.read_file(caminho_gpkg, layer="yearly_deforestation")  # use a camada certa que você viu no teste.py

    # Agrupa por estado e soma o desmatamento (área em km²)
    df_agrupado = gdf.groupby("state", as_index=False)["area_km"].sum()
    df_agrupado.rename(columns={"state": "Estado", "area_km": "Desmatamento_km2"}, inplace=True)

    # Filtra apenas os estados da Amazônia Legal
    estados_amazonia_legal = ['AC', 'AM', 'AP', 'MA', 'MT', 'PA', 'RO', 'RR', 'TO']
    df_agrupado = df_agrupado[df_agrupado["Estado"].isin(estados_amazonia_legal)]

    # GeoJSON com os contornos dos estados
    geojson_url = 'https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson'

    # Cria o mapa
    fig = px.choropleth(
        df_agrupado,
        geojson=geojson_url,
        locations='Estado',
        locationmode='geojson-id',
        color='Desmatamento_km2',
        color_continuous_scale='YlOrRd',
        featureidkey="properties.sigla",
        scope="south america",
        labels={'Desmatamento_km2': 'Área (km²)'},
        title='Desmatamento na Amazônia Legal (2023)'
    )

    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r":0,"t":50,"l":0,"b":0},
                      height=800)
    return fig
