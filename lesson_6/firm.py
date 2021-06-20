from pprint import pprint

#Firma
data = {
    "telefon": 0,
    "e-mail": 1,
    "position": 2,
    "cabinet number": 3,
    "skype": 4
}
firm = {
    "Joe Dhons": [+380508374145, "dhons.joe@gmail.com", "CEO", 1, "chef.joe"],
    "William Conqueror": [+380675793175, "conqueror.williwam@gmail.com", "commercial Director", 2, "conqueror.williwam"],
    "Evelyn Miller": [+380964873964, "evelyn.miller@gmail.com", "chief Financial Officer", 3, "evelyn.miller"],
    "Harper Lee": [+380981587008, "harper.lee@gmail.com", "writer", 4, "harper.lee"],
    "Mason Mount": [+380930014800, "mason.mountg@gmail.com", "manager", 5, "mason.mount"],
    "Ella Purnell": [+380631001002, "ella.purnell@gmail.com", "actress", 6, "ella.purnell"],
    }
pprint(firm)
pprint(firm["William Conqueror"][2])

# remove
del firm["William Conqueror"]
pprint(firm)

#search
pprint(firm["Ella Purnell"])
pprint(firm.get("Ella Purnell"))


#adding
new_firm = {
    "Scarlett Moffatt": [+380986673212, "scarlett.moffatt@gmail.com", "cleaning lady", 10, "scarlett.moffatt"]
} 
firm.update(new_firm)
pprint(firm)

#Replacing data
pprint(firm["Harper Lee"])
firm["Harper Lee"] = [+380934130093, "aleksandriv@ukr.net", "harper.lee@gmail.com", "writer", 4, "harper.lee"]
pprint(firm)