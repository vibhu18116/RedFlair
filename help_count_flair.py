import pandas as pd
import pprint

df = pd.read_csv("Extracted_data_red.csv")

# print(df)
d = dict()

count = 0

for i in df.loc[:,"flair"]:
	# print(i)
	count+=1

	if i in d:
		d[i] += 1

	else:
		# print(i)
		d[i] = 1


pprint.pprint(d)
print(count)