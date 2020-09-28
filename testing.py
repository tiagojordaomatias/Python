import random
print('Hi')
n = int(input('Insert number of teams:'))
nTeams = n + 1

teams = []
games = []

i = 1
while i < nTeams:
    nameTeam = str(input('Insira o nome da Equipa {}'.format(i)))
    teams.append(nameTeam)
    i+=1

print(teams)

s = str(random.choice(teams))
teams.remove(s)
games.append(s)
print(games)
print(teams)
