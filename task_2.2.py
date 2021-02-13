import csv
with open('stage3_test.csv', 'r', encoding='utf-8') as csvfile1:
    reader = csv.reader(csvfile1)
    with open('csv2.csv', 'w', encoding='utf-8') as csvfile2:
        fieldnames = ["Id", "Images", "Title", "Description", "Price"]
        writer = csv.DictWriter(csvfile2, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            if row[4] != 'Price':
                if 10000 < float(row[4]) < 50000:
                    writer.writerow({'Id': row[0], 'Images': row[1], 'Title': row[2], 'Description': row[3], 'Price': row[4]})
