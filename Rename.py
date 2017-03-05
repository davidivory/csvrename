#import function from openpyxl module
from openpyxl import load_workbook
#import Operating system into python
import os
#import Regular Expressions into python
import re
#import glob into python
import glob

#Where is your excel file
path_Excel ='/Users/davidivory/Desktop/'
#Where are the files you want to rename
path_Files ='/Users/davidivory/Desktop/Invoices/'

#open excel file. REPLACE Invoices.xlsx WITH THE NAME OF YOUR FILE
wb = load_workbook(filename = path_Excel+'Invoices.xlsx', data_only=True)
#What sheet is being worked on
sheet_ranges = wb['Sheet1']

#Rename files in this column
Orig_Col = 'F'

#with names from this column
New_Col = 'G'

#get directory
os.chdir(path_Files);
pdf_list=glob.glob('*.pdf')

re_transaction_number_from_cell = re.compile('[0-9]+')

x=1

while x>0:
	#this variable will iterate through F2-F64
	old_cell= Orig_Col+str(x+1)
	#this gets the value of the cell its focused on

	print(old_cell)
	old_cell_contents = sheet_ranges[old_cell].value
	print(old_cell_contents)

	if old_cell_contents is None:
		break

	print(old_cell_contents)

	old_cell_transaction_number = re_transaction_number_from_cell.search(old_cell_contents).group(0)

	print(old_cell_transaction_number)

	re_old_cell_transaction_number = re.compile("(.*)(" + old_cell_transaction_number + ")(.*)")

	resulting_file = "";

	for file_name in pdf_list:
		if (re_old_cell_transaction_number.match(file_name) is not None):
			resulting_file = file_name
			break

	if resulting_file == "":
		print('File not found')
		x=x+1
		continue

	old_name =resulting_file;

	print(old_name)

	#this variable will iterate through G2-G64
	new_cell = New_Col+str(x+1)
	#this gets the value of the cell its focused on
	new_name = sheet_ranges[new_cell].value

	os.rename(path_Files+old_name, path_Files+new_name+'.pdf')

	x=x+1

#When everything is done it will print a complete message
print("Renaming Done")




