#Kaalutud Keskmine

#Esimene ülesanne
def arvuta_kahe_aine_kaalutud_keskmine(h1, ap1, h2, ap2):
    keskmine = (h1 * ap1 + h2 * ap2) / (ap1 + ap2)
    return keskmine

#Näide, kus on esimene hinne 5(ehk A) ning 3(ehk C) ning nende ainepunktid 6 ja 3:
print(f"Kahe aine keskmine on: {arvuta_kahe_aine_kaalutud_keskmine(5, 6, 3, 3):.2f}")

#Teine Ülesanne
class OpilaseAndmed:
    def __init__(self):
        self.ained = []

    def lisa_aine(self, hinne, ainepunktid):
        self.ained.append({'hinne': hinne, 'ap': ainepunktid})

    def arvuta_kaalutud_keskmine(self):
        if not self.ained:
            return 0
        summa_toode = sum(a['hinne'] * a['ap'] for a in self.ained)
        summa_ap = sum(a['ap'] for a in self.ained)
        return summa_toode / summa_ap

#Kolmas ülesanne
def main():
    andmed = OpilaseAndmed()
    # Sõnastik, et muuta hinded numbriteks ristküliku jaoks
    hinded_dict = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1, 'F': 1}

    print("Kaalutud keskmise arvutaja")
    print("Sisesta 'stop', et lõpetada sisestamine.\n")

    while True:
        sisend_hinne = input("Sisesta hinne (A-F): ").upper()
        
        # Kui kirjutab stop, siis peatab
        if sisend_hinne == 'STOP':
            print("Peatatud!")
            break
        
        # Kui ei kuulu sõnastikku, siis ei laseb uuesti sisestada
        if sisend_hinne not in hinded_dict:
            print("Vigane hinne! Proovi uuesti.")
            continue
        
        # Try ja except selleks, et saaks vigase sisestusega otsekohe tegeleda ilma, et kood katki läheks
        try:
            sisend_ap = int(input("Sisesta ainepunktid: "))
        
        # Kui ei ole int arv, siis ei lase sisestada.
        except ValueError:
            print("Vigane arv! Sisesta täisarv.")
            continue

        # Lisab andmed klassi sisse
        andmed.lisa_aine(hinded_dict[sisend_hinne], sisend_ap)

        # Keskmise leidja, mis ümardab 2. komakohani.
        print(f"\nJooksev kaalutud keskmine: {andmed.arvuta_kaalutud_keskmine():.2f}")

        # Ristküliku joonistamine hinde ja ainepunktide põhjal
        print(f"Aine joonis (Kõrgus: {hinded_dict[sisend_hinne]}, Laius: {sisend_ap}):")
        korgus = hinded_dict[sisend_hinne]
        for _ in range(korgus):
            print("#" * sisend_ap)
        print("----------------------------------")

if __name__ == "__main__":
    main()