import openpyxl
wins = 0
gamenum = 0

wookbook = openpyxl.load_workbook("Dataset.xlsx")
worksheet = wookbook.active

for i in range(1, worksheet.max_row):
    for col in worksheet.iter_cols(2, 4):
        print(col[i].value, end="\t\t")

        if col[i].value == "Победа":
            wins = 1
            print(wins, end="\t")
    ##if col[2].value = col[2].value :
   #     ffd
    print('')
print()