#!/bin/pyithon
import zipfile
import os

original_file = "5900.zip"

while True:
    original_file = zipfile.ZipFile(original_file, 'r') #sets variable as an interactive object
    password = original_file.namelist() #list content in zip file
    pw = (password[0].removesuffix('.zip')) #removes array and removes .zip from zip content
    pw = (pw.encode()) # encodes out as int
    print(pw)


    original_file.setpassword(pw) #set password for zip needs it as an integer
    original_file.extractall() #extracts zip

    pw = (pw.decode()) # re-encodes into bytes
    original_file = pw + '.zip' # changes original_file variable into new variable
