# components/visualizations.py

import plotly.express as px
import pandas as pd

def create_kpi_cards(df, ano_min, ano_max):
    """
    Calcula KPIs básicos: área total no intervalo, maior ano, menor ano.
    Retorna uma lista de dicionários para exibição em cards.
    """
    # Filtrar pelo intervalo de anos
    sub = df[(df["year"] >= ano_min) & (df["year"] <= ano_max)]
    
    total_area = sub["area_km"].sum()
    ano_mais_recente = sub["year"].max()
    area_ano_mais_recente = sub[sub["year"] == ano_mais_recente]["area_km"].sum()
    ano_menos_recente = sub["year"].min()
    area_ano_menos_recente = sub[sub["year"] == ano_menos_recente]["area_km"].sum()

    # KPIs formatados
    return [
        {
            "title": "Área Total (km²)",
            "value": f"{total_area:,.0f}"
        },
        {
            "title": f"Desmatamento em {ano_menos_recente} (km²)",
            "value": f"{area_ano_menos_recente:,.0f}"
        },
        {
            "title": f"Desmatamento em {ano_mais_recente} (km²)",
            "value": f"{area_ano_mais_recente:,.0f}"
        },
    ]


def create_bar_chart(df, estado_selecionado, ano_min, ano_max):
    """
    Gráfico de barras: total de área desmatada por ano ou por estado, conforme filtros.
    Se 'estado_selecionado' for 'Todos', agrega por ano; senão, filtra por estado e agrega por ano.
    """
    # Filtrar pelo intervalo de anos
    sub = df[(df["year"] >= ano_min) & (df["year"] <= ano_max)]
    
    if estado_selecionado != "Todos":
        sub = sub[sub["state"] == estado_selecionado]
        titulo = f"Desmatamento anual em {estado_selecionado}"
    else:
        titulo = "Desmatamento anual na Amazônia Legal"
    
    # Agregar área por ano
    df_agg = sub.groupby("year", as_index=False)["area_km"].sum()
    fig = px.bar(
        df_agg, 
        x="year", 
        y="area_km", 
        labels={"year": "Ano", "area_km": "Área (km²)"},
        title=titulo
    )
    fig.update_layout(margin=dict(l=20, r=20, t=40, b=20))
    return fig


def create_line_chart(df, estado_selecionado):
    """
    Gráfico de linha comparando desmatamento anual de todos os estados ou de um estado específico.
    Se 'Todos', plota cada estado como linha; senão, apenas aquele estado.
    """
    if estado_selecionado == "Todos":
        df_agg = df.groupby(["year", "state"], as_index=False)["area_km"].sum()
        titulo = "Comparativo anual por estado"
        fig = px.line(
            df_agg,
            x="year",
            y="area_km",
            color="state",
            labels={"year": "Ano", "area_km": "Área (km²)", "state": "Estado"},
            title=titulo
        )
    else:
        sub = df[df["state"] == estado_selecionado]
        df_agg = sub.groupby("year", as_index=False)["area_km"].sum()
        titulo = f"Evolução anual em {estado_selecionado}"
        fig = px.line(
            df_agg,
            x="year",
            y="area_km",
            labels={"year": "Ano", "area_km": "Área (km²)"},
            title=titulo
        )

    fig.update_layout(margin=dict(l=20, r=20, t=40, b=20))
    return fig


def create_choropleth_map(df, ano_selecionado):
    """
    Mapa choropleth que colore cada estado pela área desmatada no ano selecionado.
    """
    # Filtrar apenas as geometrias e área do ano selecionado
    sub = df[df["year"] == ano_selecionado]
    df_agg = sub.dissolve(by="state", aggfunc={"area_km": "sum"}).reset_index()
    
    # Cria o mapa
    fig = px.choropleth(
        df_agg,
        geojson=df_agg.geometry,
        locations=df_agg.index,
        color="area_km",
        hover_name="state",
        labels={"area_km": "Área (km²)"},
        title=f"Desmatamento por estado em {ano_selecionado}",
        projection="mercator"
    )
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin=dict(l=10, r=10, t=40, b=10))
    return fig