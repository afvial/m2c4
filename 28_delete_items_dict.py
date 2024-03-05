# Overview of the Multiple Methods for Deleting Items in a Python Dictionary

teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels":  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}

del teams['angels']
removed_team = teams.pop('mets', 'Team not found')

print(teams)
print(removed_team)
