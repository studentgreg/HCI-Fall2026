message = "Human-Computer Interaction"
print(message)
print(message[0]) # a string is several characters concatenated
print(message.upper())
print(message.lower())
print(3+10)
print("3"+"10")
# print(3+"10")
print(3*10)
print(3*"10")

# How to check the type
print(type(3.14))
print(type(True))
print(True + True)
print(len("Greg") == 7)
print(len("Greg") > 2)
print(len("FIU") <= 3)
print(False != 0)
print(type(3==6/2))

# Number and Arithmetics

a = 10
b = 3
print(a+b) # addition
print(b-a) # subtraction
print(a*b) # multiplication
print(a/b) # division
print(a//b) # floor division
print(a**b) # exponentiation
print(a ^ b) # XOR: 1010 ^ 0011 = 1001
print(a%b) # modulo - remainder of the division of 10 by 3
print(10 % 3) # 10 /3 = 3.333 => 3
print(-10 % 3) # -10 / 3 = -3.333 => -4 => -10 - (3*-4) = -10 + 12 = 2
x = 3
print(1 < x < 10)

# Lists
restaurants = ["Starbucks", "Vickys", "Chipotle", "McDonalds"]
print(restaurants[0])
print(restaurants[1])
print(restaurants[-1])
restaurants.append("Flanigans")
restaurants.append("El Toro Loco")
restaurants.extend(["Don Pan","Macondo","Panda Express"])
print(restaurants)
print(restaurants[1:4]) # accessing indices 1, 2, and 3
print(restaurants[2:]) # accessing from index 2 to the end
print(restaurants[:5]) # accessing from beginning to index 4
print(restaurants[::-1]) # reverse the list
print(restaurants)
print(restaurants[:])

print(len(restaurants))
print(restaurants.count("Starbucks"))
# Lists allow for duplicates - why? because elements are indexed
print(restaurants.index("Starbucks"))
y = restaurants.pop(0) # remove an element by index and potentially assigning it to a variable
print(y, restaurants)
restaurants.remove("McDonalds") # removing an element by its value
print(restaurants)
restaurants.reverse()
print(restaurants)
restaurants.sort()
print(restaurants)
restaurants.sort(reverse=True)
print(restaurants)

# Lists are used for multiple purposes including writing other data structures (like trees)

for i in restaurants:
    if len(i) > 7:
        print(i.upper())
    else:
        print(i.lower())

# TODO: create 3 lists, one with 3 tv shows as strings, one with year the show started,
#  one with the imdb rating of the show

shows = ["Spongebob", "Adventure Time", "Avatar: The Last Airbender", "Lantern"]
years = [1999, 2010, 2005, 2026]
ratings = [8.2, 8.7, 9.3, 10.0]

# In python, lists can be referenced by their variable name
tvShows = {
    "name" : shows,
    "years" : years,
    "ratings" : ratings
}

print(tvShows["name"])
print(tvShows["years"])
print(tvShows["ratings"])

# a dictionary is a collection of elements consisting of a key and a value

from pprint import pprint
pprint(tvShows)

# pandas is a library in python for data manipulation and analysis
import pandas as pd

df = pd.DataFrame(tvShows)
print(df)

"""
Notice that the data is stored in a table format.
Lists are now the columns
The keys of the dictionary are the column names (headers)
"""
print(df.columns)
print(df.describe()) # descriptive statistics of the numerical columns

import plotly.express as px # data visualization library

fig1 = px.bar(df, x="name", y="ratings")
fig1.show()

fig2 = px.line(df, x="name", y="ratings")
fig2.show()