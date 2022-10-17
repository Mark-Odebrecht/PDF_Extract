# PDF_Extract


Automatizes pdf extraction from an original pdf document based on an Excel sheet, outputting separate pdf files for each found value.


### User story

I have a nephew which is a DEB patient. Today he is 20 years old and has several limitations due to his skin condition.

He is currently taking a degree in Economics and is already working remotely for a real estate company in Florianópolis, SC - Brazil.

Due to his limitations he has difficulties typing on a keyboard and faced, on almost on a daily basis, a task which took him around two hours to complete.

This task consists in acessing an MS Excel file, look for a specific value in a row, copy and paste it into a search within a pdf file.

If that given value is found, that specific page must be extracted isolately saved using the contract number for the same row that lies on a different column in the same Excel file. This way, demanding another round of copy/paste.

### The code

After a few isolate trials (which can be found within the "Isolate trials" folder) a final code was reached.

Running the code, first it is asked for the Excel file's name, which will be used as base for scanning.

Next it is asked for the pdf file's name that will be scanned.

After that, the script runs creating separate pdf files showing the payment voucher from the real estate company's customer.

Since it is specific to my nephew's demands it'll be nedded some tweaking to work with different files.

### Conclusion

With a few lines of code, my nephew reduced the time taken to perform the needed task from a few hours to a few minutes. :-) :-) :-)

#### Observation

Pyinstaller was used to create an executable file to ease the usage of the script.



