# components/layout.py

from dash import html, dcc
import dash_bootstrap_components as dbc

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
                html.Label("Ano:"),
                dcc.Slider(
                    id="slider-mapa-ano",
                    min=min(anos_disponiveis),
                    max=max(anos_disponiveis),
                    value=max(anos_disponiveis),
                    marks={ano: str(ano) for ano in anos_disponiveis},
                    step=1
                ),
                html.Br(),
                dcc.Graph(id="mapa-desmatamento")
            ]),
            
            # ─────────────── Aba 3: Sobre o Projeto ───────────────
            dcc.Tab(label="Sobre o Projeto", children=[
                html.Div([
                    html.H4("Contextualização"),
                    html.P("O desmatamento na Amazônia é uma das maiores ameaças ambientais do século XXI, "
                           "afetando biodiversidade, clima e populações locais. O PRODES, mantido pelo INPE, "
                           "fornece dados anuais de desmatamento que permitem monitorar essas mudanças."),
                    
                    html.H4("Descrição do Problema"),
                    html.Ul([
                        html.Li("Exibir desmatamento anual por estado e por ano."),
                        html.Li("Permitir ao usuário filtrar por intervalo de anos e por estado."),
                        html.Li("Fornecer visualizações interativas (gráficos de barras, linhas e mapa)."),
                        html.Li("Apresentar storytelling dentro da própria aplicação."),
                    ]),
                    
                    html.H4("Proposta de Solução/Implementação"),
                    html.P("A aplicação utiliza Python 3.x e a biblioteca Dash para construir um dashboard responsivo. "
                           "Os dados do PRODES (terreno vetorial em GeoPackage) são carregados via GeoPandas. "
                           "As visualizações usam Plotly Express. A estrutura contempla:\n"
                           "- Módulo de leitura de dados (`data_loader.py`).\n"
                           "- Funções de geração de figuras (`visualizations.py`).\n"
                           "- Layout configurável com filtros e abas (`layout.py`).\n"
                           "- Callbacks para interagir dinamicamente (`callbacks.py`)."),
                    
                    html.H4("Dificuldades e Limitações"),
                    html.P("O principal desafio foi ajustar a camada correta do GeoPackage e agregar dados "
                           "por estado e por ano sem comprometer a performance. Houve cuidado em usar "
                           "`dissolve` para criar o choropleth de maneira eficiente. Limitações incluem "
                           "a ausência de dados diários (apenas anuais) e o tamanho do GeoPackage que "
                           "pode exigir mais memória em máquinas mais antigas."),
                    
                    html.H4("Conclusão"),
                    html.P("Este dashboard atinge a categoria Avançado, pois agrega:\n"
                           "- Três visualizações interativas (barras, linhas e mapa),\n"
                           "- Filtros dinâmicos para intervalo de anos e estado,\n"
                           "- Análise comparativa e storytelling embutido,\n"
                           "- Design cuidado (tipografia simples, cores intuítivas e layout responsivo)."),
                ], className="p-4")
            ])
        ])
    ], fluid=True)
