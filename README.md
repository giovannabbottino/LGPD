# LGPD

## Features
- [X] REGEX para:
    - [X] CNPJ
    - [X] CPF
    - [x] Data de nascimento
    - [X] RG
        - [X] SP
        - [X] DF
- [X] Leitura de pdf 

## Pré-requisitos 
Para desenvolver esse projeto localmente basta clonar esse repositorio e utilizar as ferramentas de _git_ para versionamento. 
Para usar esse programa vocês precisará de Python3.

## Rodando
```bash
# após clonar esse repositorio 
# acesse a pasta do projeto
$ cd LGPD

# crie um ambiente em python3
$ python -m venv nome_ambiente

# acesse o ambiete 
$ .\nome_ambiente\Scripts\activate

# se necessario
$ Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process

# baixa os modulos
$(nome_ambiente)  pip install -r requirements.txt

# dentro do codigo é preciso adicionar o nome dos arquivo
# assim é necessario apenas 
$(nome_ambiente)  python main.py
```