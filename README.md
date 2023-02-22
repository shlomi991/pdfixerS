# PDFixer
## What is PDFixer

![image](https://user-images.githubusercontent.com/3217869/204112764-aa1004a6-28b2-410a-b33b-72beccd3d135.png)

### pdfixer is a tool for pdf-rebuilding, that utilize common libraries and preform the specified task said
### pdfixer reduce PDF files to 150 dpi and offset them to 200*250~  (about the size of an A4 file) - PDF version 1.3 

#TL;DR - PDFixer takes a PDF files and makes a new PDF file that contain the content as pictures in JPG format.
## How to use
there are 4 stages to PDFixer -
1. choose the PDF file that need to used
2. choose output folder
3. run tasks 3+4 (if pdf is large - it will take a few seconds)

## dependencies:
deprecation==2.1.0
fpdf==1.7.2
img2pdf==0.4.4
lxml==4.9.1
packaging==21.3
pdf2image==1.16.0
pikepdf==6.2.4
Pillow==9.3.0
pip==22.0.4
pyparsing==3.0.9
setuptools==58.1.0

ALSO - use poppler Release-22.11.0-0 and set it to PATH
C:\Users\User\Documents\poppler-22.11.0\Library\bin

you might need to install VC_redist.x86 
