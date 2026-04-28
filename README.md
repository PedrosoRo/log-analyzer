# 🔎 Log Analyzer

Ferramenta CLI em Python para análise de logs de autenticação, focada na detecção de comportamentos suspeitos como brute force e possíveis invasões.

---------------------## ▶️ Uso rápido

loganalyzer sample.log

## Sobre

Este projeto foi desenvolvido como forma de aplicar na prática conceitos de análise de logs e segurança, focando em identificar padrões de comportamento ao invés de apenas listar eventos.

## Funcionalidades

- Detecta múltiplas tentativas de login falhas
- Identifica possível brute force por IP
- Detecta login com sucesso após falhas
- Exporta resultados em JSON
- Gera relatórios em arquivo
  
## Instalação

git clone https://github.com/PedrosoRo/log-analyzer.git
cd log-analyzer
pip install -e .

## Como usar

loganalyzer sample.log

loganalyzer sample.log --threshold 5

loganalyzer sample.log --output

loganalyzer sample.log --json

## Exemplo de uso

🔎 RELATÓRIO DE ANÁLISE
----------------------------------------
IP: 192.168.0.2 → 3 tentativas
⚠️ ALERTA: Possível brute force em 192.168.0.2

## Sobre o projeto

Projeto desenvolvido com o objetivo de praticar análise de logs e construção de ferramentas CLI voltadas para segurança.

## Aviso

Uso educacional. Utilize apenas em ambientes autorizados.
