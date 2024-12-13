# Import modules
from algemene_functies import mijn_functie_2

mijn_lijst = [220, 430, 125, 160, 205, 90, 345]
invoer_lijst = [10,5,3,2,1,2,9]
invoer_lijst_2 = []

def aanbieding_1(smaak, prijs, korting):
    uitvoer = (f"Vandaag in de aanbieding: emmertje ijs(1 liter) in de smaak {smaak},van {prijs} voor {prijs * 1-korting} euro.")
    return uitvoer
    
def inkomsten_totaal(inkomsten, btw):
    totaal = 0
    for bedrag in inkomsten:
    totaal += bedrag
    btw_bedrag = totaal * btw
    uitvoer = f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag} euro btw betaald dient te worden."
    return uitvoer
    
def laag_en_hoog(mijn_lijst):
    return [max(mijn_lijst), min(mijn_lijst)]

def gemiddelde(mijn_lijst):
    bedrag= (sum(mijn_lijst)/7)
    return(f"De gemiddelde inkomsten deze week zijn {bedrag} euro.")

def meervoudig(invoer_lijst):
    return(laag_en_hoog(invoer_lijst))
    
def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer