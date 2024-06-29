# Program to explain shutil.copy module in python

import shutil
import os

source = "C:/Users/Walter Owando/Documents/GitHub/Data-Science-Projects/Data Science Projects/Random/YTDownloader.py"
destination = "C:/Users/Walter Owando/Documents/GitHub/Data-Science-Projects/Data Science Projects/Random/YTDowloader_copy.py"

dest = shutil.copy(source, destination)

print(f"Destination path: {dest}")