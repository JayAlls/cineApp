films = [{
        "titre": "Voyage au centre du HTML",
        "horraire": "18h",
        "places": 200
    },
    {
        "titre": "Les 9 json cachés",
        "horraire": "19h30",
        "places": 80
    },
    {
        "titre": "Algobox",
        "horraire": "21h",
        "places": 110
    }
]

for numeros, film in enumerate(films, start=1):
    titre = film["titre"]
    horraire = film["horraire"]
    places = film["places"]

    print(f"Salle {numeros}: {titre}, séances {horraire}, nombre de places: {places}")


while True:
    choix = int(input("Entrez le numéros de salle du film que vous désirez voir (1,2 ou 3): "))
    print(f"Vous avez choisis le film {films[choix-1]['titre']}")

    nb_place = films[choix-1]['places']

    if nb_place > 0:
        print("Achat efféctué !")
        films[choix-1]['places'] -= 1
        print(f'Film {films[choix-1]["titre"]}, nombre de place restante : {nb_place}')

    else:
        print('Film Complet !')