# 📊 Classificador de Sentimentos Híbrido (NLP & Regras de Negócio)

Este projeto consiste em um sistema de análise de sentimentos desenvolvido em Python, focado em feedbacks de usuários. Ele utiliza uma abordagem híbrida que combina modelos de Processamento de Linguagem Natural (NLP) com validações customizadas para garantir alta precisão em cenários críticos.

## 🚀 Diferenciais do Projeto
O maior desafio identificado foi a ocorrência de "Falsos Neutros" ou "Falsos Positivos" em modelos de IA padrão. Para resolver isso, implementei:

* **Tradução Automática**: Integração com a biblioteca `deep-translator` para otimizar a entrada de dados para o léxico do VADER.
* **Camada de Verificação**: Filtro de palavras-chave críticas que "sobrescrevem" o score da IA caso termos negativos específicos (como "atraso" ou "problema") sejam detectados.

## 🧪 Validação de Qualidade (QA)
O projeto conta com uma suite de testes automatizados (`test_simples.py`) que valida 5 cenários distintos.

* **Identificação de Limitações:** Durante o desenvolvimento, os testes revelaram que frases como *"O suporte demorou muito"* eram interpretadas como positivas pela IA padrão (Score: 0.4019) devido à falta de contexto específico de negócio.
* **Implementação de Correção:** Com base nos logs de erro, refatorei a hierarquia da lógica para dar precedência às regras de negócio. 
* **Resultado Final:** Atualmente, o sistema apresenta **100% de sucesso** nos testes, garantindo que falhas de serviço críticas nunca sejam ignoradas em produção.

## 🛠️ Tecnologias
* **Python**: Linguagem base do projeto.
* **vaderSentiment**: Ferramenta para análise de polaridade e sentimentos.
* **deep-translator**: Biblioteca para normalização e tradução de idiomas.
* **Venv**: Ambiente virtual para isolamento e organização das dependências.