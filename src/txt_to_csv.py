import csv

def txt_to_csv (txtpath,csvpath) :
    txt_file = open(txtpath, "r", encoding = "utf-8")
    csv_file = open(csvpath, "w")
    reader = txt_file.readline()
    writer = csv.writer(csv_file)
    while reader :
        writer.writerow([reader])
        reader = txt_file.readline()
    txt_file.close()
    csv_file.close()

print ("Enter the path of input text file: ")
txtpath = input()
print ("Enter the path of output csv file: ")
csvpath = input()
txt_to_csv(txtpath, csvpath)
