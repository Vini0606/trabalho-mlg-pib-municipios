# Trabalho MLG - PIB dos Municípios

Análise econômica exploratória e modelagem de regressão para explicar os fatores que influenciam o valor bruto da Agropecuária brasileira.

## Visão Geral

Este projeto realiza uma análise completa do Produto Interno Bruto (PIB) dos municípios brasileiros, com foco especial em entender os fatores que influenciam o setor agropecuário. O trabalho contempla:

- **Exploração e Limpeza de Dados** (Parte 1): Análise inicial dos dados brutos com identificação de valores faltantes, outliers e inconsistências
- **Análise Territorial e Visualização** (Parte 2): Análise exploratória avançada com painéis de informações, mapas e estudos de correlação
- **Modelagem de Regressão** (Parte 3): Construção de modelos de regressão linear simples e múltipla com validação em dados de teste

## Estrutura do Projeto

```
trabalho-mlg-pib-municipios/
├── data/
│   ├── raw/                           # Dados originais (não modificados)
│   └── processed/
│       └── pib_municipios_limpo.csv   # Dados após limpeza e processamento
├── notebooks/
│   ├── 01_exploracao_e_limpeza.ipynb  # Exploração inicial e tratamento de dados
│   ├── 02_analise_territorial.ipynb   # Análise exploratória avançada
│   └── 03_modelagem_regressao.ipynb   # Construção e validação de modelos
├── config/
│   ├── settings.py                    # Configuração de paths do projeto
│   └── USAGE.md                       # Guia de uso dos paths
├── src/
│   ├── data_cleaning.py               # Funções para limpeza de dados
│   └── plots.py                       # Funções auxiliares para visualizações
├── reports/
│   ├── figures/                       # Gráficos e visualizações geradas
│   ├── relatorio_parte_1.pdf          # Relatório da Parte 1
│   └── relatorio_parte_2.pdf          # Relatório da Parte 2
├── pyproject.toml                     # Configuração do projeto e dependências
├── requirements.txt                   # Lista de dependências (pip)
└── README.md                          # Este arquivo
```

## Notebooks

### 📊 Notebook 1: Exploração e Limpeza de Dados (`01_exploracao_e_limpeza.ipynb`)

**Objetivos:**
- Carregar e explorar os dados brutos do PIB dos municípios (2010-2023)
- Identificar valores faltantes, outliers e inconsistências
- Aplicar técnicas de limpeza e transformação de dados
- Normalizar estrutura de dados para análises posteriores

**Saídas:**
- Dataset limpo e processado: `pib_municipios_limpo.csv`
- Análise descritiva com estatísticas por setor econômico

---

### 🗺️ Notebook 2: Análise Territorial e Visualização (`02_analise_territorial.ipynb`)

**Objetivos:**
- Criar painéis de informações (retrato fiel do período)
- Gerar mapas e visualizações territoriais
- Analisar correlações entre variáveis quantitativas
- Estudar relações entre variáveis qualitativas e quantitativas

**Seções:**
1. **Painéis de Informações**: Top 10 municípios por valor da agropecuária
2. **Mapas Territoriais**: Distribuição territorial por Unidade da Federação
3. **Análise de Correlação**: Correlação entre setores econômicos
4. **Relações Qualitativas**: Distribuição da agropecuária por grande região

**Bibliotecas Principais:** pandas, seaborn, matplotlib, plotly

---

### 📈 Notebook 3: Modelagem de Regressão (`03_modelagem_regressao.ipynb`)

**Objetivos:**
- Construir modelos de regressão linear simples e múltipla
- Validar modelos com divisão treino/teste (80/20)
- Analisar significância estatística dos coeficientes
- Diagnóstico de resíduos e validação de suposições

**Seções:**
1. **Divisão de Dados**: Separação em amostras de treino (80%) e teste (20%)
2. **Regressão Linear Múltipla**: Estimação via Mínimos Quadrados Ordinários (MQO)
3. **Avaliação do Modelo**: Análise de R² e RMSE
4. **Diagnóstico**: Verificação de normalidade e homocedasticidade dos resíduos

**Variáveis Explanatórias:**
- Valor adicionado bruto da Indústria
- Valor adicionado bruto dos Serviços
- Valor adicionado bruto da Administração

**Variável Dependente:**
- Valor adicionado bruto da Agropecuária

**Bibliotecas Principais:** statsmodels, scikit-learn, numpy, matplotlib

## Dados

### Dataset Principal
- **Fonte:** PIB dos Municípios (2010-2023)
- **Formato:** .csv (após processamento)
- **Localização:** `data/processed/pib_municipios_limpo.csv`

### Variáveis Principais
- Código do Município e Sigla da UF
- Nome do Município e Grande Região
- Valor adicionado bruto por setor (Agropecuária, Indústria, Serviços, Administração Pública)
- Valores em R$ 1.000 (preços correntes)

## Instalação e Configuração

### Pré-requisitos
- Python >= 3.11
- pip ou uv (gerenciador de pacotes)

### Instalação das Dependências

**Com pip:**
```bash
pip install -r requirements.txt
```

**Com uv (recomendado):**
```bash
uv venv
source .venv/bin/activate  # Linux/macOS
# ou
.venv\Scripts\activate  # Windows
uv sync
```

### Dependências Principais
- **pandas** (3.0.2+): Manipulação e análise de dados
- **numpy** (2.4.4+): Computação numérica
- **matplotlib** (3.10.8+): Visualizações básicas
- **seaborn** (0.13.2+): Visualizações estatísticas
- **plotly** (6.7.0+): Gráficos interativos
- **scikit-learn** (1.8.0+): Machine learning e métricas
- **statsmodels** (0.14.6+): Modelagem estatística avançada
- **openpyxl** (3.1.5+): Leitura de arquivos Excel
- **nbformat** (5.10.4+): Suporte a Jupyter Notebooks

## Como Usar

### Executar os Notebooks

1. **Ativar o ambiente virtual:**
   ```bash
   source .venv/bin/activate  # Linux/macOS
   .venv\Scripts\activate      # Windows
   ```

2. **Iniciar Jupyter:**
   ```bash
   jupyter notebook
   ```

3. **Abrir e executar os notebooks na seguinte ordem:**
   - `notebooks/01_exploracao_e_limpeza.ipynb`
   - `notebooks/02_analise_territorial.ipynb`
   - `notebooks/03_modelagem_regressao.ipynb`

### Usar Paths do Projeto

Nos notebooks, importe os paths pré-configurados:

```python
from config import PIB_MUNICIPIOS_PROCESSED, FIGURES_DIR, REPORTS_DIR

# Carregar dados processados
df = pd.read_csv(PIB_MUNICIPIOS_PROCESSED)

# Salvar figura
plt.savefig(FIGURES_DIR / "minha_figura.png")
```

Veja `config/USAGE.md` para mais exemplos.

## Resultados Esperados

### Após Notebook 1
- Estatísticas descritivas do dataset
- Identificação de outliers por setor econômico
- Dataset limpo pronto para análise

### Após Notebook 2
- Dashboard visual com top municípios
- Mapa de distribuição territorial
- Matriz de correlação entre setores
- Visualizações por grande região

### Após Notebook 3
- Coeficientes do modelo de regressão com p-values
- R² e RMSE em dados de teste
- Gráficos de diagnóstico (resíduos, normalidade)
- Interpretação dos fatores que influenciam a agropecuária

## Requisitos do Trabalho

O projeto atende aos seguintes requisitos:

✅ **Item 2.1**: Exploração e limpeza dos dados  
✅ **Item 2.2**: Análise de missing values e outliers  
✅ **Item 3.1**: Painéis de informações (retrato fiel)  
✅ **Item 3.2**: Mapas territoriais  
✅ **Item 3.3**: Análise de correlações  
✅ **Item 3.4**: Divisão treino/teste e validação  
✅ **Item 4.1-4.3**: Regressão simples e múltipla com inferência estatística  

## Contato e Informações

- **Projeto:** MLG - Modelagem de regressão aplicada ao PIB dos Municípios
- **Disciplina:** Modelagem Linear Generalizada
- **Data:** 2024/2025
