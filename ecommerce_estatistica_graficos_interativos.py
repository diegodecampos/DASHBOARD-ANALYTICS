import plotly.express as px
import pandas as pd
import numpy as np
from dash import Dash, html, dcc


# FUNÇÃO DE LIMPEZA
def limpar_dados(df):
    if df.empty:
        return df

    def limpar_vendas(valor):
        if isinstance(valor, str):
            valor = valor.lower().replace('+', '').replace('.', '').strip()
            if 'mil' in valor:
                valor = float(valor.replace('mil', '').replace(',', '.')) * 1000
            else:
                valor = valor.replace(',', '.')
        try:
            return float(valor)
        except:
            return 0.0

    # Limpeza e conversão
    if 'Qtd_Vendidos' in df.columns:
        df['Qtd_Vendidos'] = df['Qtd_Vendidos'].apply(limpar_vendas)

    df.columns = df.columns.str.replace('Gênero', 'Genero')

    for col in ['Preço', 'Nota', 'N_Avaliações', 'Desconto']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    return df.dropna(subset=['Preço', 'Qtd_Vendidos', 'Nota'])


# FUNÇÃO DE CRIAÇÃO DE GRÁFICOS
def cria_graficos(df):
    # 1. Histograma
    fig1 = px.histogram(df, x='Preço', nbins=50, title='Distribuição de Preços dos Produtos',
                        color_discrete_sequence=['green'], marginal="rug")

    # 2. Densidade
    fig2 = px.density_heatmap(df, x='Preço', y='Qtd_Vendidos', nbinsx=30, nbinsy=30,
                              title='Dispersão de Densidade: Preço vs. Vendas',
                              color_continuous_scale='Blues', text_auto=True)

    # 3. Mapa de Calor (Correlação)
    cols_corr = ['Preço', 'Nota', 'N_Avaliações', 'Desconto', 'Qtd_Vendidos']
    cols_existentes = [c for c in cols_corr if c in df.columns]
    corr_matrix = df[cols_existentes].corr()
    fig3 = px.imshow(corr_matrix, text_auto=".2f", aspect="auto",
                     title="Mapa de Calor de Correlação", color_continuous_scale='RdBu_r')

    # 4. Barras: Top 10 Marcas
    top_marcas = df['Marca'].value_counts().head(10).reset_index()
    top_marcas.columns = ['Marca', 'Contagem']
    fig4 = px.bar(top_marcas, x='Marca', y='Contagem', color='Marca',
                  title='Top 10 Marcas com Mais Produtos', color_discrete_sequence=px.colors.qualitative.Plotly)

    # 5. Pizza: Gênero
    col_gen = 'Genero' if 'Genero' in df.columns else df.columns[0]
    contagem_genero = df[col_gen].value_counts().reset_index()
    contagem_genero.columns = [col_gen, 'Valor']
    if len(contagem_genero) > 5:
        outros = pd.DataFrame([{col_gen: 'Outros', 'Valor': contagem_genero.iloc[5:]['Valor'].sum()}])
        contagem_genero = pd.concat([contagem_genero.head(5), outros])

    fig5 = px.pie(contagem_genero, names=col_gen, values='Valor', title='Distribuição por Gênero',
                  color_discrete_sequence=px.colors.qualitative.Safe)

    # 6. Regressão (Atenção: requer pip install statsmodels)
    fig6 = px.scatter(df, x='Desconto', y='N_Avaliações', trendline="ols",
                      title='Regressão: Impacto do Desconto nas Avaliações',
                      trendline_color_override="red", opacity=0.4)

    return fig1, fig2, fig3, fig4, fig5, fig6


# FUNÇÃO DE CRIAÇÃO DO APP
def cria_app(df):
    app = Dash(__name__)

    # Limpa os dados antes de gerar as figuras
    df_limpo = limpar_dados(df)

    if df_limpo.empty:
        app.layout = html.Div([html.H1("Erro: Dados não encontrados ou vazios.")])
        return app

    fig1, fig2, fig3, fig4, fig5, fig6 = cria_graficos(df_limpo)

    app.layout = html.Div(style={'backgroundColor': '#f4f4f9', 'padding': '30px', 'fontFamily': 'Arial'}, children=[
        html.H1("Dashboard de Análise E-commerce", style={'textAlign': 'center'}),
        html.Hr(),

        html.Div([
            dcc.Graph(figure=fig1),
            dcc.Graph(figure=fig2),
            dcc.Graph(figure=fig3),
            dcc.Graph(figure=fig4),
            dcc.Graph(figure=fig5),
            dcc.Graph(figure=fig6)
        ])
    ])
    return app


# EXECUTA O APP
try:
    df_original = pd.read_csv('ecommerce_estatistica.csv')
except FileNotFoundError:
    print("Arquivo não encontrado.")
    df_original = pd.DataFrame()

if __name__ == '__main__':
    app = cria_app(df_original)
    app.run(debug=True, port=8050)