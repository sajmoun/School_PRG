import random

class Hrac:
    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.pozice = 1

class HadyAZebrikyHra:
    def __init__(self, pocet_hracu):
        self.velikost_desky = 100
        self.hraci = [Hrac(f"Hrac {i+1}") for i in range(pocet_hracu)]
        self.hady_a_zebriky = self.generuj_hady_a_zebriky()
        self.pozice_hracu = {hrac.pozice: hrac for hrac in self.hraci}

    def generuj_hady_a_zebriky(self):
        hady_a_zebriky = {
            2: 38,
            7: 14,
            8: 31,
            15: 26,
            16: 6,
            21: 42,
            28: 84,
            36: 44,
            46: 25,
            49: 11,
            51: 67,
            62: 19,
            64: 60,
            71: 91,
            74: 53,
            78: 98,
            87: 94,
            89: 68,
            92: 88,
            95: 75,
            99: 80
        }
        return hady_a_zebriky

    def pohyb_hrace(self, hrac, kroky):
        stara_pozice = hrac.pozice
        nova_pozice = hrac.pozice + kroky

        
        if nova_pozice in self.hady_a_zebriky: # Kontrola, zda se na dané pozici nachází speciální pole (had nebo žebřík)
            print(f"{hrac.jmeno} skončil na speciálním poli!")
            nova_pozice = self.hady_a_zebriky[nova_pozice]

        
        if nova_pozice in self.pozice_hracu and self.pozice_hracu[nova_pozice] is not None:
            jiny_hrac = self.pozice_hracu[nova_pozice]
            print(f"{hrac.jmeno} narazil do {jiny_hrac.jmeno}! Pohybuji {jiny_hrac.jmeno} zpět na pozici {nova_pozice - 1}")
            jiny_hrac.pozice = max(1, jiny_hrac.pozice - 1)
            self.pozice_hracu[nova_pozice] = jiny_hrac
            print(f"{jiny_hrac.jmeno} byl posunut o jedno pole zpět!")

            # Kontrola, zda je pole volné
            if jiny_hrac.pozice in self.hady_a_zebriky:
                print(f"{jiny_hrac.jmeno} přistál na speciálním poli! Specialni pole!")
                jiny_hrac.pozice = self.hady_a_zebriky[jiny_hrac.pozice]

        # Nová pozice
        hrac.pozice = min(nova_pozice, self.velikost_desky)
        self.pozice_hracu[stara_pozice] = None # pozice je nyní volná
        self.pozice_hracu[hrac.pozice] = hrac

    def tah_hrace(self, hrac):
        soucet_hodu_kostkou = 0

        while True:
            input(f"Stiskněte Enter pro hod kostkou pro {hrac.jmeno}...")
            hod_kostkou = random.randint(1, 6)

            print(f"{hrac.jmeno} hodil {hod_kostkou}")

            if hod_kostkou == 6:
                print(f"{hrac.jmeno} hodil 6! Hází znovu...")
                soucet_hodu_kostkou += hod_kostkou
            else:
                soucet_hodu_kostkou += hod_kostkou
                break

        nova_pozice = hrac.pozice + soucet_hodu_kostkou

        # Kontrola, zda hod hráče nepřesáhl velikost hrací plochy
        if nova_pozice > self.velikost_desky:
            print(f"{hrac.jmeno} hodil příliš vysoké číslo, smolík. Přeskočení tohoto tahu.")
            return

        # Pohyb hráče a kontrola hadů, žebříků, kolizí a speciálních polí
        self.pohyb_hrace(hrac, soucet_hodu_kostkou)

        # Kontrola, zda je hráč nyní na speciálním poli po pohybu
        if hrac.pozice in self.hady_a_zebriky:
            print(f"{hrac.jmeno} přistál na speciálním poli! Specialni pole!")
            self.pohyb_hrace(hrac, 0)  # Znovu zavolej pohyb_hrace s 0 kroky pro kontrolu speciálního pole

        # Kontrola, zda hráč stál na posledním poli
        if hrac.pozice == self.velikost_desky:
            print(f"{hrac.jmeno} vyhrál!")
            exit()

        # Aktualizace pozice hráče
        print(f"{hrac.jmeno} je nyní na pozici {hrac.pozice}")

if __name__ == "__main__":
    pocet_hracu = int(input("Zadejte počet hráčů: "))
    hra = HadyAZebrikyHra(pocet_hracu)

    while True:
        print("*" * 20) 
        for hrac in hra.hraci:
            hra.tah_hrace(hrac)
