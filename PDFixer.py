import sys
import os
import shutil
import glob
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

# poppler_path = r"C:\Users\User\Documents\poppler-22.11.0\Library\bin"
###
class ImageFormats:
        JPG = "jpg"
        # PNG = "png"
        # TIFF = "tiff"
        # PPM = "ppm"
        
class Globals:
        source = "C:\\shlomi\\pdfixer_files\\out"
        backup_before_fixer = "C:\\shlomi\\pdfixer_files\\BKbeforeFixer"
        fixer = "C:\\shlomi\\pdfixer_files\\fixer"
        temp = "C:\\shlomi\\pdfixer_files\\temp"
        temp_pdf = "C:\\shlomi\\pdfixer_files\\temp_pdf"
        dest1 = "C:\\shlomi\\pdfixer_files\\archive"
        dest2 = "C:\\shlomi\\pdfixer_files\\outbound"
        output_after_extract = "C:\\shlomi\\pdfixer_files\\output_after_extract"


def move_copy_zip():
    files = os.listdir(Globals.source)
    for f in files:
        if f.endswith('.zip'):
            shutil.copy(Globals.source+'/'+f, Globals.backup_before_fixer)
            print("copied to BKbeforeFixer")
            shutil.move(Globals.source+'/'+f, Globals.fixer)
            print("moved to fixer")


def clean_temp():
    files = glob.glob(Globals.temp+'/*')
    for f in files:
        os.remove(f)   

def clean_output_after_extract():
    files = glob.glob(Globals.output_after_extract+'/*')
    for f in files:
        os.remove(f)                


def extract_pdfs():
    files = os.listdir(Globals.fixer)
    for f in files: 
        if f.endswith('.zip'):
            shutil.move(Globals.fixer+'/'+f, Globals.temp)
            print("moved to temp")
            with zipfile.ZipFile(Globals.temp+'/'+f, 'r') as file:
                file.extractall(path=Globals.temp)
            print("extract in temp")
            os.remove(Globals.temp+'/'+f)
            print("delete zip in temp")

            extract_files = os.listdir(Globals.temp)    
            for s in extract_files:    
                if s.endswith('.pdf'):
                    images = convert_from_path(Globals.temp+'/'+s,  dpi=150, output_folder=Globals.temp_pdf, fmt='jpg')
                    ###
                    pdf = FPDF(orientation='P', format='A4')
                    imgs = []

                    img_list = [x for x in os.listdir(Globals.temp_pdf)]
                        
                    for img in img_list:
                        pdf.add_page()
                        imag = Globals.temp_pdf+"\\"+img
                        pdf.image(imag, w=200, h=260)
                    pdf.output(s)
                    shutil.move(Globals.temp_pdf+'/'+s, Globals.output_after_extract)

                if s.endswith('.xml'):
                    shutil.move(Globals.temp+'/'+s, Globals.output_after_extract)
                
                else:
                    shutil.move(Globals.temp+'/'+s, Globals.output_after_extract)

            clean_temp()        

            list_output_after_extract = os.listdir(Globals.output_after_extract)
            with zipfile.ZipFile(f, 'w') as zip_file:
             for file_name in list_output_after_extract:
                file_path = os.path.join(Globals.output_after_extract, file_name)
                zip_file.write(file_path, file_name)


            shutil.copy(Globals.output_after_extract+'/'+f, Globals.dest1)
            shutil.move(Globals.output_after_extract+'/'+f, Globals.dest2)

            clean_output_after_extract()

def main():
    move_copy_zip()
    extract_pdfs()
    

    
if __name__ == "__main__":
    main()
    
    
    