bigmovie_db = {}

#one dictionary
moviedb_2022 = {}
casting1 = ["RK","AB","MR","NJ"]
name1 = "Brahmhastra"
moviedb_2022[name1]=casting1
#print(moviedb_2022)
 
name2 = "Drishyam"
casting2 = ["AKN","TB","SS","AD"]
moviedb_2022[name2]=casting2
#print(moviedb_2022)
 
casting3 = ["SK","RK","SD","RKM","KL"]
name3 = "The Cashmir Files"
moviedb_2022[name3]=casting3
#print(moviedb_2022)

casting4 = ["AKN","AB","RR"]
name4 = "Gangubai Kathiawadi"
moviedb_2022[name4]=casting4
#print(moviedb_2022)


#dictionary ssecond
moviedb_2023 = {}
casting1 = ["RR","AK","MR","VJ"]
name1 = "Dunki"
moviedb_2023[name1]=casting1


casting2 = ["SKN","AB","SD"]
name2 = "Pathan"
moviedb_2023[name2]=casting2
 
casting3 = ["VM","RK","SD","RKM"]
name3 = "12th Fail"
moviedb_2023[name3]=casting3


casting4 = ["CM","EB","RD"]
name4 = "Openheimer"
moviedb_2023[name4]=casting4
#print(moviedb_2023)

#Dictionary third

moviedb_2024 = {}
casting1 = ["KA","VB","MR"]
name1 = "Bhul Bhulaiyan"
moviedb_2024[name1]=casting1


casting2 = ["TS","MC","Ps","RR"]
name2 = "Bade Miyan Chote Miyan"
moviedb_2024[name2]=casting2
 
casting3 = ["VM","RS","FD","RKM"]
name3 = "Wicked"
moviedb_2024[name3]=casting3


casting4 = ["CP","EB","RD"]
name4 = "Khel Khel Main"
moviedb_2024[name4]=casting4
#print(moviedb_2024)

#Dictionary 4th

moviedb_2025 = {}
casting1 = ["AK","AB","RD","JF"]
name1 = "Housfull5"
moviedb_2025[name1]=casting1


casting2 = ["SS","AB","SD"]
name2 = "War2"
moviedb_2025[name2]=casting2
 
casting3 = ["AK","RK","SD","RKM"]
name3 = "Kesari2"
moviedb_2025[name3]=casting3


casting4 = ["SM","JK","RD"]
name4 = "Param Sundari"
moviedb_2025[name4]=casting4
#print(moviedb_2025)

#one big dictionary
bigmovie_db[2022] = moviedb_2022
bigmovie_db[2023] = moviedb_2023
bigmovie_db[2024] = moviedb_2024
bigmovie_db[2025] = moviedb_2025
#print(bigmovie_db)

#Acess the cast of specific movie
print(bigmovie_db[2022]["Brahmhastra"])

#Print all the movie released 
for year in bigmovie_db:
    for movies in bigmovie_db[year]:
        print(movies)

#Print all the cast
for year in bigmovie_db:
    for movies in bigmovie_db[year]:
        print(bigmovie_db[year][movies])

#Check movie is present in that year or not
if "Housfull5" in bigmovie_db[2025]:            
    print("yes,movie is present")

#Print all the movie and their cast
for year in bigmovie_db:
    for movies,cast in bigmovie_db[year].items():
        print(movies,"---->",cast)
    

#find all movies that include specific actor
actor = "RD"
for year in bigmovie_db:
    for movie,cast in bigmovie_db[year].items():
        if actor in cast:
            print(movie)

# actor = "AB"
# for year in bigmovie_db:
#     for movie, cast in bigmovie_db[year].items():
#         if actor in cast :
#             print(movie,"---->",[year])

#Find actor in present in which movie

count = 0
actor = "AB"
for year in bigmovie_db:
    for cast in bigmovie_db[year].values():
         if actor in cast:
             count = count+1
print("Actor AB present in movie:",count,bigmovie_db[year])

#List movies with more than two actor
for year in bigmovie_db:
    for movie,cast in bigmovie_db[year].items():
        if len(cast)>2:
            print(movie)

#count of movie released in each year
for year in bigmovie_db:
    print(len(bigmovie_db[year]),"--->",year)