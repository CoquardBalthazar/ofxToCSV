import subprocess
from ofxparse import OfxParser
import csv

def parse_ofx(file_path):
    with open(file_path,"rb") as fileobj:
        ofx = OfxParser.parse(fileobj)
        #Extract the necessary data
        #Process the data in the needed format

        # Extracting additional information
        account_number = ofx.account.number
        account_type = ofx.account.account_type
        account_currency = ofx.account.curdef
        date_created = ofx.account.statement.start_date
        account_balance = ofx.account.statement.balance

        # Extracting transaction data
        transactions = []

        for transaction in ofx.account.statement.transactions:
            # Extracting date, name, and amount from each transaction
            date = transaction.date.strftime("%d/%m/%Y")
            name = transaction.payee
            amount = transaction.amount

            # Appending extracted data as a tuple
            transactions.append((date, name, amount))
        
        return account_number, account_type, account_currency, date_created, account_balance, transactions

def write_to_csv(data, csv_file_path):
    account_number, account_type, account_currency, date_created, account_balance, transactions = data

    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, dialect="excel")

        # Writing additional information:
        writer.writerow(["Numéro Compte", account_number])
        writer.writerow(["Type", "CCP" if account_type == "CHECKING" else ""])
        writer.writerow(["Compte tenu en", account_currency])
        writer.writerow(["Date", date_created.strftime("%d/%m/%Y")]) #%d/%m/%Y   %Y/%m/%d
        writer.writerow(["Solde (EUROS)", str(account_balance)])

        # Writing header row
        writer.writerow([])
        writer.writerow(['Date', 'Name', 'Amount(EUROS)'])

        # Write data to the CSV file
        for row in data[5]:
            writer.writerow(row)

    #subprocess.call(['xpg-open', csv_file_path])

if __name__ == "__main__":
    
    # Replace 'input.ofx' and 'output.csv' with actual file paths
    ofx_file_path = 'data/input.ofx'
    csv_file_path = 'output.csv'

    # Step 1: Parse the OFX file
    parsed_data = parse_ofx(ofx_file_path)

    # Step 2: Write the parsed data to a CSV file
    write_to_csv(parsed_data, csv_file_path)

    print("Conversion complete.")
    


