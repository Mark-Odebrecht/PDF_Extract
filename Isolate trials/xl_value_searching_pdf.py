import PyPDF2
import re
import pandas as pd

arquivo_pdf = str(input('Digite o nome do arquivo pdf: '))

arquivo_excel = str(input('Digite o nome do arquivo pdf: '))

pdf_file = 'PDF_Extract\{}.pdf'.format(arquivo_pdf)
file_base_name = pdf_file.replace('.pdf', '')

df = pd.read_excel('PDF_Extract\{}.xlsx'.format(arquivo_excel), usecols='B, C')


object = PyPDF2.PdfFileReader(pdf_file)

NumPages = object.getNumPages()


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

