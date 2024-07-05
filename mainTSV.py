import csv

def tsv_to_csv(input_file, output_file):
    encodings = ["utf-8","latin-1","utf-16"]
    for encoding in encodings :
        try :
            with open(input_file, 'r', newline='', encoding=encoding) as tsvfile:
                reader = csv.reader(tsvfile, delimiter='\t')
                with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile)
                    for row in reader:
                        writer.writerow(row)
            print(f"Conversion completed using encoding: {encoding}")
            break
        except UnicodeDecodeError:
                print(f"Failed to decode using encoding : {encoding}")

# Example usage:
input_file = 'data/tsv/20240517-90j-Mai-20242143295S0381715941047419.tsv'
output_file = 'output/ConverterTSV_20240517-90j-Mai-20242143295S0381715941047419.csv'
tsv_to_csv(input_file, output_file)




# PROBLEM To Solve : 
# - Integer column from Transaction is not as integer but as text printed