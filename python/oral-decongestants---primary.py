# Tim Doran, Evangelos Kontopantelis, Jose M Valderas, Stephen Campbell, Martin Roland, Chris Salisbury, David Reeves, 2023.

import sys, csv, re

codes = [{"code":"10001","system":"gprdproduct"},{"code":"10411001","system":"gprdproduct"},{"code":"10564001","system":"gprdproduct"},{"code":"10732001","system":"gprdproduct"},{"code":"10820001","system":"gprdproduct"},{"code":"10890001","system":"gprdproduct"},{"code":"10890002","system":"gprdproduct"},{"code":"10929001","system":"gprdproduct"},{"code":"10972001","system":"gprdproduct"},{"code":"11468001","system":"gprdproduct"},{"code":"11596001","system":"gprdproduct"},{"code":"11618001","system":"gprdproduct"},{"code":"12177001","system":"gprdproduct"},{"code":"12886001","system":"gprdproduct"},{"code":"12887001","system":"gprdproduct"},{"code":"1320001","system":"gprdproduct"},{"code":"1359001","system":"gprdproduct"},{"code":"14214001","system":"gprdproduct"},{"code":"1462001","system":"gprdproduct"},{"code":"1765001","system":"gprdproduct"},{"code":"186001","system":"gprdproduct"},{"code":"186002","system":"gprdproduct"},{"code":"246001","system":"gprdproduct"},{"code":"2481001","system":"gprdproduct"},{"code":"2484001","system":"gprdproduct"},{"code":"2571001","system":"gprdproduct"},{"code":"3143007","system":"gprdproduct"},{"code":"3167007","system":"gprdproduct"},{"code":"3581007","system":"gprdproduct"},{"code":"4010001","system":"gprdproduct"},{"code":"4629001","system":"gprdproduct"},{"code":"4629002","system":"gprdproduct"},{"code":"4629003","system":"gprdproduct"},{"code":"4631001","system":"gprdproduct"},{"code":"4632001","system":"gprdproduct"},{"code":"5437001","system":"gprdproduct"},{"code":"5437002","system":"gprdproduct"},{"code":"5611001","system":"gprdproduct"},{"code":"5611002","system":"gprdproduct"},{"code":"5686001","system":"gprdproduct"},{"code":"5689001","system":"gprdproduct"},{"code":"5689002","system":"gprdproduct"},{"code":"5689003","system":"gprdproduct"},{"code":"5691001","system":"gprdproduct"},{"code":"5691002","system":"gprdproduct"},{"code":"5706001","system":"gprdproduct"},{"code":"5909001","system":"gprdproduct"},{"code":"6643001","system":"gprdproduct"},{"code":"6699007","system":"gprdproduct"},{"code":"7354001","system":"gprdproduct"},{"code":"7361001","system":"gprdproduct"},{"code":"7361002","system":"gprdproduct"},{"code":"7712001","system":"gprdproduct"},{"code":"7921001","system":"gprdproduct"},{"code":"8019001","system":"gprdproduct"},{"code":"8082001","system":"gprdproduct"},{"code":"8528001","system":"gprdproduct"},{"code":"8794001","system":"gprdproduct"},{"code":"9001","system":"gprdproduct"},{"code":"9002","system":"gprdproduct"},{"code":"902001","system":"gprdproduct"},{"code":"902002","system":"gprdproduct"},{"code":"9169001","system":"gprdproduct"},{"code":"9278001","system":"gprdproduct"},{"code":"9287001","system":"gprdproduct"},{"code":"9616001","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('oral-decongestants-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["oral-decongestants---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["oral-decongestants---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["oral-decongestants---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
