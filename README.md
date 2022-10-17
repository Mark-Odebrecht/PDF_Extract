# PDF_Extract


Automatizes pdf extraction from an original pdf document based on an Excel sheet, outputting separate pdf files for each found value.


### User story

I have a nephew which is a DEB (dystrophic epidermolysis bullosa) patient. Today he is 20 years old and has several limitations due to his skin condition.

He is currently taking a degree in Economics and is already working remotely for a real estate company in Florianópolis, SC - Brazil.

Due to his limitations he has difficulties typing on a keyboard and faced, on almost on a daily basis, a task which took him around two hours to complete.

This task consists in acessing an MS Excel file, look for a specific value in a row, copy and paste it into a search within a pdf file.

If that given value is found, that specific page must be extracted isolately saved using the contract number for the same row that lies on a different column in the same Excel file. This way, demanding another round of copy/paste.

### The code

***This code was originaly written in a private repository and later published on this specific one.***

After a few isolate trials (which can be found within the "Isolate trials" folder) a final code was reached.

Running the code, first it is asked for the Excel file's name, which will be used as base for scanning.

Next it is asked for the pdf file's name that will be scanned.

After that, the script runs creating separate pdf files showing the payment voucher from the real estate company's customer.

Since it is specific to my nephew's demands it'll be needed some tweaking to work with different files.

Internet sources were consulted looking for text extraction from pdf files[^1], converting database into a dataframe[^2], turning a pdf file into and object[^3] and locating specific values from the datafram[^4].

### Conclusion

With a few lines of code, my nephew reduced the time taken to perform the needed task from a few hours to a few minutes. :-) :-) :-)
<br>
<br>
#### Observation

Pyinstaller was used to create an executable file to ease the usage of the script.

Guidance for this conversion was found on the internet[^5].

<br>
<br>

[^1]: https://www.geeksforgeeks.org/extract-text-from-pdf-file-using-python/#:~:text=pdf%20reader%20object%20has%20function,and%20returns%20the%20page%20object.&text=Page%20object%20has%20function%20extractText,text%20from%20the%20pdf%20page.&text=At%20last%2C%20we%20close%20the%20pdf%20file%20object.
<br>

[^2]: https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html
<br>

[^3]: https://python.hotexamples.com/pt/examples/PyPDF2/PdfFileReader/-/python-pdffilereader-class-examples.html
<br>

[^4]: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html
<br>

[^5]: https://datatofish.com/executable-pyinstaller/
<br>


