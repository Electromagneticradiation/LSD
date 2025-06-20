import csv
def txt_to_csv(txtpath,csvpath) :

    # with ensures file gets closed
    with open(txtpath, "r", encoding = "utf-8") as txt_file, open(csvpath, "w", newline = "", encoding = "utf-8") as csv_file :
        writer = csv.writer(csv_file)
        for line in txt_file :
            writer.writerow([line.strip()])

# to make sure code only runs upon file execution and NOT during imports
if __name__ == "__main__":

    print("Enter the path of input text file: ")
    # escape character in path must be replaced with / or \\
    txtpath = input().replace("\\","/")
    print("Enter the path of output csv file: ")
    csvpath = input().replace("\\","/")
    txt_to_csv(txtpath, csvpath) 
 