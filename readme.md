# Relatórios Preços de ações da B3 IBOV

Este script Python acessa o site da b3 e captura as informações das ações em alta e baixa.

## Execução do Script

1. **Execute o script Python**
- O script acessará o site da B3 para obter informações sobre as ações.
- Os dados serão processados e exportados para dois arquivos separados com os dados das ações em alta e baixa.
- O nome do arquivo com as ações em alta será `high_price.csv`.
- O nome do arquivo com as ações em baixa será `low_price.csv`.

## Pré-requisitos

- Python 3.x
- Virtualenv (opcional, mas recomendado)

## Instalação

1. **Clone o repositório:**

```bash```
- git clone https://github.com/seu-usuario/seu-projeto.git
- cd seu-projeto

2. **Crie e ative um ambiente virtual(opcional):**
- python -m venv venv
- source venv/bin/activate  # No Windows, use 'venv\Scripts\activate'

3. **Instale as dependências:**
```bash```
- pip install -r requirements.txt

4. **Utilização:**
- cd no diretório raiz do projeto
- ative o ambiente virtual (opcional)
- python run.py

# Logs 
Os logs de execução são armazenados no arquivo `log.log` na raiz do projeto.