import csv
from phonenumbers import parse, carrier
code = '+7'
ans = ''

def find(number):
    pN = parse(code + number)
    C = carrier.name_for_number(pN, 'ru')
    ans = code + number + ': ' + C + ', ' + geo(number)
    return ans

def geo(number):
    region=''
    with open("Numbers-Plan-9.csv", "r", encoding='utf-8') as f:
        reader = csv.reader(f, delimiter="\t")
        for i, line in enumerate(reader):
            if i != 0:
                if  line[0].split(";")[0] == number[:3] and [k for k in range(int(line[0].split(";")[1]), int(line[0].split(";")[2])) if int(number[3:]) == k]:
                    #prov = line[0].split(";")[4]
                    region = line[0].split(";")[5].strip()
    return region