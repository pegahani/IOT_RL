from xlrd import open_workbook
import numpy as np

__author__ = 'pegah'

class manage_AS:
    def get_CS(self, AS):
        book = open_workbook("WS-AS.xlsx", on_demand=True)
        sheet = book.sheet_by_index(0)
        CSs = []
        for r in range(sheet.nrows):
            row = sheet.row(r)
            if row[0].value == AS:
                t = row[1].value
                CSs.append(t)
        return CSs

    def get_AS_list(self):
        book = open_workbook("AS.xlsx",on_demand=True)
        sheet = book.sheet_by_index(0)
        AS = set()

        for r in range(sheet.nrows):
            row = sheet.row(r)
            if row[1].value != "[AS]":
                AS.add(row[1].value)

        text_file = open("AS.txt", "w")
        text_file.write("{} \n".format("AS-ID AS"))

        AS_output = AS.copy()
        count = 0

        for i in xrange(len(AS)):
            text_file.write("{0} {1}\n".format(count, AS.pop()))
            count += 1

        text_file.close()

        return list(AS_output)

    def merge_text(self, file1, file2):

        text_file = open("tp-rt-merge.txt", "w")

        with open(file1) as f1, open(file2) as f2:
            for x, y in zip(f1, f2):
                text_file.write("{0} {1}\n".format(x.strip(), ((y.strip()).split())[3]))

        return

    def get_qos(self, service_ID, time_slice_ID):
        output = []
        file = "tp-rt-merge.txt"
        with open(file) as qos:
            for line in qos:
                words_list = line.split()
                if words_list[1] == service_ID and words_list[2] == time_slice_ID:
                    #response time and Throughput
                    QoS = words_list[3:5]
                    if QoS not in output:
                        output.append([np.float32(i) for i in QoS])
                    #output.append(words_list[3:5])

        return list(output)