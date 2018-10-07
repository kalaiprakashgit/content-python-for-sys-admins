
import os
texttofind = 'car1'
texttoreplace = 'Maruthi'
sourcepath = os.listdir('InputFiles/')
for file in sourcepath:
    inputfile = 'InputFiles/'+ file
    print ('Conversion is going for', inputfile)
    with open(inputfile,'r') as inputfile:
       filedata = inputfile.read()
       freq = 0
       freq = filedata.count(texttofind)
    destinationpath = 'OutputFiles/'+ file
    filedata = filedata.replace(texttofind,texttoreplace)
    with open(destinationpath,'w') as file:
        file.write(filedata)
    print ('Total %d record changed' %freq)