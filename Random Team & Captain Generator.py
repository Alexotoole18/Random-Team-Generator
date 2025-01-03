import random
players = ["Alex", "Jack", "Jeff", "Sharon", "Woody", "Luna", "Lee", "Jordan", "Gerry", "Michael", "Joseph", "Gary", "Stephen", "Simon", "Ethan", "Tobi", "JJ", "Harold", "Anthony", "Josh", "Ben", "Aaron","James", "John", "Paul", "Billy", "Barry", "Craig", "Tom", "Dave"]
print("Welcome to Team Allocator!")
while True:
     random.shuffle(players)
     team1 = players[:len(players)//3]
     print("team 1 captain: " + random.choice(team1))
     print("team 1:")
     for player in team1:
         print(player)
     team2 = players[len(players)//3: (len(players)//3)*2]
     print("\nTeam 2 captain: " + random.choice(team2))
     print("team 2:")
     for player in team2:
         print(player)
     team3 = players[(len(players)//3)*2:]
     print("\nTeam 3 captain: " + random.choice(team3))
     print("Team 3:")
     for player in team3:
         print(player)
     response = input("Pick teams again? Type y or n: ")
