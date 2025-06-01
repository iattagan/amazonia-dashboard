# components/callbacks.py

from dash import Output, Input, State
import dash_bootstrap_components as dbc
from dash import html

from components.data_loader import load_deforestation_gdf
from components.vizualizations import (
    create_kpi_cards,
    create_bar_chart,
    create_line_chart,
    create_choropleth_map
)

# Carrega o GeoDataFrame globalmente, para não ler várias vezes.
GDF = load_deforestation_gdf()

def register_callbacks(app):
    # ─── Callback: Atualiza KPIs, gráfico de barras e linha (Visão Geral) ───
    @app.callback(
        Output("kpi-cards", "children"),
        Output("bar-graph", "figure"),
        Output("line-graph", "figure"),
        Input("dropdown-estado", "value"),
        Input("slider-anos", "value"),
    )
    def update_visao_geral(estado_selecionado, anos_intervalo):
        ano_min, ano_max = anos_intervalo
        
        # 1. KPIs
        kpis = create_kpi_cards(GDF, ano_min, ano_max)
        cards = []
        for kpi in kpis:
            card = dbc.Col(
                dbc.Card([
                    dbc.CardBody([
                        html.H6(kpi["title"], className="card-title"),
                        html.H3(kpi["value"], className="card-text")
                    ])
                ], className="mb-2"),
                width=4
            )
            cards.append(card)
        
        # 2. Gráfico de barras
        bar_fig = create_bar_chart(GDF, estado_selecionado, ano_min, ano_max)
        
        # 3. Gráfico de linha
        line_fig = create_line_chart(GDF, estado_selecionado)
        
        return cards, bar_fig, line_fig

    # ─── Callback: Atualiza Mapa (Mapa Interativo) ───
    @app.callback(
        Output("mapa-desmatamento", "figure"),
        Input("slider-mapa-ano", "value")
    )
    def update_mapa(ano_selecionado):
        map_fig = create_choropleth_map(GDF, ano_selecionado)
        return map_fig
