*
                📊 DASHBOARD ANALYTICS: E-COMMERCE INSIGHTS
             

Um motor de análise estatística e visualização interativa desenvolvido para 
transformar dados brutos de E-commerce em inteligência de negócio.



---
1. 🚀 GUIA RÁPIDO: COMO EXECUTAR
---

Siga estes passos para levantar o dashboard em menos de 2 minutos:

📌 PASSO 1: Clonar ou Baixar
   Certifique-se de que o arquivo 'app.py' e o dataset 'ecommerce_estatistica.csv'
   estejam na mesma pasta.

📌 PASSO 2: Preparar o Ambiente
   Abra o seu terminal/prompt e instale as dependências necessárias:
   
   $ pip install pandas plotly dash statsmodels

📌 PASSO 3: Ignorar o Motor
   Execute o script principal:
   
   $ python app.py

📌 PASSO 4: Visualizar
   O terminal informará que o Dash está rodando. Abra seu navegador e acesse:
   
   👉 http://127.0.0.1:8050



---
2. 🛠️ O QUE ESTÁ ACONTECENDO POR BAIXO DO CAPÔ?
---

O sistema opera em três camadas automatizadas:

A. PIPELINE DE LIMPEZA (Data Cleaning)
   - Normalização de strings (converte "2 mil" em 2000.0).
   - Tratamento de caracteres especiais e acentuação de colunas.
   - Conversão forçada de tipos numéricos e descarte de valores nulos (NaN).

B. MOTOR ESTATÍSTICO (Analytics)
   - Cálculo de correlação matricial (Pearson).
   - Modelagem de regressão linear OLS (Ordinary Least Squares).
   - Agrupamentos (Aggregation) por Marca e Gênero.

C. CAMADA DE VISUALIZAÇÃO (Front-end)
   - 06 Gráficos interativos com tecnologia Plotly.
   - Layout responsivo via Dash Components.



---
3. 📈 VISUALIZAÇÕES DISPONÍVEIS
---

| Gráfico              | Insight Gerado                                     |
|----------------------|----------------------------------------------------|
| Histograma Preços    | Identifica o posicionamento de preço no mercado.   |
| Densidade (Heatmap)  | Mostra onde o volume de vendas se concentra.       |
| Mapa de Correlação   | Revela o que realmente afeta a nota do produto.    |
| Top 10 Marcas        | Share de prateleira por fabricante.                |
| Pizza de Gênero      | Composição demográfica simplificada.               |
| Regressão Linear     | Prova se o desconto está gerando mais avaliações.  |

---
4. ⚠️ NOTAS TÉCNICAS
---

- Dataset: O sistema espera um arquivo chamado 'ecommerce_estatistica.csv'.
- Performance: O uso do 'statsmodels' permite que a linha de tendência (Trendline)
  seja calculada em tempo real sobre o volume total de dados.
- Interatividade: Todos os gráficos permitem Zoom, Pan e Exportação para PNG 
  através da barra de ferramentas flutuante do Plotly.
