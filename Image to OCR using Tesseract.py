# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 22:12:00 2019

@author: Patrick Jane
"""
#Importing the required libraries

#Install Pillow and pytesseract, before you can import. 

from PIL import Image
import pytesseract

#I've used my PAN Card image to see if this OCR can read the text. 
pan = Image.open("C:/Users/Patrick Jane/Downloads/pan.jpeg")
#pan.show()


#First install tesseract OCR from this link, https://github.com/UB-Mannheim/tesseract/wiki
#install and then use the .exe path here. 
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
pytesseract.image_to_string(pan)











