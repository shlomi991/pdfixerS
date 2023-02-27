import sys
import os
import shutil
import argparse
from tkinter import filedialog
import img2pdf
from pdf2image import convert_from_path
import pathlib
from fpdf import FPDF
###
import tkinter as tk
from tkinter import ttk
from tkinter import * 
from PIL import Image
import zipfile

poppler_path = r"C:\Users\User\Documents\poppler-22.11.0\Library\bin"
###
class ImageFormats:
        JPG = "jpg"
        # PNG = "png"
        # TIFF = "tiff"
        # PPM = "ppm"
        
class Globals:
        source = "C:\\pdfixer_files\\out"
        backup_before_fixer = "C:\\pdfixer_files\\BKbeforeFixer"
        fixer = "C:\\pdfixer_files\\fixer"
        temp = "C:\\pdfixer_files\\temp"
        temp_pdf = "C:\\pdfixer_files\\temp_pdf"
        dest1 = "C:\\pdfixer_files\\outbound"
        dest2 = "C:\\pdfixer_files\\archive"
        output_after_extract = "C:\\pdfixer_files\\output_after_extract"
        temporary_file = ""


def move_copy_zip():
    files = os.listdir(Globals.source)
    for f in files
        if f.endswith('.zip'):
            shutil.copy(Globals.source+'/'+f, Globals.backup_before_fixer)
            print("copied to BKbeforeFixer")
            shutil.move(Globals.source+'/'+f, Globals.fixer)
            print("moved to fixer")

    unpack_pdf()


def extract_pdfs():
    files = os.listdir(Globals.fixer)
    for f in files 
        if f.endswith('.zip'):
            shutil.move(Globals.fixer+'/'+f, Globals.temp)
            print("moved to temp")
            with zipfile.zip(Globals.temp+'/'+f, 'r') as file:
                file.extractall()

            extract_files = os.listdir(Globals.temp)    
            for s in extract_files    
                if s.endswith('.pdf'):
                    images = convert_from_path(Globals.temp+'/'+s,  dpi=150, output_folder=Globals.temp_pdf, fmt='jpg')
                    ###
                    pdf = FPDF(orientation='P', format='A4')
                    imgs = []

                    img_list = [x for x in os.listdir(Globals.temp_pdf)]
                        
                    for img in img_list
                        pdf.add_page()
                        imag = Globals.temp_pdf+"\\"+img
                        pdf.image(imag, w=200, h=260)
                    pdf.output("images.pdf")
                    shutil.move(Globals.temp_pdf+'/'+s, Globals.output_after_extract)

                if s.endswith('.xml'):
                    shutil.move(Globals.temp+'/'+s, Globals.output_after_extract)

                else:
                    shutil.move(Globals.temp+'/'+s, Globals.output_after_extract)

            list_output_after_extract = os.listdir(output_after_extract)
            with zipfile.ZipFile(f, 'w') as zip_file:
             for file_name in list_output_after_extract:
                file_path = os.path.join(output_after_extract, file_name)
                zip_file.write(file_path, file_name)

            
            shutil.move(Globals.fixer+'/'+f, Globals.temp)






def unpack_pdf():
    images = convert_from_path(Globals.temporary_file,  dpi=150, output_folder=Globals.middlepath, fmt='jpg')
    ###
    pdf = FPDF(orientation='P', format='A4')
    imgs = []

    img_list = [x for x in os.listdir(Globals.middlepath)]
    
    for img in img_list:
        pdf.add_page()
        imag = Globals.middlepath+"\\"+img
        pdf.image(imag, w=200, h=260)
    pdf.output("images.pdf")
    
        
def finish_operation():
    current = os.path.abspath(os.getcwd())
    shutil.copy(current+"\\"+"images.pdf", Globals.output_dir)
    delete_temp_dir()
    root.quit()

def main():
    files = os.listdir(source)
    for f in files
    

    
if __name__ == "__main__":
    main()
    
    
    