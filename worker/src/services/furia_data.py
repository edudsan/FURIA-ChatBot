import requests
from bs4 import BeautifulSoup

class FuriaData:
    @staticmethod
    def get_next_matches():
        """Retorna os próximos jogos da FURIA"""
        url = "https://www.hltv.org/team/8297/furia"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        matches = []
        
        # Exemplo de scraping (ajuste conforme o site)
        for match in soup.select(".upcoming-matches .match"):
            opponent = match.select_one(".team-name").text
            tournament = match.select_one(".event-name").text
            date = match.select_one(".match-time").text
            matches.append({
                "vs": opponent,
                "torneio": tournament,
                "data": date
            })
        return matches

    @staticmethod
    def get_team_roster():
        """Retorna a escalação atual da FURIA"""
        return [
            {"nome": "KSCERATO", "função": "Rifler"},
            {"nome": "yuurih", "função": "Rifler"},
            {"nome": "arT", "função": "IGL/AWPer"},
            {"nome": "drop", "função": "Rifler"},
            {"nome": "saffee", "função": "AWPer"}
        ]

    @staticmethod
    def get_latest_results():
        """Retorna os últimos resultados"""
        return [
            {"vs": "Natus Vincere", "resultado": "2-1", "evento": "IEM Katowice"},
            {"vs": "Vitality", "resultado": "1-2", "evento": "BLAST Premier"}
        ]