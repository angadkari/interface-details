import csv

with open("interface-desc.txt",'r') as raw_desc:
	stripped  = (line.strip() for line in raw_desc)
	csv_line = (line.split(",") for line in new_line if line)
	with open('interface-desc.csv','w') as out_file:
		writer = csv.writer(out_file)
		writer.writerows(csv_line)
