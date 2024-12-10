mijn_lijst = [220, 430, 125, 160, 205, 90, 345]

def aanbieding_1(smaak, prijs, korting):
    print(f"Vandaag in de aanbieding: emmertje ijs(1 liter) in de smaak {smaak},van {prijs} voor {prijs * 1-korting} euro.")
    
def inkomsten_totaal(ma, di, wo, do, vr, za, zo, btw):
    totaal = ma+di+wo+do+vr+za+zo
    btw = (totaal * (1+btw) -totaal)
    print(f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw} euro btw betaald dient te worden")
    
def laag_en_hoog(mijn_lijst):
    print(max(mijn_lijst))
    print(min(mijn_lijst))

