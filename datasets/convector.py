import csv
import json


def convector(file_csv, file_json=None, model=None):

    with open(file_csv, encoding="utf-8") as csv_f:
        result = []
        for row in csv.DictReader(csv_f):
            del row['id']
            if 'price' in row:
                row['price'] = int(row['price'])
            if "is_published" in row:
                if row['is_published'] == "TRUE":
                    row['is_published'] = True
                else:
                    row['is_published'] = False
            result.append({'model': model, "fields": row})

    with open(file_json, 'w', encoding="utf-8") as json_f:
        json_f.write(json.dumps(result, ensure_ascii=False))


convector('categories.csv', 'categories.json', 'ads.category')
convector('ads.csv', 'ads.json', 'ads.ad')
