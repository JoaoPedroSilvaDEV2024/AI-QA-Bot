# 🤖 AI QA Bot — Sistema Inteligente de Testes Automatizados

AI QA Bot é uma ferramenta de **Quality Assurance automatizado com IA**, projetada para gerar, executar e analisar testes de APIs de forma inteligente, simulando um fluxo real de validação usado em ambientes de produção.

---

## 🧠 Sobre o projeto

O AI QA Bot automatiza o processo de testes de software utilizando inteligência artificial e regras de validação.

O sistema permite:

- Analisar endpoints de APIs
- Gerar casos de teste automaticamente
- Executar testes de forma automatizada
- Avaliar qualidade e confiabilidade do sistema
- Gerar relatórios de resultados

Este projeto simula uma ferramenta interna de QA utilizada por times de engenharia em empresas modernas.

---

## ⚙️ Tecnologias utilizadas

### 💻 Backend / Core

- Python
- FastAPI
- Requests
- Pytest

### 🤖 Inteligência Artificial

- Lógica de geração de testes (IA-ready)
- Estrutura preparada para integração com LLMs (OpenAI)

### 🔁 Automação

- Execução automatizada de testes
- Pipeline estilo CI/CD (GitHub Actions ready)
- Logging de resultados

---

## 🧪 Funcionalidades

- Geração automática de testes para APIs
- Execução de testes em endpoints reais ou locais
- Validação de respostas esperadas
- Análise de sucesso/falha
- Relatório estruturado de qualidade
- Estrutura preparada para IA generativa

---

## 📊 Como funciona

1. O sistema analisa um endpoint ou serviço
2. Gera automaticamente casos de teste
3. Executa requisições HTTP
4. Valida respostas retornadas
5. Gera um relatório final de qualidade

---

## 🚀 Como rodar o projeto

### 1. Instalar dependências

```bash
pip install fastapi uvicorn pytest requests
```
### 2. Rodar API (ambiente de teste)

```bash
python -m uvicorn app.api:app --reload
```
### Executar AI QA Bot

```bash
python main.py
```
---
## 📁 Estrutura do projeto

```
ai-qa-bot/
│
├── app/
│   ├── api.py              # API de teste (FastAPI)
│   ├── analyzer.py        # Análise de resultados
│   ├── runner.py          # Executor de testes
│   ├── test_generator.py  # Gerador de testes (IA-ready)
│   ├── logger.py          # Logs e registros
│   └── report.json        # Relatório gerado
│
├── tests/
│   └── test_api.py        # Testes automatizados
│
└── main.py                # Orquestrador principal
```
