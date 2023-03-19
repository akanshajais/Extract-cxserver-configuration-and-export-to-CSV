import yaml
import csv
import os

# Define list of files to ignore
IGNORED_FILES = ['MWPageLoader.yaml', 'languages.yaml',
                 'JsonDict.yaml', 'Dictd.yaml', 'mt-defaults.wikimedia.yaml']

# Define output CSV file name
OUTPUT_FILE = 'supported_language_pairs.csv'

# Define CSV header
CSV_HEADER = ['source language', 'target language',
              'translation engine', 'is preferred engine?']

# Define empty list to store language pairs
supported_pairs = []

# Parse all YAML files in the 'config' directory
for filename in os.listdir(r'C:/Users/AKANSHA/Downloads/contribution/config'):
    if filename not in IGNORED_FILES and filename.endswith('.yaml'):
        with open(f'C:/Users/AKANSHA/Downloads/contribution/config/{filename}') as f:
            config = yaml.safe_load(f)

            # Check for non-standard file structure with 'handler' key
            if isinstance(config, str):  # handler case
                parts = config.split('_to_')
                source_lang = parts[0]
                target_lang = parts[1]
                supported_pairs.append(
                                 (source_lang, target_lang, filename[:-5], False))
            else:
              # regular case
                for source_lang, target_langs in config.items():
                    for target_lang in target_langs:
                     supported_pairs.append(
                        (source_lang, target_lang, filename[:-5], False))
# Write language pairs to CSV file
with open(OUTPUT_FILE, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(CSV_HEADER)
    for pair in supported_pairs:
        writer.writerow(pair)
