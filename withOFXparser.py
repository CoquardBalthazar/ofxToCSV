from ofxparse import OfxParser
import csv

with open(r"data\Extrato31232179272.ofx") as fileobj:
    ofx = OfxParser.parse(fileobj)


lst_operacoes = []

for i in ofx.account.statement.transactions:
    lst_operacoes.append(
        {
            "payee": i.payee,
            "type": i.type,
            "date": i.date,
            "user_date": i.user_date,
            "amount": f"{i.amount}".replace(".", ","),
            "id": i.id,
            "memo": i.memo,
            "sic": i.sic,
            "mmc": i.mcc,
            "checksum": i.checknum,
        }
    )


colunas = [
    "payee",
    "type",
    "date",
    "user_date",
    "amount",
    "id",
    "memo",
    "sic",
    "mmc",
    "checksum",
]

# use latin-1 ou iso-8859-1 para windows
# use utf-8 para linux e mac
with open(r"data/extrato.csv", "w", encoding="latin-1", newline="") as filecsv:
    writer = csv.DictWriter(filecsv, fieldnames=colunas, dialect="excel")
    writer.writeheader()
    writer.writerows(lst_operacoes)
