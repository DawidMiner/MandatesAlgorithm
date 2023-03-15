from mandates import Mandates
from tests import TestMyAlgorithm

mandates = Mandates()
mandates.CreateTableOfSumsOfVotes()
choice = int(input("Jaką metodą chcesz policzyć ilość mandatów przypadających dla danej partii?\n1. Metoda d'Hondt'a\n"
                   "2. Metoda Sainte-Lagu\n3. Metoda Hare-Niemeyer'a\nWybór numer: "))
amount_of_mandates = int(input("Podaj ilość mandatów do obsadzenia: "))

if choice == 1:
    mandates.DivideSumsOfVotes(1, 1, amount_of_mandates)
    mandates.ChooseMandates(amount_of_mandates)

if choice == 2:
    mandates.DivideSumsOfVotes(3, 2, amount_of_mandates)
    mandates.ChooseMandates(amount_of_mandates)

if choice == 3:
    mandates.MandatesWithHareNiemeyera(amount_of_mandates)

mandates.DisplayNumbersOfMandates(choice)
mandates.AddMandatesToList(choice)
mandates.DisplayGraph()

