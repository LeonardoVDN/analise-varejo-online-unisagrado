# Análise de Tendências de Mercado de Varejo Online

## Apresentação do Projeto

Este é um projeto de Analise de Dados e BI em conjunto com o centro universitario UNISAGRADO, seguindo as orientações do professor orientador VICTOR HUGO BRAGUIM CANTO.

Esse projeto aplica conceitos de **Análise de Dados** e **Business Intelligence** para explorar o comportamento de vendas no e-commerce brasileiro. A partir do dataset público "Brazilian E-commerce Public Dataset" (Kaggle).

## Breve Apresentação

* **Motivação**: entender tendências de vendas, categorias de maior receita e padrões de comportamento.
* **Metodologia**: pipeline de ETL em notebooks, EDA, testes estatísticos e clustering.
* **Resultados**: insights sobre categorias de baixo/alto ticket, evolução de receita e agrupamentos de produtos.
* **Ferramenta final**: dashboard interativo que permite filtrar categorias, períodos e visualizar KPIs e clusters.

### Esse projeto foi idealizado por um grupo de 3 alunos:
Leonardo Valentim do Nascimento
Udymilla Gonçalves Chagas
Natasha Cristine Barbosa

### Proposta e Objetivos Gerais do Projeto
Você e seu grupo devem propor, desenvolver e apresentar um projeto aplicado de Ciência de Dados que explore um problema real ou uma oportunidade de melhoria em qualquer área (ex.: saúde, educação, finanças, meio ambiente, esportes, varejo, logística etc.).

Objetivos Gerais
Identificar uma fonte de dados relevante (preferencialmente pública).

Formular uma pergunta ou problema orientador.

Aplicar conceitos e ferramentas da Ciência de Dados para responder ou solucionar a questão proposta.

Apresentar os resultados de forma clara, visual e fundamentada.

Utilize Python ou R.

### pergunta ou problema orientador.
Como podemos agrupar categorias de produtos com perfis semelhantes de ticket médio, avaliação e volume, para orientar decisões de marketing e estoque focadas em maximizar receita e satisfação do cliente?

### Arquivos e notebooks do projeto
1. **Carga e inspeção inicial dos dados** (`00-load.ipynb`)
2. **Limpeza e integração** de tabelas e criação de métricas derivadas (`01-clean.ipynb`)
3. **Exploração de dados (EDA)**: vendas por categoria, evolução mensal, distribuição de preços e avaliações (`02-eda.ipynb`)
4. **Análise de correlações e testes estatísticos** (ANOVA) entre variáveis-chave (`03-corr.ipynb`)
5. **Clustering** de categorias para identificar grupos com perfis de venda semelhantes (`04-cluster.ipynb`)
6. **Dashboard interativo** em Streamlit para visualização dinâmica dos resultados (`app.py`)

## Tecnologias e Bibliotecas

* Python 3.8+
* Jupyter Notebook
* pandas, numpy
* matplotlib, plotly
* scikit-learn, scipy
* streamlit

## Estrutura do Repositório

```
/ (raiz)
├── app.py                   # Dashboard Streamlit
├── requirements.txt         # Dependências Python
├── data/
│   ├── olist_*.csv          # CSVs originais baixados do Kaggle
│   ├── ecommerce_clean.csv  # Dados integrados e limpos
│   └── category_clusters.csv# Mapeamento categoria → cluster
└── notebooks/
    ├── 00-load.ipynb        # Carga e inspeção inicial
    ├── 01-clean.ipynb       # Limpeza e merge de tabelas
    ├── 02-eda.ipynb         # Exploração de dados (vendas e estatísticas)
    ├── 03-corr.ipynb        # Correlações e ANOVA
    └── 04-cluster.ipynb     # Clustering de categorias
```

## Passo a Passo para Rodar Localmente

### 1. Clonar o Repositório

```bash
git clone <URL_DO_REPO>
cd nome-do-repo
```

### 2. Criar e Ativar Ambiente Virtual

```bash
python3 -m venv venv           # Cria o virtualenv
source venv/bin/activate       # macOS/Linux
venv\Scripts\activate        # Windows
```

### 3. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 4. Preparar os Dados Se não possuir

1. Baixe manualmente o dataset no Kaggle: [https://www.kaggle.com/olistbr/brazilian-ecommerce](https://www.kaggle.com/olistbr/brazilian-ecommerce)
2. Extraia todos os CSVs na pasta `data/`.

### 5. Executar Notebooks em Ordem

Em um terminal ou no Jupyter Lab:

```bash
jupyter notebook
```

Abra e execute cada notebook na sequência:

1. `notebooks/00-load.ipynb`
2. `notebooks/01-clean.ipynb`
3. `notebooks/02-eda.ipynb`
4. `notebooks/03-corr.ipynb`
5. `notebooks/04-cluster.ipynb`

> **Atenção:** Após o clustering, será gerado o arquivo `data/category_clusters.csv`.

### 6. Rodar o Dashboard Streamlit

No terminal (na raiz do projeto):

```bash
streamlit run app.py
```

Abra o link exibido (geralmente [http://localhost:8501](http://localhost:8501)) para interagir com o dashboard.
