import csv
import json
import os


def jsontojsonl(file, output_file):
    with open(file) as json_file:
        JSON_file = json.load(json_file)

    with open(output_file, 'w') as outfile:
        for key, val in JSON_file.items():
            entry = {"file_name": key, "text": val}
            json.dump(entry, outfile)
            outfile.write('\n')


def csvtojsonl(file, output_file):
    with open(file, 'r') as f:
        reader = csv.reader(f)
        amr_csv = list(reader)

    with open(output_file, 'w') as outfile:
        for line in amr_csv:
            entry = {"file_name": line[0], "text": line[1]}
            json.dump(entry, outfile)
            outfile.write('\n')

