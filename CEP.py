import PyPDF2
import re
import pandas as pd

# Inputing excel file name without .xlsx extension
arquivo_excel = str(input('Digite o nome do arquivo excel: '))

# Inputing pdf file name without .pdf extension
arquivo_pdf = str(input('Digite o nome do arquivo pdf: '))

# Renaming and instancing pdf file
pdf_file = '{}.pdf'.format(arquivo_pdf)

# Converting Excel sheet into a pandas dataframe
df = pd.read_excel('{}.xlsx'.format(arquivo_excel), usecols='B, C')

# Converting pdf file into an object ready for scanning
object = PyPDF2.PdfFileReader(pdf_file)

# Storing page numbers to make the script able to extract one page at a time
NumPages = object.getNumPages()

# Iteration for pdf file scanning and page extracting
for j in df.index:
    chave=str(df.loc[j, 'Chave'])
    imovel=df.loc[j, 'Imóvel']

    for i in range(0, NumPages):
        PageObj = object.getPage(i)
        Text = PageObj.extractText()
        ResSearch = re.search(chave, Text)
        if ResSearch != None:
            page = i
            pdfWriter = PyPDF2.PdfFileWriter()
            pdfWriter.addPage(object.getPage(page))

            with open('{}.pdf'.format(imovel), 'wb') as f:
                pdfWriter.write(f)
                f.close()