class GPT:
    def __init__(self):
        self.furia_data = FuriaData()

    def query(self, input: str) -> str:
        input_lower = input.lower()
        
        # Respostas pré-definidas
        if "próximos jogos" in input_lower:
            matches = self.furia_data.get_next_matches()
            return f"Próximos jogos da FURIA:\n" + "\n".join(
                [f"{m['vs']} - {m['torneio']} ({m['data']})" for m in matches]
            )
        
        elif "escalação" in input_lower:
            roster = self.furia_data.get_team_roster()
            return "Escalação da FURIA:\n" + "\n".join(
                [f"{p['nome']} ({p['função']})" for p in roster]
            )
        
        elif "resultados" in input_lower:
            results = self.furia_data.get_latest_results()
            return "Últimos resultados:\n" + "\n".join(
                [f"{r['vs']} {r['resultado']} ({r['evento']})" for r in results]
            )
        
        else:
            # Usa GPT-J para respostas gerais
            return self._ask_gpt(input)
    
    def _ask_gpt(self, input: str) -> str:
        """Chama a API do Hugging Face para respostas gerais"""
        payload = {"inputs": f"Pergunta sobre FURIA CS:GO: {input}"}
        response = requests.post(MODEL_URL, headers=HEADERS, json=payload)
        return response.json()[0]['generated_text']