# Como Usar os Paths de Configuração

## Nos Notebooks

### Opção 1: Importar path específico
```python
from config import PIB_MUNICIPIOS_RAW

# Usar diretamente
df = pd.read_csv(PIB_MUNICIPIOS_RAW)
```

### Opção 2: Importar todos os paths
```python
from config import DATA_RAW_DIR, DATA_PROCESSED_DIR, PIB_MUNICIPIOS_RAW

# Usar os paths conforme necessário
df = pd.read_csv(PIB_MUNICIPIOS_RAW)
```

### Opção 3: Usar função helper para listar todos os arquivos de dados
```python
from config import get_data_files

files = get_data_files()
print(files)
# Output: {'pib_municipios_raw': PosixPath(...), 'data_raw_dir': PosixPath(...), ...}
```

### Opção 4: Importar diretórios
```python
from config import DATA_PROCESSED_DIR, FIGURES_DIR, REPORTS_DIR

# Salvar dados processados
df_clean.to_csv(DATA_PROCESSED_DIR / "dados_limpos.csv")

# Salvar figura
plt.savefig(FIGURES_DIR / "minha_figura.png")
```

## Nos Scripts Python (main.py, etc)

```python
from config import PIB_MUNICIPIOS_RAW, DATA_PROCESSED_DIR

# Carregar dados
df = pd.read_csv(PIB_MUNICIPIOS_RAW)

# Processar e salvar
df_processed = process_data(df)
df_processed.to_csv(DATA_PROCESSED_DIR / "dados_processados.csv")
```

## Adicionar Novos Arquivos

Quando criar novos arquivos processados, adicione a referência em `config/settings.py`:

```python
# ====== PROCESSED DATA FILES ======
PIB_MUNICIPIOS_CLEANED = DATA_PROCESSED_DIR / "pib_municipios_cleaned.csv"
PIB_MUNICIPIOS_MODELED = DATA_PROCESSED_DIR / "pib_municipios_modeled.csv"
```

Depois, atualize o `__init__.py` para exportar as novas constantes.

## Testar Configuração

Para verificar se todos os paths estão corretos, execute:

```bash
python config/settings.py
```

Isso mostrará todos os caminhos configurados e confirmará se os arquivos existem.
