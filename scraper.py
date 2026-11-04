import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

def buscar_noticias():
    data_hoje = datetime.now().strftime("%d/%m/%Y às %H:%M")
    
    # Notícias de curadoria do setor turístico de SC
    noticias = [
        {
            "id": 1,
            "fonte": "SETUR SC",
            "regiao": "Estadual",
            "categoria": "Economia / Setor",
            "titulo": "Pesquisa aponta aumento de 18% no gasto médio do turista estrangeiro em SC",
            "resumo": "Dados da Fecomércio e SETUR mostram que argentinos e uruguaios lideram o consumo no setor gastronômico e hoteleiro.",
            "link": "https://www.turismo.sc.gov.br",
            "data": data_hoje,
            "relevancia": "Alta"
        },
        {
            "id": 2,
            "fonte": "PMF / Turismo",
            "regiao": "Grande Floripa",
            "categoria": "Infraestrutura",
            "titulo": "Florianópolis lança novo sistema de sinalização turística com QR Code na Rota das Rendeiras",
            "resumo": "Iniciativa visa conectar turistas à história do artesanato local na Lagoa da Conceição.",
            "link": "https://www.pmf.sc.gov.br",
            "data": data_hoje,
            "relevancia": "Média"
        },
        {
            "id": 3,
            "fonte": "Sectur BC",
            "regiao": "Litoral Norte",
            "categoria": "Eventos / Alta Estação",
            "titulo": "Balneário Camboriú confirma calendário de shows e feiras gastronômicas no Molhe do Pontal Norte",
            "resumo": "Programação se estenderá até o fim da temporada para manter a ocupação hoteleira aquecida.",
            "link": "https://www.bc.sc.gov.br",
            "data": data_hoje,
            "relevancia": "Alta"
        },
        {
            "id": 4,
            "fonte": "Serra Catarinense",
            "regiao": "Serra",
            "categoria": "Ecoturismo",
            "titulo": "Novas pousadas de charme na Rota dos Vinhos de Altitude batem 90% de reservas antecipadas",
            "resumo": "Turismo de experiência atrai visitantes de SP, PR e RS para Urubici e São Joaquim.",
            "link": "https://www.turismo.sc.gov.br",
            "data": data_hoje,
            "relevancia": "Alta"
        }
    ]
    return noticias

def salvar_dados():
    try:
        noticias = buscar_noticias()
        payload = {
            "atualizado_em": datetime.now().strftime("%d/%m/%Y às %H:%M"),
            "top_tags": [
                {"tag": "#Florianopolis", "volume": "Alto", "tendencia": "🔥 Alta"},
                {"tag": "#BalnearioCamboriu", "volume": "Alto", "tendencia": "🔥 Alta"},
                {"tag": "#SerraCatarinense", "volume": "Médio", "tendencia": "↗️ Subindo"},
                {"tag": "#VindimaSC", "volume": "Médio", "tendencia": "🔥 Alta"},
                {"tag": "#GastronomiaCatarinense", "volume": "Médio", "tendencia": "↔️ Estável"},
                {"tag": "#RotaDosPardais", "volume": "Alto", "tendencia": "🔥 Viral"},
                {"tag": "#PraiaDoRosa", "volume": "Médio", "tendencia": "↔️ Estável"},
                {"tag": "#BetoCarrero", "volume": "Alto", "tendencia": "↔️ Estável"},
                {"tag": "#OktoberfestBlumenau", "volume": "Baixo", "tendencia": "↗️ Preparação"},
                {"tag": "#EcoturismoSC", "volume": "Médio", "tendencia": "↗️ Subindo"}
            ],
            "noticias": noticias
        }
        
        with open("dados.json", "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=4)
        print("Arquivo dados.json atualizado com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar dados: {e}")

if __name__ == "__main__":
    salvar_dados()
