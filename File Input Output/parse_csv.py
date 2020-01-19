import csv

with open('names.csv', 'r') as csv_file:
	csv_reader = csv.DictReader(csv_file) #Read the file

	with open('new_names.csv' , 'w') as new_file:
		fieldnames = ['fist_name' , 'last_name'] #Write file
        
        csv_writer = csv.DictWriter(new_file , fieldnames=fieldnames, delimiter='\t')
		
		csv_writer.writeheader()

		for line in csv_reader:
			del line['email']
			#csv_writer.writerow(line)