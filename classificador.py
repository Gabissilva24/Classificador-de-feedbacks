from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from deep_translator import GoogleTranslator

def analisar_feedbacks():
    """
    Realiza a análise de sentimentos em feedbacks de clientes utilizando 
    uma abordagem híbrida de IA (VADER) e regras baseadas em palavras-chave.
    """
    analisador = SentimentIntensityAnalyzer()
    tradutor = GoogleTranslator(source='pt', target='en')

    feedbacks = [
        "O produto é excelente e superou minhas expectativas!",
        "Tive problemas com a entrega, o suporte demorou a responder.",
        "A interface é funcional, mas poderia ser mais intuitiva."
    ]

    print("--- Analisando Sentimentos com VADER ---\n")

    for frase in feedbacks:
        try:
            # Tradução necessaria pois o modelo VADER otimizado para a lingua inglesa
            frase_en = tradutor.translate(frase)

            # Calculo de polaridade (-1 a 1)
            scores = analisador.polarity_scores(frase_en)
            polaridade = scores['compound']

            # Regras de Negocio: Identificacao de termos criticos que a IA pode subestimar
            palavras_negativas = ["problem", "delay", "slow", "difficult", "support"]
            contem_critica = any(word in frase_en.lower() for word in palavras_negativas)

            # Classificação final baseada no threshold e na presenca de criticas diretas
            if polaridade > 0.01:
                status = "POSITIVO ✅"
            elif "problema" in frase.lower() or "demorou" in frase.lower() or polaridade < 0:
                status = "NEGATIVO ❌"
            else:
                status = "NEUTRO ⚪"

            print(f"Original: {frase}")
            print(f"Traduzido: {frase_en}")
            print(f"Status: {status} (Score: {polaridade})\n")
            
        except Exception as e:
            print(f"Erro ao processar a frase: {frase}. Erro: {e}")

if __name__ == "__main__":
    analisar_feedbacks()