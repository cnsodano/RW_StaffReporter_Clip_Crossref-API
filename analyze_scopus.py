""" Use to find number of self citations in a Scopus citation report exported csv""" 
import pandas as pd
AUTHOR: str = "Verma"

df = pd.read_csv("scopus.csv")
temp = df["Authors"].copy()
for index in df["Authors"].index:
    temp[index] = AUTHOR in df["Authors"][index]
sum(temp)
print("Num of self-citations = " + str(temp))
breakpoint()
