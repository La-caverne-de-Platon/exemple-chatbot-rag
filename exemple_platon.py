import requests
from requests.cookies import RequestsCookieJar

def AI(query: str) -> str:
    # La requête PowerShell récupérée via l'inspecteur d'éléments du navigateur web, onglet "Réseau", clique-droit sur "generate_answer"
    url = "https://www.phorm.ai/api/db/generate_answer"
    headers = {
        "authority": "www.phorm.ai",
        "method": "POST",
        "path": "/api/db/generate_answer",
        "scheme": "https",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ko;q=0.5",
        "origin": "https://www.phorm.ai",
        "priority": "u=1, i",
        "sec-ch-ua": '"Chromium";v="124", "Microsoft Edge";v="124", "Not-A.Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "Content-Type": "application/json"
    }

    
    session = requests.Session()
    session.headers.update(headers)

    # Ici les informations vis à vis du philosophe, il faut toujours relier le projet Phorm à un repo Github
    payload = {
        "query": query,
        "project": "8f603354-e047-48cc-ad66-717a8ecdb598",
        "repos": ["https://github.com/la-caverne-de-platon/auteurs_platon/tree/main"]
    }

    # Au lieu d'attendre toute la réponse, on va afficher la réponse au fur et à mesure
    with session.post(url, json=payload, stream=True) as response:
        response.raise_for_status()
        found_answer = False
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                try:
                    decoded_chunk = chunk.decode('utf-8')
                except UnicodeDecodeError:
                    # ça peut arriver qu'il y ait des soucis, on les ignore pour le moment
                    continue
                if found_answer:
                    yield chunk
                elif '"answer":' in decoded_chunk:
                    # On affiche uniquement ce qui vient après le tag 'answer' de la réponse, à savoir la véritable réponse et non les sources utilisées
                    found_answer = True


# Comment s'en servir
query = "c'est quoi le bonheur selon Platon ?"
for chunk in AI(query):
    print(chunk.decode('utf-8'),  end='')
