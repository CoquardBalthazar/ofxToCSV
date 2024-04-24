import subprocess
from ofxparse import OfxParser
import csv

#print(dir(subprocess))

with open("data/input.ofx","rb") as fileobj:
    ofx = OfxParser.parse(fileobj)
account = ofx.account.statement.transactions[0].id
print(dir(account))
print(str(account))
