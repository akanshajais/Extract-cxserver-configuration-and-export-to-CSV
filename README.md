# Extract-cxserver-configuration-and-export-to-CSV
**This is my contribution For the microtask T331201: Extract cxserver configuration and export to CSV, The code in outreachy_contribution.py read all the .yaml files in the config directory of the cxserver repository, except for the files listed in the question. For each file, it reads the YAML data, extracts the supported language pairs, and appends them to the supported_pairs list and then stored it in csv file .The resulting CSV file will have the four columns specified in the code.**

**FLOW OF EXECUTION I FOLLOWED**
- The code defines an empty list supported_pairs to store the extracted language pairs.
- The code loops through each file in the config directory using os.listdir('config').
- The loop checks if the file ends with .yaml and is not in the list of ignored files defined by IGNORED_FILES.
- If the file is a handler file, i.e., it contains only a single language pair in the format "source_language_to_target_language", the code splits the string using _to_ and extracts the source and target languages, as well as the translation engine from the filename.
- If the file is not a handler file, the code reads the YAML data using yaml.safe_load() and loops through each language pair in the format {'source_language': ['target_language', ...], ...}.
- For each language pair, the code extracts the source and target languages, as well as the translation engine from the filename.
- The code appends each extracted language pair as a tuple to the supported_pairs list.
- Once all files have been processed, the code opens a new CSV file supported_pairs.csv for writing using open('supported_pairs.csv', 'w', newline='').
- The code creates a CSV writer object using csv.writer().
- The code writes the CSV header row ['source language', 'target language', 'translation engine', 'is preferred engine?'] using writer.writerow().
- The code writes all language pairs in the supported_pairs list to the CSV file using writer.writerows().

# Library Used

- PyYAML
