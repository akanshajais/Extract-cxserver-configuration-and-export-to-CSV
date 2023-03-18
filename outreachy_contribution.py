import os
import yaml
import csv

supported_pairs = []

for filename in os.listdir(r'C:\Users\AKANSHA\Downloads\contribution\config'):
    if not filename.endswith('.yaml'):
        continue
    if filename in ['MWPageLoader.yaml', 'languages.yaml', 'JsonDict.yaml', 'Dictd.yaml', 'mt-defaults.wikimedia.yaml']:
        continue

    with open(f'C:/Users/AKANSHA/Downloads/contribution/config/{filename}') as f:
        config = yaml.safe_load(f)

        if isinstance(config, str):  # handler case
            parts = config.split('_to_')
            source_lang = parts[0]
            target_lang = parts[1]
            supported_pairs.append((source_lang, target_lang, filename[:-5], False))
        else:  # regular case
            for source_lang, target_langs in config.items():
                for target_lang in target_langs:
                    supported_pairs.append((source_lang, target_lang, filename[:-5], False))

with open('supported_pairs.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['source language', 'target language', 'translation engine', 'is preferred engine?'])
    writer.writerows(supported_pairs)
