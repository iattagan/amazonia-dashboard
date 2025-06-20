# components/layout.py

from dash import html, dcc
import dash_bootstrap_components as dbc
from components.choropleth_map import get_choropleth_figure

def serve_layout(app, anos_disponiveis, estados_disponiveis):
    """
    Layout da aplicação, recebendo listas de anos e estados para popular controles.
    """
    return dbc.Container([
        html.H1("Amazônia em Alerta", className="text-center my-4"),
        
        dcc.Tabs([
            # ─────────────── Aba 1: Visão Geral ───────────────
            dcc.Tab(label="Visão Geral", children=[
                # Fila de filtros: Estado + Intervalo de Anos
                dbc.Row([
                    dbc.Col([
                        html.Label("Estado:"),
                        dcc.Dropdown(
                            id="dropdown-estado",
                            options=[{"label": s, "value": s} for s in estados_disponiveis],
                            value="Todos",
                            clearable=False
                        )
                    ], width=4),
                    dbc.Col([
                        html.Label("Intervalo de anos:"),
                        dcc.RangeSlider(
                            id="slider-anos",
                            min=min(anos_disponiveis),
                            max=max(anos_disponiveis),
                            value=[min(anos_disponiveis), max(anos_disponiveis)],
                            marks={ano: str(ano) for ano in anos_disponiveis},
                            step=1,
                            allowCross=False
                        )
                    ], width=8),
                ], className="mb-4"),
                
                # Cards de KPI (inicialmente vazios)
                dbc.Row(id="kpi-cards", className="mb-4"),
                
                # Gráficos
                dbc.Row([
                    dbc.Col(dcc.Graph(id="bar-graph"), width=6),
                    dbc.Col(dcc.Graph(id="line-graph"), width=6)
                ])
            ]),
            
            # ─────────────── Aba 2: Mapa Interativo ───────────────
            dcc.Tab(label="Mapa Interativo", children=[
                html.Br(),
                html.H4("Mapa de Desmatamento na Amazônia Legal (2023)"),
                dcc.Graph(figure=get_choropleth_figure())
            ]),

            # ─────────────── Aba 3: Sobre o Projeto ───────────────
            dcc.Tab(label="Sobre o Projeto", children=[
                dcc.Store(id="store-section-index", data=0),
                html.Div(id="conteudo-sobre-projeto"),
                dbc.Button("Anterior", id="botao-anterior", color="secondary", className="me-2", n_clicks=0),
                dbc.Button("Próximo", id="botao-proximo", color="primary", n_clicks=0),
            ]),
        ])
    ], fluid=True)
