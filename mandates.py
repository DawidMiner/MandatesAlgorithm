import math
import matplotlib.pyplot as plt


class Mandates:
    def __init__(self):
        self.table_of_votes = []
        self.table_of_mandates = []
        self.parties_index = []

    def CreateTableOfSumsOfVotes(self):
        number_of_parties = int(input("Podaj liczbę partii: "))
        for party in range(0, number_of_parties):
            keep_trying = True
            while keep_trying:
                try:
                    votes = int(input(f"Ile głosów ma partia numer {party + 1}: "))
                    if votes > 0:
                        self.table_of_votes.append([votes])
                        keep_trying = False
                    else:
                        print("Liczba głosów musi byc liczbą nieujemną")

                except:
                    print("Liczba głosów musi byc liczbą nieujemną")

        return self.table_of_votes

    def DivideSumsOfVotes(self, start_divider, loop_jump, end_of_loop):
        for party in self.table_of_votes:
            if start_divider == 3:
                party.append(round(party[0]/1.4, 0))
                for divider in range(start_divider, (end_of_loop * 2) + 1, loop_jump):
                    if (round(party[0] / divider)) != party[-1]:
                        party.append(round(party[0] / divider))
            if start_divider == 1:
                for divider in range(start_divider, end_of_loop + 1, loop_jump):
                    if (round(party[0] / divider)) != party[-1]:
                        party.append(round(party[0] / divider))
            party.append(0)

        return self.table_of_votes

    def ChooseMandates(self, amount_of_mandates):
        mandate_for_party_number = 0
        position_in_table_of_votes = 0

        for mandate in range(0, amount_of_mandates):
            highest_number = 0
            for party in range(len(self.table_of_votes) - 1, -1, -1):
                for votes in range(0, len(self.table_of_votes[party]) - 1):
                    if self.table_of_votes[party][votes] > highest_number:
                        highest_number = self.table_of_votes[party][votes]
                        mandate_for_party_number = party
                        position_in_table_of_votes = votes
            try:
                self.table_of_votes[mandate_for_party_number].remove(
                    self.table_of_votes[mandate_for_party_number][position_in_table_of_votes])
                self.table_of_votes[mandate_for_party_number][len(self.table_of_votes[mandate_for_party_number]) - 1] += 1
            except IndexError:
                pass

        return self.table_of_votes

    def MandatesWithHareNiemeyera(self, amount_of_mandates):
        sum_of_all_votes = 0
        sum_of_all_mandates = 0
        for party in self.table_of_votes:
            sum_of_all_votes += party[0]

        for party in self.table_of_votes:
            party.append(math.floor((party[0] * amount_of_mandates) / sum_of_all_votes))
            party.append(abs((party[0] * amount_of_mandates) - (party[1] * sum_of_all_votes)))
            sum_of_all_mandates += math.floor(party[1])
        if sum_of_all_mandates < amount_of_mandates:
            for mandate in range(0, amount_of_mandates - sum_of_all_mandates):
                max_rest = 0
                number_of_party = []
                number_of_party_with_max_rest = 0
                for party in range(len(self.table_of_votes) - 1, -1, -1):
                    if self.table_of_votes[party][2] >= max_rest:
                        number_of_party_with_max_rest = party
                        max_rest = self.table_of_votes[party][2]
                number_of_party.append(number_of_party_with_max_rest)
                for party in range(len(self.table_of_votes) - 1, -1, -1):
                    if self.table_of_votes[party][2] == max_rest and party not in number_of_party:
                        number_of_party.append(party)
                if len(number_of_party) == 1:
                    self.table_of_votes[number_of_party[0]][1] += 1
                else:
                    mandate_for_party = 0
                    min_votes = self.table_of_votes[number_of_party[0]][1]
                    for party in number_of_party:
                        if self.table_of_votes[party][1] < min_votes:
                            min_votes = self.table_of_votes[party][1]
                            mandate_for_party = party
                    self.table_of_votes[mandate_for_party][1] += 1

    def DisplayNumbersOfMandates(self, choice):
        number_of_party = 1
        if choice == 1 or choice == 2:
            for party in self.table_of_votes:
                print(f"Dla partii numer {number_of_party}: {party[len(party) - 1]}")
                number_of_party += 1
        elif choice == 3:
            for party in self.table_of_votes:
                print(f"Dla partii numer {number_of_party}: {math.floor(party[1])}")
                number_of_party += 1

    def AddMandatesToList(self, choice):
        for party in self.table_of_votes:
            if choice == 3:
                self.table_of_mandates.append(math.floor(party[1]))
            elif choice == 1 or choice == 2:
                self.table_of_mandates.append(math.floor(party[-1]))

        for num in range(1, len(self.table_of_mandates) + 1):
            self.parties_index.append(num)
        return self.table_of_mandates

    def DisplayGraph(self):
        plt.bar(self.parties_index, self.table_of_mandates)
        plt.xlabel("Numer partii")
        plt.ylabel("Ilość przysługującyh mandatów")
        plt.title("Wykres przysługujących mandatów")
        plt.show()
