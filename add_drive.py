import csv

def create_csv():

	with open('persons.csv', 'w') as csvfile:
	    filewriter = csv.writer(csvfile, delimiter=',',
	                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
	    filewriter.writerow(['Name', 'Day'])