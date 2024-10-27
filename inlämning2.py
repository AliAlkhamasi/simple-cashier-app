import datetime
import time
import os

class Produkter:
    def __init__(self,produktid,namn,pris_typ,pris):
        self.produktid = produktid
        self.namn = namn
        self.pris_typ = pris_typ
        self.pris = pris

class Kassasystem:
    def __init__(self):
        self.produkter = self.varor("Produkter.txt")
        self.kundkorg = []

    def varor(self, filnamn):
        produkter = []
        try:
            with open(filnamn, "r") as file:
                for line in file:
                    produktid, namn, pris_typ, pris = line.strip().split(",")
                    produkter.append(Produkter(int(produktid), namn, pris_typ, int(pris)))
        except FileNotFoundError:
            print(f"Filen {filnamn} hittades inte.")
        return produkter
   
    def ny_kund(self):
        print("Ny kund!")
        self.kundkorg = []
   
    def lägg_till_vara(self,produktid,antal):
        produkt = None
        for prod in self.produkter:
            if prod.produktid == produktid: 
                produkt = prod
                break
           
        if produkt:
            self.kundkorg.append((produkt, antal))
            print(f"lagt till {antal} av {produkt.namn}")
        else:
            print(f"{produktid} finns inte")


    def betala(self): 
        if not self.kundkorg:
            print("Kundkorgen är tom! Finns inget att betala")
            
       
        total_summa = 0
        print("Kvitto: ")
        print("-" * 20)
        for produkt,antal in self.kundkorg:
            kostnad = produkt.pris * antal
            total_summa += kostnad
            print(f"{produkt.namn} {antal}{produkt.pris_typ} {produkt.pris}kr/{produkt.pris_typ}")
            
        print(f"Totalsumma: {total_summa}SEK")
        print("-" * 20)
        self.spara_kvitto(total_summa)


    def spara_kvitto(self,total_summa):
       
        datum = datetime.datetime.now().strftime("%Y%m%d")
        fil_namn = f"KVITTO_{datum}.txt"
        with open(fil_namn,"a") as file:
            file.write("\n--- Nytt Kvitto ---\n")
            for produkt, antal in self.kundkorg:
                file.write(f"{produkt.namn} ({produkt.pris_typ}) - {antal} x {produkt.pris}")
            file.write(f"Totalsumma: {total_summa}SEK\n")
            file.write("--- Slut på kvittot ---\n\n")
        print(f"Kvittot sparat till filen: {fil_namn}")

def meny():
    kassa = Kassasystem()

    while True:
        print("MENY")
        print("1.Ny kund")
        print("2.Avsluta")
        val = input("Vänligen gör ett val: ")
        if val == "1":
            kassa.ny_kund()
            while True:
                choice = input("kommandon:\n <produktid> <antal>\n PAY\n kommando: ")
                if choice == "PAY":
                    kassa.betala()
                    time.sleep(1)
                    return
 
                else:
                    try:
                        produktid, antal = choice.split() 
                        kassa.lägg_till_vara(int(produktid), int(antal)) 
                    except ValueError:
                        print("Felaktig kommande ange som: 300 2 (produktid, antal)")
        if val == "2":
            print("Kassan avslutas!")
            break
        else:
            print("Felaktig inmatning, ange 1 eller 2")
            time.sleep(1)
            os.system("cls")
           
meny()





