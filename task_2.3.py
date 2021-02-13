import csv
with open('stage3_test.csv', encoding='utf-8') as csvfile1:
    reader = csv.DictReader(csvfile1)
    with open('csv3.csv', 'w', encoding='utf-8') as csvfile2:
        fieldnames = ["Id", "Title", "Price"]
        writer = csv.DictWriter(csvfile2, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            writer.writerow({'Id': row['Id'], 'Title': row['Title'], 'Price': row['Price']})
