from ast import arg
from genericpath import isdir
import sys
import os
import shutil
import argparse
import img2pdf
from pdf2image import convert_from_path

class ImageFormats:
    JPG = "jpg"
    PNG = "png"
    TIFF = "tiff"
    #PPM  "ppm"

def compress_to_zip(zip_path, folder_path):
    shutil.make_archive(zip_path, "zip", folder_path)

def unzip_to_folder(zip_path, folder_path):
    shutil.unpack_archive(zip_path, folder_path, "zip")

def pdf_to_image_zip(pdf_path, zip_path, temp_output_path, img_format=ImageFormats.JPG):
    try:
        os.makedir(temp_output_path)
    except OSError as e:
        print("Error while creating {} after removing it".format(temp_output_path))

    images = convert_from_path(pdf_path, dpi=150, output_folder=temp_output_path,fmt=img_format)

    compress_to_zip(zip_path.replace(".zip",""), temp_output_path)

    shutil.rmtree(temp_output_path)


def image_zip_to_pdf(zip_path, pdf_path, temp_out_path, img_format=ImageFormats.JPG):
    unzip_to_folder(zip_path, temp_out_path)
    with open(pdf_path, "wb") as new_pdf:
        imgs = []
        for fname in sorted(os.listdir(temp_out_path)):
            if not fname.endswith("."+img_format):
                continue

            path = os.path.join(temp_out_path, fname)
            if os.path.isdir(path):
                continue

            imgs.append(path)
        
        new_pdf.write(img2pdf.convert(imgs))
    shutil.rmtree(temp_out_path)


def init_args():
    usage_example = """Usage example: python pdf_to_image_pdf.py -i "in.pdf" -o "out.pdf"""
    parser = argparse.ArgumentParser(epilog=usage_example)
    parser.add_argument('-i', '--input', required=True, help="path of input pdf to convert")
    parser.add_argument('-o', '--output', required=True, help="path of Output pdf - Converted pdf file")

    return parser.parse_args()

def main():
    args = init_args()

    pdf_to_image_zip(args.input, "converted.zip", "tmp")
    os.makedir("tmp2")
    image_zip_to_pdf("converted.zip", args.output, "tmp2")

if __name__ == "__main__":
    main()
