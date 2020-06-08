import os,sys
from glob import glob
import pdfkit
from tqdm import tqdm


def getHTMLFiles(searchDirectiory):
    result = [y for x in os.walk(searchDirectiory) for y in glob(os.path.join(x[0], '*.html'))]
    return result

def main():
	# I/O
	cwd = os.getcwd()
	pagesLocation = cwd + '\\_site\\medholo\\2019\\' 
	pdfOutDir = cwd+'\\pdf\\'

	# Get all HTML Files
	htmlFiles = getHTMLFiles(pagesLocation)

	# Loop through and generate all the PDF Files
	for htmlFile in tqdm(htmlFiles):	    
	    pdfFileName = htmlFile.split('\\')[-2]+'.pdf'
	    pdfkit.from_file(htmlFile,pdfOutDir+pdfFileName)  
	    os.system( 'cls' )

if __name__ == "__main__":
    main()
    print('Finished publishing notes in PDF')