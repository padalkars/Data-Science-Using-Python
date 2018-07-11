from collections import Counter
import pandas as pd
import math

Statement_1 = "Cracking the Coding Interview, 6th Edition is here to help you through this process, teaching you what you need to know and enabling you to perform at your very best."
Statement_2 = "I have coached and interviewed hundreds of software engineers."
Statement_3 = "The result is this book."

Statements = [Statement_1, Statement_2, Statement_3]
ind = ['Statement 1', 'Statement 2', 'Statement 3']

result_set = set()
row = {}
for stm,i in zip(Statements,ind):
	if(stm not in row.keys()):
		row[i] = dict(Counter(stm.lower().strip(',').split(' ')))	
	
	if(not result_set):
				
		for ele in stm.lower().split(' '):
			result_set.add(ele)
		continue
	result_set = result_set.union(set(stm.lower().strip(',').split(' ')))

		
column = list(result_set)

#Create an empty data frame
df = pd.DataFrame(index=ind, columns=column)

#Filling the Data Frame 
for col in column:
	for key in row.keys():
		if(col in row[key].keys()):
			df.loc[key][col] = row[key][col]
		else:
			df.loc[key][col] = 0
print(df)

   
