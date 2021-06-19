# Basketball players
from pprint import pprint
Basketball_players = {
    "LeBron James": 195,
    "Michael Jordan": 198,
    "Magic Johnson": 191,
    "Wilt Chamberlain": 201,
    "Oscar Robertson": 195
}
# add new pleyer
new_players = {
    "Bill Russell": 194,
}
Basketball_players.update(new_players)
pprint(Basketball_players)

# remove player

del Basketball_players ["Magic Johnson"]
pprint(Basketball_players)

