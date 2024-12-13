mijn_dict = {"vis": 10, "vlees": 25, "overig" : 15}
totaal = 50

def presenteer(mijn_dict = {}, totaal = 0):
    for key, value in mijn_dict.items():
        print (f"{key} : {value} euro")
    print ("===================")
    print (f"Totaal {totaal} euro")
             