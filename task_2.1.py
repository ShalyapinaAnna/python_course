import csv
with open('stage3_test.csv', encoding='utf-8') as csvfile1:
    reader = csv.DictReader(csvfile1)
    with open('csv1.csv', 'w', encoding='utf-8') as csvfile2:
        fieldnames = ["Id", "Images", "Title", "Description", "Price"]
        writer = csv.DictWriter(csvfile2, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            number = row["Images"].split(',')
            if len(number) > 3:
                writer.writerow(row)
