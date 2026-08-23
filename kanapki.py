def lista_skladnikow(*skladniki):
    print("Zamowiona kanapka ma: ")
    for skladnik in skladniki:
        print(f"- {skladnik}")

lista_skladnikow("mango", "musztarde")
lista_skladnikow("tunczyk", "salate", "pomidora")
lista_skladnikow("czipsy")
