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
print("With a new player:", Basketball_players)

# remove player

del Basketball_players ["Magic Johnson"]
print("Removed one player:", Basketball_players)

# search players

print(Basketball_players.get("Bill Russell"))

# Replacing data
print(Basketball_players["Wilt Chamberlain"])
Basketball_players["Wilt Chamberlain"] = 202
print(Basketball_players)
