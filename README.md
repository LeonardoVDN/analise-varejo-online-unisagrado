# 📊 Análise de Tendências de Mercado de Varejo Online

## 🎯 Visão Geral

Projeto desenvolvido em parceria com o Centro Universitário UNISAGRADO, sob orientação do Prof. Dr. Victor Hugo Braguim Canto, aplicando conceitos avançados de **Análise de Dados** e **Business Intelligence** para explorar o comportamento de vendas no e-commerce brasileiro.

---

## 💡 Problema de Pesquisa

> **Como podemos agrupar categorias de produtos com perfis semelhantes de ticket médio, avaliação e volume, para orientar decisões de marketing e estoque focadas em maximizar receita e satisfação do cliente?**

---

## 👥 Equipe

* **Leonardo Valentim do Nascimento**
* **Udymilla Gonçalves Chagas**
* **Natasha Cristine Barbosa**

---

## 📑 Objetivos do Projeto

* Identificar padrões de comportamento de consumo no e-commerce brasileiro
* Analisar tendências de vendas e categorias de maior receita
* Desenvolver agrupamentos (clusters) de produtos com características semelhantes
* Criar um dashboard interativo para visualização dinâmica dos resultados
* Fornecer insights acionáveis para decisões de marketing e gestão de estoque

---

## 🔍 Metodologia

O projeto emprega uma metodologia completa de ciência de dados:

1. **Extração de Dados:** Utilização do dataset público "Brazilian E-commerce Public Dataset" (Kaggle)
2. **Transformação:** Pipeline ETL para limpeza e integração de dados
3. **Análise Exploratória:** Identificação de padrões e tendências nos dados
4. **Análise Estatística:** Testes de correlação e ANOVA entre variáveis-chave
5. **Machine Learning:** Técnicas de clustering para segmentação de categorias
6. **Visualização:** Dashboard interativo para exploração dos resultados

---

## 📂 Estrutura do Projeto

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

---
## 🛠️ Tecnologias Utilizadas

* **Python 3.8+**
* **Jupyter Notebook** - Desenvolvimento e documentação
* **pandas & numpy** - Manipulação e análise de dados
* **matplotlib & plotly** - Visualização de dados
* **scikit-learn & scipy** - Modelagem estatística e machine learning
* **streamlit** - Dashboard interativo

---
## 🔢 Fluxo de Análise

1. **Carga e inspeção inicial dos dados** (00-load.ipynb)
   * Importação dos datasets originais
   * Análise preliminar de estrutura e qualidade

2. **Limpeza e integração** (01-clean.ipynb)
   * Tratamento de valores ausentes e outliers
   * Integração das tabelas relacionadas
   * Criação de métricas derivadas

3. **Exploração de dados (EDA)** (02-eda.ipynb)
   * Análise de vendas por categoria
   * Evolução mensal de receita
   * Distribuição de preços e avaliações

4. **Análise estatística** (03-corr.ipynb)
   * Identificação de correlações entre variáveis
   * Testes ANOVA para validação de hipóteses

5. **Clustering** (04-cluster.ipynb)
   * Segmentação de categorias por perfil de vendas
   * Identificação de grupos com características semelhantes

6. **Dashboard interativo** (app.py)
   * Visualização dinâmica dos resultados
   * Filtros por categoria, período e clusters
---

## 🚀 Instruções para Execução

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

---

## 📈 Principais Resultados

- **Identificação de categorias de alto e baixo ticket médio**  
  Encontramos quais grupos de produtos geram maior receita por pedido e quais mantêm preços mais acessíveis.

- **Análise da evolução temporal de receita por segmento**  
  Visualizamos como a receita mensal se comporta ao longo do período de estudo para cada categoria selecionada.

- **Segmentação de produtos em clusters com características semelhantes**  
  Aplicamos K-Means para agrupar categorias em perfis homogêneos de ticket médio, avaliação e volume de vendas.

- **Dashboard interativo para exploração dinâmica dos resultados**  
  Implementamos um app em Streamlit com filtros de categoria, período e cluster, exibindo KPIs, séries temporais e dispersões interativas.

---

## 📝 Contexto Acadêmico

Este projeto foi desenvolvido como parte da disciplina de Análise de Dados e Business Intelligence do Centro Universitário UNISAGRADO, seguindo as diretrizes estabelecidas pelo professor orientador Victor Hugo Braguim Canto.

---

## 📚 Referências

* Dataset: [Brazilian E-commerce Public Dataset by Olist](https://www.kaggle.com/olistbr/brazilian-ecommerce)
* Documentação das bibliotecas: [pandas](https://pandas.pydata.org/docs/), [scikit-learn](https://scikit-learn.org/stable/documentation.html), [Streamlit](https://docs.streamlit.io/)