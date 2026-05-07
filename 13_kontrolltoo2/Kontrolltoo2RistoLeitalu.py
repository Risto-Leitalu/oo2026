#Loogikaskeem

from abc import ABC, abstractmethod

class Lylitus(ABC):
    def __init__(self, nimi):
        self.nimi = nimi
        self.sisendid = {}
        self.valjund = None
        self.jargmine = None
        
    def yhenda(self, siht_lylitus, kanal):
        self.jargmine = (siht_lylitus, kanal)
        
    @abstractmethod
    def arvuta_valjund(self):
        pass
    
    def signaal(self, kanal, seisund):
        self.sisendid[kanal] = seisund
        uus_valjund = self.arvuta_valjund()
        
        print(f"Lülitus: {self.nimi}")
        print(f"  Sisendid: { {k: ('true' if v else 'false') for k, v in self.sisendid.items()}}")
        print(f"  Uus väljundseisund: {'teadmata' if uus_valjund is None else ('true' if uus_valjund else 'false')}")
        
        if uus_valjund is not None and uus_valjund != self.valjund:
            self.valjund = uus_valjund
            if self.jargmine:
                siht, siht_kanal = self.jargmine
                siht.signaal(siht_kanal, self.valjund)
        

class ANDLylitus(Lylitus):
    def arvuta_valjund(self):
        s1 = self.sisendid.get(1)
        s2 = self.sisendid.get(2)
        
        if s1 is False or s2 is False:
            return False
        if s1 is True and s2 is True:
            return True
        return None

class ORLylitus(Lylitus):
    def arvuta_valjund(self):
        s1 = self.sisendid.get(1)
        s2 = self.sisendid.get(2)
        
        if s1 is True or s2 is True:
            return True
        if s1 is False and s2 is False:
            return False
        return None

class NOTLylitus(Lylitus):
    def arvuta_valjund(self):
        s1 = self.sisendid.get(1)
        if s1 is None:
            return None
        return not s1
    
if __name__ == "__main__":
    and1 = ANDLylitus("AND-1")
    not1 = NOTLylitus("NOT-1")
    or1 = ORLylitus("OR-1")
    and2 = ANDLylitus("AND-2")
    not2 = NOTLylitus("NOT-2")

    and1.yhenda(or1, 1)
    not1.yhenda(or1, 2)
    or1.yhenda(and2, 1)
    not2.yhenda(and2, 2)

    print("1. Aktiveerin AND-1 esimese kanali:")
    and1.signaal(1, True)

    print("\n2. Aktiveerin NOT-1 sisendis:")
    not1.signaal(1, True)

    print("\n3. Aktiveerin AND-1 teise kanali:")
    and1.signaal(2, True)

    print("\n4. Aktiveerin NOT-2 sisendi:")
    not2.signaal(1, False)
