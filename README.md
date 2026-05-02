# Automação de testes - API + Web

<img loading="lazy" src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge"/>


## Objetivo  
Projeto acadêmico desenvolvido para automatizar teste de API e Web, aplicando boas práticas de desenvolvimento, organização de código e integração contínua (CI/CD).


## Escopo

### Automação de testes para API
    Testes automatizados para a API do Swagger Petstore, cobrindo todos os endpoints das entidades:
    - User
    - Pet
    - Store

### automação de testes para Web
    Testes automatizados E2E no site SauceDemo usando Selenium, e executando o fluxo:
    - Login
    - Adição de produtos ao carrinho 
    - Finalização de compra


## Tecnologias Utilizadas
    - Python: Linguagem base do projeto.
    - Pytest: Framework para criação, organização e execução dos testes.
    - Requests: Biblioteca para automação e validação dos endpoints da API.
    - Selenium WebDriver: Ferramenta para automação de interações no navegador (Web E2E).
    - GitHub Actions: Ferramenta para implementação da Pipeline de CI.


## Estrutura do projeto
    
    ├── /api-tests
    ├── /web-tests
    ├── /.github/workflows
    └── README.md


## Como Executar

### Clonar repositório
```bash
git clone https://github.com/ditimon01/Automa-o-QA-petstore-saucedemo
```

### Instalar dependências
```bash
pip install -r requirements.txt
```

### Rodar Testes
```bash
# API
pytest api-tests/

# Web
pytest web-tests/
```
