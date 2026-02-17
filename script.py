from flask import Flask, render_template

app = Flask(__name__)

# Simulation d'une base de données de croquettes
CROQUETTES = [
    {"id": 1, "nom": "Énergie Plus", "prix": 45.99, "description": "Pour chiens sportifs et actifs.", "image": "energie.jpg"},
    {"id": 2, "nom": "Sénior Confort", "prix": 39.50, "description": "Facile à digérer pour les vieux toutous.", "image": "senior.jpg"},
    {"id": 3, "nom": "Chiot Croissance", "prix": 42.00, "description": "Tout ce qu'il faut pour bien grandir.", "image": "chiot.jpg"},
]

@app.route('/')
def home():
    return render_template('index.html', produits=CROQUETTES)

@app.route('/produit/<int:produit_id>')
def detail_produit(produit_id):
    # Chercher le produit correspondant à l'ID
    produit = next((p for p in CROQUETTES if p['id'] == produit_id), None)
    return render_template('produit.html', produit=produit)

if __name__ == '__main__':
    app.run(debug=True)
