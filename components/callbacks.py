# components/callbacks.py

from dash import Output, Input, State
import dash_bootstrap_components as dbc
import dash
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

    # ─── Callback: Navegação entre seções da aba "Sobre o Projeto" ───
    @app.callback(
        Output("store-section-index", "data"),
        Output("conteudo-sobre-projeto", "children"),
        Input("botao-anterior", "n_clicks"),
        Input("botao-proximo", "n_clicks"),
        State("store-section-index", "data")
    )
    def navegar_secoes(n_clicks_ant, n_clicks_prox, indice_atual):
        from components.sobre_projeto import secoes_projeto  # importa a lista
        
        if indice_atual is None:
            indice_atual = 0

        # Atualiza o índice com base nos botões clicados
        ctx = dash.callback_context
        if not ctx.triggered:
            return indice_atual, secoes_projeto[indice_atual]
        
        botao_id = ctx.triggered[0]["prop_id"].split(".")[0]

        if botao_id == "botao-proximo":
            novo_indice = min(indice_atual + 1, len(secoes_projeto) - 1)
        elif botao_id == "botao-anterior":
            novo_indice = max(indice_atual - 1, 0)
        else:
            novo_indice = indice_atual

        return novo_indice, secoes_projeto[novo_indice]