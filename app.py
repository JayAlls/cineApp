from tkinter import *

window = Tk()
window.geometry("720x540")
window.minsize(720, 540)
window.title("Séance de cinéma - Logiciel de gestion")
window.config(background="grey")



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


def click_btn(film_id, txt):
    print(f"Vous avez choisis le film {films[film_id - 1]['titre']}")

    nb_place = films[film_id - 1]['places']

    if nb_place > 0:
        print("Achat efféctué !")
        films[film_id-1]['places'] -= 1
        txt.set(films[film_id-1]['places'])
        print(f'Film {films[film_id - 1]["titre"]}, nombre de place restante : {nb_place}')

    else:
        print("Film Complet")
        txt.set("Film Complet")


for numeros, film in enumerate(films, start=1):
    titre = film["titre"]
    horraire = film["horraire"]
    places = film["places"]
    place_var = StringVar()
    place_var.set(places)

    title_label = Label(window, text=titre, font=("Georgia", 20), bg='grey')
    title_label.grid(row= numeros, column=0)

    horraire_label = Label(window, text=horraire, font=("Georgia", 20), bg='grey')
    horraire_label.grid(row=numeros , column=1)

    places_label = Label(window, textvariable=place_var, font=("Georgia", 20), bg='grey')
    places_label.grid(row=numeros, column=2)

    bouton = Button(window, text='reserver', font=("Georgia", 20), bg='grey',
                    command= lambda num=numeros,
                    txt=place_var: click_btn(num, txt))
    bouton.grid(row=numeros, column=3)

window.mainloop()