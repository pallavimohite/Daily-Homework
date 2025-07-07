class Player:
    def __init__(self,name,jersey_no,runs,wicket,team):
        self.__name = name 
        self.__jersey_no = jersey_no
        self.__runs = runs 
        self.__wicket = wicket
        self.__team = team
        


    def get_name(self):
        return self.__name
    def set_name(self,newname):
        self.__name = newname

    def get_jersey_no(self):
        return self.__jersey_no
    def set___jersey_no(self,newjersey_no):   
        self.__jersey_no = newjersey_no

    def get_runs(self):
        return self.__runs
    def set_runs(self,newruns):
        self.__runs = newruns

    def get_wicket(self):
        return self.__wicket
    def set_wicket(self,newwicket):
        self.__wicket= newwicket

    def get_team(self):
        return self.__team
    def set_team(self,newteam):
        self.__team = newteam

p1 = Player("Rohit Sharma", 45, 6211, 1, "MI")
p2 = Player("Ishan Kishan", 32, 2322, 0, "MI")
p3 = Player("Suryakumar Yadav", 63, 3249, 0, "MI")
p4 = Player("Tilak Varma", 9, 740, 1, "MI")
p5 = Player("Tim David", 11, 741, 0, "MI")
p6 = Player("Cameron Green", 42, 452, 6, "MI")
p7 = Player("Jasprit Bumrah", 93, 56, 145, "MI")
p8 = Player("Piyush Chawla", 3, 609, 179, "MI")
p9 = Player("Jason Behrendorff", 65, 22, 29, "MI")
p10 = Player("Nehal Wadhera", 18, 241, 0, "MI")
p11 = Player("Arjun Tendulkar", 24, 27, 3, "MI")

p12 = Player("MS Dhoni", 7, 5082, 0, "CSK")
p13 = Player("Ruturaj Gaikwad", 31, 1797, 0, "CSK")
p14 = Player("Devon Conway", 88, 924, 0, "CSK")
p15 = Player("Moeen Ali", 18, 1033, 33, "CSK")
p16 = Player("Ravindra Jadeja", 8, 2692, 152, "CSK")
p17 = Player("Deepak Chahar", 90, 79, 72, "CSK")
p18 = Player("Matheesha Pathirana", 99, 10, 22, "CSK")
p19 = Player("Ambati Rayudu", 9, 4000, 0, "CSK")
p20 = Player("Ben Stokes", 55, 935, 29, "CSK")
p21 = Player("Shivam Dube", 25, 1375, 5, "CSK")
p22 = Player("Maheesh Theekshana", 58, 20, 23, "CSK")

p23 = Player("Virat Kohli", 18, 7263, 4, "RCB")
p24 = Player("Faf du Plessis", 18, 4133, 0, "RCB")
p25 = Player("Glenn Maxwell", 32, 2719, 29, "RCB")
p26 = Player("Dinesh Karthik", 19, 4516, 0, "RCB")
p27 = Player("Mohammed Siraj", 13, 97, 78, "RCB")
p28 = Player("Wanindu Hasaranga", 49, 120, 35, "RCB")
p29 = Player("Harshal Patel", 9, 182, 111, "RCB")
p30 = Player("Anuj Rawat", 66, 222, 0, "RCB")
p31 = Player("Shahbaz Ahmed", 21, 321, 15, "RCB")
p32 = Player("Karn Sharma", 33, 106, 63, "RCB")
p33 = Player("Rajat Patidar", 5, 318, 0, "RCB")

p34 = Player("Shubman Gill", 77, 2790, 0, "GT")
p35 = Player("Hardik Pandya", 33, 2309, 53, "GT")
p36 = Player("David Miller", 10, 2714, 0, "GT")
p37 = Player("Rahul Tewatia", 4, 738, 32, "GT")
p38 = Player("Wriddhiman Saha", 6, 2798, 0, "GT")
p39 = Player("Mohammed Shami", 11, 69, 127, "GT")
p40 = Player("Rashid Khan", 19, 313, 139, "GT")
p41 = Player("Alzarri Joseph", 44, 50, 20, "GT")
p42 = Player("Sai Sudharsan", 23, 572, 0, "GT")
p43 = Player("Vijay Shankar", 14, 1056, 9, "GT")
p44 = Player("Abhinav Manohar", 96, 197, 0, "GT")

p45 = Player("Shreyas Iyer", 41, 2776, 0, "KKR")
p46 = Player("Andre Russell", 12, 2262, 96, "KKR")
p47 = Player("Nitish Rana", 27, 2594, 7, "KKR")
p48 = Player("Rinku Singh", 35, 725, 0, "KKR")
p49 = Player("Venkatesh Iyer", 25, 953, 3, "KKR")
p50 = Player("Sunil Narine", 74, 1046, 163, "KKR")
p51 = Player("Varun Chakravarthy", 29, 23, 62, "KKR")
p52 = Player("Umesh Yadav", 19, 163, 136, "KKR")
p53 = Player("Lockie Ferguson", 87, 36, 37, "KKR")
p54 = Player("Rahmanullah Gurbaz", 21, 227, 0, "KKR")
p55 = Player("Harshit Rana", 20, 12, 11, "KKR")

#List of all team
MI_Team=[]
CSK_Team = []
RCB_Team = []
GT_Team = []
KKR_Team = []

all_teams = [MI_Team,CSK_Team,RCB_Team,GT_Team,KKR_Team]

#Insert Data into list
MI_Team.append(p1)
MI_Team.append(p2)
MI_Team.append(p3)
MI_Team.append(p4)
MI_Team.append(p5)
MI_Team.append(p6)
MI_Team.append(p7)
MI_Team.append(p8)
MI_Team.append(p9)
MI_Team.append(p10)
MI_Team.append(p11)

CSK_Team.append(p12)
CSK_Team.append(p13)
CSK_Team.append(p14)
CSK_Team.append(p15)
CSK_Team.append(p16)
CSK_Team.append(p17)
CSK_Team.append(p18)
CSK_Team.append(p19)
CSK_Team.append(p20)
CSK_Team.append(p21)
CSK_Team.append(p22)

RCB_Team.append(p23)
RCB_Team.append(p24)
RCB_Team.append(p25)
RCB_Team.append(p26)
RCB_Team.append(p27)
RCB_Team.append(p28)
RCB_Team.append(p29)
RCB_Team.append(p30)
RCB_Team.append(p31)
RCB_Team.append(p32)
RCB_Team.append(p33)

GT_Team.append(p34)
GT_Team.append(p35)
GT_Team.append(p36)
GT_Team.append(p37)
GT_Team.append(p38)
GT_Team.append(p39)
GT_Team.append(p40)
GT_Team.append(p41)
GT_Team.append(p42)
GT_Team.append(p43)
GT_Team.append(p44)


KKR_Team.append(p45)
KKR_Team.append(p46)
KKR_Team.append(p47)
KKR_Team.append(p48)
KKR_Team.append(p49)
KKR_Team.append(p50)
KKR_Team.append(p51)
KKR_Team.append(p52)
KKR_Team.append(p53)
KKR_Team.append(p54)
KKR_Team.append(p55)

#for players in MI_Team:
print("Name:", p1.get_name())
print("jersey_no:",p1.get_jersey_no())
print("Runs:",p1.get_runs())
print("Wickets:",p1.get_wicket())

#Team name
for team in all_teams:
    for player in team:
        pass
    print(player.get_team())

#name and team
for team in all_teams:
    for player in team:
        print(f"Name of the player :{player.get_name()} and team is {player.get_team()}")

#Analysis for finding best runner
for team in all_teams:
    for player in team:
        if player.get_runs() > 2000:
            print("Players having more than 2000 runs")
            print(player.get_name(),"Completed",player.get_runs(),"Runs")

for team in all_teams:
    for player in team:
        if player.get_runs() > 3000:
            print("Players having more than 3000 runs")
            print(player.get_name() ,"Completed" ,player.get_runs(),"Runs")


for team in all_teams:
    for player in team:
        if player.get_runs() > 7000:
            print("Players having more than 7000 runs")
            print(player.get_name(),"Completed", player.get_runs(),"and he is best runner")

#Best Bowler
for team in all_teams:
    for player in team:
        if player.get_wicket() > 100:
            print(player.get_name())

for team in all_teams:
    for player in team:
        if player.get_wicket() > 150:
            print(player.get_name(), "has more rhan 150 wickets")
            print(player.get_wicket())
        

for team in all_teams:
    for player in team:
        if player.get_wicket() > 170 and player.get_wicket()<180:
            print(player.get_name()," is the Bestest Bowller")
        elif player.get_wicket() > 160 and player.get_wicket()<170:
             print(player.get_name()," is the Second Best Bowller")
        elif player.get_wicket() > 150 and player.get_wicket() < 160:
             print(player.get_name()," is the Third Best Bowller")
        else:
            pass

#All Rounder Player
for Team in all_teams:
    for player in Team:
        if player.get_runs()>2000 and player.get_wicket() > 20:
            print(f"{player.get_name()} is a all roundder Player")
        


























