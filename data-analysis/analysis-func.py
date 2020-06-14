>>> import csv
>>> def initAnalysis(x):
	with open('modified.csv', 'w', newline='') as file:
		fieldnames = ['District Number', 'Number of Successful Responses', 'Total Number of Incidents', '% of Successful Responses', 'Average Number of Nearby CFVs']
		writer = csv.DictWriter(file, fieldnames=fieldnames)
		writer.writeheader()
		writer.writerow({'District Number': 3, 'Number of Successful Responses': 2, 'Total Number of Incidents': 10, '% of Successful Responses': 0.2, 'Average Number of Nearby CFVs': 0.75})
		writer.writerow({'District Number': 5, 'Number of Successful Responses': 7, 'Total Number of Incidents': 9, '% of Successful Responses': 77.8, 'Average Number of Nearby CFVs': 2.3})
		writer.writerow({'District Number': 18, 'Number of Successful Responses': 4, 'Total Number of Incidents': 8, '% of Successful Responses': 50, 'Average Number of Nearby CFVs': 1.4})
		writer.writerow({'District Number': 20, 'Number of Successful Responses': 8, 'Total Number of Incidents': 12, '% of Successful Responses': 66.7, 'Average Number of Nearby CFVs': 1.8})
		writer.writerow({'District Number': 22, 'Number of Successful Responses': 0, 'Total Number of Incidents': 6, '% of Successful Responses': 0, 'Average Number of Nearby CFVs': 0.5})
		writer.writerow({'District Number': 27, 'Number of Successful Responses': 3, 'Total Number of Incidents': 5, '% of Successful Responses': 0.6, 'Average Number of Nearby CFVs': 1.2})
	return

>>> # function used for demo to refine data from incident-stats-scdf.csv to create modified.csv
>>> # only applicable to this dataset for THIS DEMO.
