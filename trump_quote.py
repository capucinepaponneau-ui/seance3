import requests

def get_random_trump_quote():
    # L'URL du point de terminaison pour une citation aléatoire
    url = "https://api.whatdoestrumpthink.com/api/v1/quotes/random"
    
    try:
        # Envoi de la requête GET
        response = requests.get(url)
        
        # Vérification que la requête a réussi (code 200)
        response.raise_for_status()
        
        # Extraction des données JSON
        data = response.json()
        
        # L'API renvoie un dictionnaire avec la clé 'message'
        quote = data.get('message')
        
        return quote

    except requests.exceptions.RequestException as e:
        return f"Erreur lors de la récupération de la citation : {e}"

if __name__ == "__main__":
    print("--- Citation aléatoire de Trump ---")
    quote = get_random_trump_quote()
    print(f"\" {quote} \"")