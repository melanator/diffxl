import argparse
from pathlib import Path
from openpyxl import load_workbook, Workbook
from colorama import Fore, Style

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("file_1", help="First excel file")
    parser.add_argument("file_2", help="Second excel file")
    parser.add_argument("-v", "--verbose", help="Verbose mode", action="store_true")
    args = parser.parse_args()

    file1, file2 = Path(args.file_1), Path(args.file_2)

    # Check if first path exists
    if not file1.exists():
        print("The first target file does not exists")
        raise SystemExit(1)
    
    # Check if second path exists
    if not file2.exists():
        print("The second target file does not exists")
        raise SystemExit(1)
    
    # Check if path are the same
    if file1 == file2:
        print("You selected the same workbooks\nExit")
        return SystemExit(2)

    compare(load_workbook(file1), load_workbook(file2))
        

def compare(wb1: Workbook, wb2: Workbook):  
    if(wb1 == wb2):
        print("Workbooks are the same")
        return 0

    print(wb1.sheetnames)
    print(wb2.sheetnames)
    print(Fore.RED + str(set(wb1.sheetnames) - set(wb2.sheetnames)))
    print(Style.RESET_ALL)


class Difference:
    pass

if __name__ == "__main__":
    main()
