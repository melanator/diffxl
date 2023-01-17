import sys
from openpyxl import load_workbook
from colorama import Fore, Style

def main():
    if len(sys.argv) == 1:
        print("No excel files")
        return 0

    elif len(sys.argv) == 2:
        print("Specify the second file")
        return 0

    else:
        first_excel = load_workbook(sys.argv[1])
        second_excel = load_workbook(sys.argv[2])\
        
        if(first_excel == second_excel):
            print("Workbooks are the same")
            return 0

        print(first_excel.sheetnames)
        print(second_excel.sheetnames)
        print(Fore.RED + str(set(second_excel.sheetnames) - set(first_excel.sheetnames)))
        print(Style.RESET_ALL)

class Compare:
    pass

if __name__ == "__main__":
    main()
