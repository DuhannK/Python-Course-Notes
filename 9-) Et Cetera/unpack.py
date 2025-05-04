def total(galleons, sickles, knuts):
    return(galleons * 17 + sickles) * 29 + knuts

coins = {5"galleons": 100, "sickles": 50, "knuts": 2}
print(total(**coins), "Knuts")
