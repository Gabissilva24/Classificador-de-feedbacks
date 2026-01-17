from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from deep_translator import GoogleTranslator

def executar_suite_testes():
    """
    Executa uma bateria de testes automatizados para validar a precisao
    do classificador em diferentes cenarios de sentimentos.
    """
    analisador = SentimentIntensityAnalyzer()
    tradutor = GoogleTranslator(source='pt', target='en')
    
    # Lista de cenarios (Dicionario com entrada e resultado esperado)
    cenarios = [
        {"frase": "O produto é maravilhoso!", "esperado": "POSITIVO"},
        {"frase": "Tive problemas com a entrega", "esperado": "NEGATIVO"},
        {"frase": "O suporte demorou muito", "esperado": "NEGATIVO"},
        {"frase": "O papel é branco", "esperado": "NEUTRO"},
        {"frase": "A interface é funcional, mas poderia ser intuitiva", "esperado": "NEUTRO"}
    ]
    
    palavras_negativas = ["problema", "atraso", "demorou", "dificuldade"]
    passou = 0
    falhou = 0

    print("--- INICIANDO SUITE DE TESTES AUTOMATIZADOS (QA) ---\n")

    for cenario in cenarios:
        frase = cenario["frase"]
        traducao = tradutor.translate(frase)
        score = analisador.polarity_scores(traducao)['compound']
        tem_critica = any(word in frase.lower() for word in palavras_negativas)

        # Logica de Classificacao (Threshold + Regra de Negocio)
        if score > 0.05:
            resultado = "POSITIVO"
        elif tem_critica or score < -0.05:
            resultado = "NEGATIVO"
        else:
            resultado = "NEUTRO"

        # Validacao do resultado esperado vs obtido
        if resultado == cenario["esperado"]:
            print(f"✅ PASSOU: '{frase}' -> {resultado}")
            passou += 1
        else:
            print(f"❌ FALHOU: '{frase}' -> Esperado: {cenario['esperado']}, Obtido: {resultado} (Score: {score})")
            falhou += 1

    print(f"\n--- RELATÓRIO FINAL ---")
    print(f"Total de testes: {len(cenarios)} | Sucessos: {passou} | Falhas: {falhou}")

if __name__ == "__main__":
    executar_suite_testes()