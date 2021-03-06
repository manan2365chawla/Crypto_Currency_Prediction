import csv

#remove rate and last
#add attribute status

def remove_attribute(attr):
	f = open("results/dataset.csv")
	data = f.readlines()
	index_to_remove = 0
	print('removing attribute'+attr)
	data[0] = data[0].rstrip().split(",")
	for i in range(len(data[0])):
		if data[0][i]==attr:
			index_to_remove = i
			break
	return index_to_remove
	f.close()

def create_cleaned_dataset(indices_to_exclude):
	f = open("results/dataset.csv")
	data = f.readlines()
	o = open("results/cleaned_dataset.csv","w", newline='')
	writer = csv.writer(o)
	for line in data:
		line = line.rstrip().split(",")
		row = []
		for i in range(len(line)):
			if not i in indices_to_exclude:
				row.append(line[i])
		writer.writerow(row)
	f.close()
	o.close()

if __name__ == "__main__":
	attributes_to_remove = ['RATE','LAST','Timestamp']
	indices_to_remove = []
	for attr in attributes_to_remove:
		indices_to_remove.append(remove_attribute(attr))
	print(indices_to_remove)
	create_cleaned_dataset(indices_to_remove)
