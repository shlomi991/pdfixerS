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
import time

poppler_path = r"C:\Program Files\poppler-0.68.0_x86\poppler-0.68.0\bin"
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
        output_after_extract = "C:\\shlomi\\pdfixer_files\\output_after_extract"
        error_files = "C:\\shlomi\\pdfixer_files\\error_files"
        dest1 = "C:\\shlomi\\pdfixer_files\\archive"
        dest2 = "C:\\shlomi\\pdfixer_files\\outbound"
        


def move_copy_zip():
    files = os.listdir(Globals.source)
    for f in files:
        if f.endswith('.zip'):
            shutil.copy(Globals.source+'/'+f, Globals.backup_before_fixer)
            print(f + " copied to BKbeforeFixer")
            shutil.move(Globals.source+'/'+f, Globals.fixer)
            print(f + " moved to fixer")

def clean_fixer():
    files = glob.glob(Globals.fixer+'/*')
    for f in files:
        os.remove(f)


def clean_temp():
    files = glob.glob(Globals.temp+'/*')
    for f in files:
        os.remove(f)   


def clean_temp_pdf():
    files = glob.glob(Globals.temp_pdf+'/*')
    for f in files:
        os.remove(f)           

def clean_output_after_extract():
    files = glob.glob(Globals.output_after_extract+'/*')
    for f in files:
        os.remove(f)

def clean_all():
    clean_fixer()
    clean_temp()  
    clean_temp_pdf() 
    clean_output_after_extract()


def extract_pdfs():
    files = os.listdir(Globals.fixer)
    for f in files: 
        print("starting to extract: " + f)
        try:
            if f.endswith('.zip'):
                shutil.move(Globals.fixer+'/'+f, Globals.temp)
                print(f + " moved to temp")
                with zipfile.ZipFile(Globals.temp+'/'+f, 'r') as file:
                    file.extractall(path=Globals.temp)
                print(f + " extract in temp")
                os.remove(Globals.temp+'/'+f)
                print(f + " delete zip in temp")

                extracted_files = os.listdir(Globals.temp)    
                for s in extracted_files:    
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
                            print("add page pdf" + img)
                        os.chdir(Globals.temp_pdf)
                        print("s=" + s)    
                        pdf.output(s)

                        shutil.move(Globals.temp_pdf+'/'+s, Globals.output_after_extract)
                        img_list={}
                        images={}
                        clean_temp_pdf()


                    elif  s.endswith('.xml'):
                        shutil.move(Globals.temp+'/'+s, Globals.output_after_extract)
                    

                clean_temp()     

                os.chdir(Globals.output_after_extract)
                list_output_after_extract = os.listdir(Globals.output_after_extract)
                with zipfile.ZipFile(f, 'w') as zip_file:
                 for file_name in list_output_after_extract:
                    file_path = os.path.join(Globals.output_after_extract, file_name)
                    zip_file.write(file_path, file_name)

                print("extracted")
                shutil.copy(Globals.output_after_extract+'/'+f, Globals.dest1)
                shutil.copy(Globals.output_after_extract+'/'+f, Globals.dest2)


                clean_output_after_extract()

        except:
            print("Error with extract_pdfs function")
            files_temp = os.listdir(Globals.temp)
            files_temp_pdf = os.listdir(Globals.temp_pdf)
            files_output_after_extract = os.listdir(Globals.output_after_extract)
            
            if len(files_temp) != 0:
                for f in files_temp:
                    if f.endswith('.xml'):
                        shutil.copy(Globals.temp+'/'+f, Globals.error_files)
                        print(f + "copied to error_files")
                clean_temp()

            if len(files_temp_pdf) != 0:
                for f in files_temp_pdf:
                    if f.endswith('.xml'):
                        shutil.copy(Globals.temp+'/'+f, Globals.error_files)
                        print(f + "copied to error_files")
                clean_temp_pdf()

            if len(files_output_after_extract) != 0:
                for f in files_output_after_extract:
                    if f.endswith('.xml'):
                        shutil.copy(Globals.output_after_extract+'/'+f, Globals.error_files)
                        print(f + "copied to error_files")
                clean_output_after_extract()


def main():
    while 1==1:
        files = os.listdir(Globals.source)
        if len(files) != 0:
            clean_all()
            move_copy_zip()
            extract_pdfs()
            clean_temp_pdf()
            time.sleep(7)

        else:
            time.sleep(7)
    

    
if __name__ == "__main__":
    main()
    
    
    