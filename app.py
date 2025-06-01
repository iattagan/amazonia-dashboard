# app.py

import dash
import dash_bootstrap_components as dbc
from components.data_loader import load_deforestation_gdf
from components.layout import serve_layout
from components.callbacks import register_callbacks

# Instancia a aplicação (pode usar tema Bootstrap via CDN opcionalmente)
app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Amazônia em Alerta"

# Carrega o GeoDataFrame para extrair anos e estados disponíveis
GDF = load_deforestation_gdf()
anos_disponiveis = sorted(GDF["year"].unique().tolist())
estados_disponiveis = ["Todos"] + sorted(GDF["state"].unique().tolist())

# Define o layout, passando listas para dropdowns e sliders
app.layout = serve_layout(app, anos_disponiveis, estados_disponiveis)

# Registra todos os callbacks (KPIs, gráficos e mapa)
register_callbacks(app)

if __name__ == "__main__":
    app.run(debug=True)
