# log-analyzer

Ferramenta CLI em Python para análise de logs de autenticação.

## O que faz

- Detecta múltiplas tentativas de login falhas
- Identifica possível brute force
- Detecta login com sucesso após falhas
- Exporta resultados em JSON
- Gera relatórios

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
