# Machine Learning II

Exercícios práticos da disciplina de **Machine Learning II** da PUCRS.

Objetivo: aplicar técnicas de Machine Learning em Python usando notebooks, com foco em análise de dados, treinamento e avaliação de modelos.

## Setup no WSL Ubuntu

Pré-requisitos: WSL Ubuntu, Python 3 e `pip`.

### Do zero

```bash
cd machine-learning-II
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pip install jupyterlab ipykernel
jupyter lab
```

### Com o ambiente já criado

```bash
cd machine-learning-II
source venv/bin/activate
pip install -r requirements.txt
pip install jupyterlab ipykernel
jupyter lab
```

## Uso

Abra um notebook `.ipynb` no Jupyter Lab, selecione o kernel do ambiente virtual e execute as células.

Para salvar novas dependências:

```bash
pip freeze > requirements.txt
```

Para sair do ambiente virtual:

```bash
deactivate
```
