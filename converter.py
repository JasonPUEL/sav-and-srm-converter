
import os, sys



def sav_to_srm(file_name):
	with open(file_name, 'rb') as sav_file:
		conv = sav_file.read()

	for i in range(16384):
		conv += b'f'

	with open(file_name[:-3]+'srm', 'wb') as srm_file:
		srm_file.write(conv)
            
def srm_to_save(file_name):
    with open(file_name, 'rb') as srm_file:
        conv = srm_file.read()

    with open(file_name[:-3]+'sav', 'wb') as sav_file:
        sav_file.write(conv[:-16384])
		
def converter(file):
    if file[-4:] == '.srm':
        print('Identified as .SRM file\nConverting')
        srm_to_save(file)
        print('Converted to .SAV file')

    elif file[-4:] == '.sav':
        print('Identified as .SAV file\nConverting')
        sav_to_srm(file)
        print('Converted to .SRM file')
    else:
        print('File type not recognised')

#===================================================================

if __file__ == '__main__': 
    try:
        file = sys.argv[1]
    except IndexError:
        file = input('File path from dictionary ['+os.getcwd()+']: ')

    converter(file)

