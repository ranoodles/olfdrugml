import csv

zinc_ids = set()
with open('postTests/results.csv', 'r') as f:
    for line in f:
        line = line.strip()
        if line:
            zinc_ids.add(line)

smiles_list = []
with open('postTests/maestroResults.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        title = row['title'].strip()
        if title in zinc_ids:
            smiles = row['SMILES'].strip()
            smiles_list.append([smiles]) 

with open('smiles_output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for smiles in smiles_list:
        writer.writerow(smiles)
