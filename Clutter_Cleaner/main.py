# Write a program to clear the clutter inside a folder on your computer.
# You should use os module to rename all the png images from 1.png all
# the way till n.png where n is the number of png files in that folder.
# Do the same for other file formats. For example:
#
#In this program whateever file of type pdf,txt,or png you will add it will automatically rename
# in a sequence to clear the clutter
#
# sfdsf.png --> 1.png
# vfsf.png --> 2.png
# this.png --> 3.png
# design.png --> 4.png
# name.png --> 5.png

import os

print("\n**************** Clutter Cleaner ******************\n")
files = os.listdir("ClutteredFolder")
i = 1
j = 1
k = 1
print("File before renaming:\n")
for file in files:

  if file.endswith(".png"):
    print("This is png file\n",file)
    os.rename(f"ClutteredFolder/{file}", f"ClutteredFolder/{i}.png")
    i = i + 1

  elif file.endswith(".txt"):
    print("This is txt file\n",file)
    os.rename(f"ClutteredFolder/{file}", f"ClutteredFolder/{j}.txt")
    j = j + 1

  elif file.endswith(".pdf"):
    print("This is pdf file \n",file)
    os.rename(f"ClutteredFolder/{file}", f"ClutteredFolder/{k}.pdf")
    k = k + 1

print("\nFiles After renaming :\n")
for nf in files:
    print(nf)