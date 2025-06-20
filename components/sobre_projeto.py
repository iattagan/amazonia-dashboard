from dash import html
import dash_bootstrap_components as dbc

secoes_projeto = [
    dbc.Card([
        dbc.CardHeader(html.H2("Projeto Visualização de Dados - Desmatamento da Amazônia", className="text-center")),
        dbc.CardBody([
            html.P("Aluno: José Iatagan Andrade Neto", className="text-muted"),
            html.P("Professor: Mauricio Moreira Neto", className="text-muted"),
            html.P("Disciplina: Visualização de Dados", className="text-muted"),
            html.Br(),
            html.P("Este projeto apresenta um painel interativo desenvolvido com Python e Dash, com o objetivo de visualizar dados reais sobre o desmatamento na Floresta Amazônica. Os dados foram obtidos da plataforma TerraBrasilis (INPE).")
        ])
    ], className="mb-4", style={"padding": "20px"}),

    dbc.Card([
        dbc.CardHeader(html.H4("🌍 Por que falar de desmatamento?")),
        dbc.CardBody([
            html.P("A Floresta Amazônica é a maior floresta tropical do mundo e essencial para o equilíbrio climático global."),
            html.Ul([
                html.Li("Cobre cerca de 5,5 milhões de km²"),
                html.Li("Abriga mais de 10% das espécies conhecidas do planeta"),
                html.Li("Influencia o regime de chuvas em todo o continente sul-americano")
            ])
        ])
    ], className="mb-4", style={"padding": "20px"}),

    dbc.Card([
        dbc.CardHeader(html.H4("🌳 Contextualização")),
        dbc.CardBody(html.P("A Amazônia Legal enfrenta níveis alarmantes de desmatamento, afetando a biodiversidade, o clima e comunidades tradicionais. Utilizando dados do PRODES/INPE, o dashboard busca transformar dados técnicos em visualizações acessíveis e interativas."))
    ], className="mb-4", style={"padding": "20px"}),

    dbc.Card([
        dbc.CardHeader(html.H4("🎯 Objetivo")),
        dbc.CardBody(html.P("Criar uma aplicação web interativa para visualizar e analisar o desmatamento por estado e ano, promovendo consciência ambiental e subsidiando pesquisas."))
    ], className="mb-4", style={"padding": "20px"}),

    dbc.Card([
        dbc.CardHeader(html.H4("💡 Solução Proposta")),
        dbc.CardBody([
            html.P("A aplicação foi desenvolvida com Python, Dash e Plotly, utilizando dados geoespaciais (GeoPackage). Destaques:"),
            html.Ul([
                html.Li("Gráficos interativos de barras e linhas com filtros por estado e ano."),
                html.Li("Mapa coroplético atualizado automaticamente."),
                html.Li("Código modular: `layout.py`, `visualizations.py`, `data_loader.py`, `callbacks.py`."),
            ])
        ])
    ], className="mb-4", style={"padding": "20px"}),

    dbc.Card([
        dbc.CardHeader(html.H4("🛠️ Tecnologias Utilizadas")),
        dbc.CardBody(html.P("Python 3.12.4, Dash, Plotly Express, Bootstrap, GeoPandas, Pandas, Git, VS Code."))
    ], className="mb-4", style={"padding": "20px"}),

    dbc.Card([
        dbc.CardHeader(html.H4("⚠️ Desafios e Limitações")),
        dbc.CardBody([
            html.Ul([
                html.Li("Processamento e leitura correta das camadas do GeoPackage."),
                html.Li("Conversão eficiente de dados espaciais para mapas."),
                html.Li("Dados limitados a recortes anuais e arquivos pesados."),
            ])
        ])
    ], className="mb-4", style={"padding": "20px"}),

    dbc.Card([
        dbc.CardHeader(html.H4("✅ Conclusão")),
        dbc.CardBody([
            html.P("Este dashboard atende aos critérios de projeto *Avançado*, pois inclui:"),
            html.Ul([
                html.Li("Visualizações interativas (barras, linhas e mapa)."),
                html.Li("Filtros dinâmicos por estado e ano."),
                html.Li("Análise comparativa com storytelling implícito."),
                html.Li("Design responsivo e acessível."),
            ]),
            html.P("É uma ferramenta robusta para análise ambiental, com potencial de expansão.")
        ])
    ], style={"padding": "20px"})
]
