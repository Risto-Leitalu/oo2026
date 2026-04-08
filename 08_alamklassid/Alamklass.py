class Seade:
    def __init__(self, tootja, mudel):
        self.tootja = tootja
        self.mudel = mudel
        self._on_sees = False

    def lülita_sisse(self):
        self._on_sees = True
        print(f"{self.tootja} {self.mudel} on nüüd sees.")

    def lülita_välja(self):
        self._on_sees = False
        print(f"{self.tootja} {self.mudel} on välja lülitatud.")

    def __str__(self):
        return f"Seade: {self.tootja} {self.mudel}"


class Arvuti(Seade):
    def __init__(self, tootja, mudel, protsessor):
        super().__init__(tootja, mudel)
        self.protsessor = protsessor

    def käivita_programm(self, programmi_nimi):
        if self._on_sees:
            print(f"Käivitan programmi {programmi_nimi} protsessoril {self.protsessor}...")
        else:
            print("Viga: Arvuti peab olema sisse lülitatud!")


class Sülearvuti(Arvuti):
    def __init__(self, tootja, mudel, protsessor, aku_vastupidavus):
        super().__init__(tootja, mudel, protsessor)
        self.aku_vastupidavus = aku_vastupidavus

    def näita_andmeid(self):
        status = "Sees" if self._on_sees else "Väljas"
        print(f"Sülearvuti: {self.tootja} {self.mudel} | Protsessor: {self.protsessor} | "
              f"Aku: {self.aku_vastupidavus}h | Olek: {status}")


class Nutitelefon(Seade):
    def __init__(self, tootja, mudel, ekraani_suurus):
        super().__init__(tootja, mudel)
        self.ekraani_suurus = ekraani_suurus

    def helista(self, number):
        if self._on_sees:
            print(f"Helistan numbril {number}...")
        else:
            print("Telefon on hetkel välja lülitatud")

if __name__ == "__main__":
    print("--- Elektroonika Haldussüsteem ---\n")

    # Loome sülearvuti objekti
    minu_lapa = Sülearvuti("Apple", "MacBook Air", "M2", 18)
    
    # Loome nutitelefoni objekti
    minu_telefon = Nutitelefon("Samsung", "Galaxy S23", 6.1)

    # Tegevused sülearvutiga
    minu_lapa.näita_andmeid()
    minu_lapa.lülita_sisse()
    minu_lapa.käivita_programm("Python IDE")
    
    print("-" * 30)

    # Tegevused telefoniga
    print(minu_telefon)
    minu_telefon.helista("555-0123")
    minu_telefon.lülita_sisse()
    minu_telefon.helista("555-0123")