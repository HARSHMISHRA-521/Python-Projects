from PyPDF2 import PdfWriter
import os

print("\n----------------- PDF MERGER -----------------------\n")

merger = PdfWriter()
files = [file for file in os.listdir() if file.endswith(".pdf")]
files.sort()

for pdf in files:
    merger.append(pdf)

merger.write("FULL-PYTHON-PDF-MERGED.pdf")
print("PDF's are merged successfully !")
merger.close()
