 # import packages
import PyPDF2
import re


pdf_file = 'PDF_Extract\Santander Imóveis 22-08.pdf'
file_base_name = pdf_file.replace('.pdf', '')

# open the pdf file
object = PyPDF2.PdfFileReader(pdf_file)

# get number of pages
NumPages = object.getNumPages()

# define keyterms
String = "597.68217"


    for i in range(0, NumPages):
        PageObj = object.getPage(i)
        Text = PageObj.extractText()
        ResSearch = re.search(String, Text)
        if ResSearch != None:
            page = i
            pdfWriter = PyPDF2.PdfFileWriter()
            pdfWriter.addPage(object.getPage(int(page)))

            with open('{0}-teste.pdf'.format(file_base_name), 'wb') as f:
                pdfWriter.write(f)
                f.close()

