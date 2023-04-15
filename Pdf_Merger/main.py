from PyPDF2 import PdfWriter
import os

print("\n----------------- PDF MERGER -----------------------\n")

merger = PdfWriter()
files = [file for file in os.listdir() if file.endswith(".pdf")]
files.sort()

for pdf in files:
    merger.append(pdf)

merger.write("MERGED-PDF.pdf")
print("PDF's are merged successfully !")
merger.close()


#THIS PROGRAM WILL MERGE THE ALL PDFS STORED IN THE FOLDER IN A ORDER IN A SINGLE PDF
