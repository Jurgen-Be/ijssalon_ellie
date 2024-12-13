def decoreer(tekst=""):
    lengte = len(tekst) + 4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()
    
def fooi_pp(bedrag, personen):
    
    try:
        bedrag_pp = bedrag /personen
        
    except:
        bedrag_pp = "??"
        
    uitvoer = (f"Het bedrag van de fooi is {bedrag_pp} euro per persoon")
    return uitvoer
    
def onderstreep(tekst=""):
    uit = []
    uit.append(tekst)
    tekens =""
    for teken in tekst:
        teken = "="
        tekens += teken
    uit.append(tekens)
    return uit

def som(inkomsten = {}):
    totaal = 0
    for value in inkomsten.values():
        totaal += value
    return totaal