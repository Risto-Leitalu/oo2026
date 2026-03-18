from abc import ABC, abstractmethod

# liides
class Maksemeetod(ABC):
    @abstractmethod
    def maksa(self, summa: float):
        pass

# pangalingi klass
class Pangalink(Maksemeetod):
    def __init__(self, panga_nimi: str):
        self.panga_nimi = panga_nimi

    def maksa(self, summa: float):
        print(f"Tasutud {summa}€ kasutades {self.panga_nimi} pangalinki.")

# kinkekaardi klass
class Kinkekaart(Maksemeetod):
    def __init__(self, kood: str, jaak: float):
        self.kood = kood
        self.jaak = jaak

    def maksa(self, summa: float):
        if self.jaak >= summa:
            self.jaak -= summa
            print(f"Tasutud {summa}€ kinkekaardiga {self.kood}. Uus jääk: {self.jaak}€.")
        else:
            print(f"Viga: Kinkekaardil {self.kood} pole piisavalt saldot!")

# ostmise funktsioon
def soorita_ost(makseviis: Maksemeetod, summa: float):
    makseviis.maksa(summa)

if __name__ == "__main__":
    print("--- Ostukorvi vormistamine ---")
    
    # objektid
    swedbank = Pangalink("Swedbank")
    paypal = Pangalink("Paypal")
    kinkekaart = Kinkekaart("GIFT-2026-ABC", 50.0)

    # näidised
    soorita_ost(swedbank, 12.50)
    soorita_ost(paypal, 40)
    soorita_ost(kinkekaart, 20.0)
    soorita_ost(kinkekaart, 40.0)