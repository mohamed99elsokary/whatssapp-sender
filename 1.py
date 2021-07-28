import string
import random
with open('numbers.txt', 'r') as file :
  filedata = file.read()
  
print (filedata)
# Replace the target
for x in string.ascii_letters:
    
    filedata = filedata.replace(x+",", "")
    filedata = filedata.replace(x, "")
filedata = filedata.replace("+", "'+")
filedata = filedata.replace(",", "',")
filedata = filedata.replace(", ", ",")
filedata = filedata.replace(" ", "")
filedata = filedata.replace("+2", "")
filedata = filedata.replace("'1", "'01")
filedata = filedata.replace("-", "")
filedata = filedata.replace("+", "")
for x in range(11):
    filedata = filedata.replace("'1", "'")
    filedata = filedata.replace("'2", "'")
    filedata = filedata.replace("'3", "'")
    filedata = filedata.replace("'4", "'")
    filedata = filedata.replace("'5", "'")
    filedata = filedata.replace("'6", "'")
    filedata = filedata.replace("'7", "'")
    filedata = filedata.replace("'8", "'")
    filedata = filedata.replace("'9", "'")
    filedata = filedata.replace("'00", "'")
    filedata = filedata.replace("'02", "'")
    filedata = filedata.replace("'03", "'")
    filedata = filedata.replace("'04", "'")
    filedata = filedata.replace("'05", "'")
    filedata = filedata.replace("'06", "'")
    filedata = filedata.replace("'07", "'")
    filedata = filedata.replace("'08", "'")
    filedata = filedata.replace("'09", "'")    
    filedata = filedata.replace("'',", "")    
filedata = filedata.replace("'", "")
filedata = filedata.replace(",", '''
''')


# Write the file out again
with open('joker.txt', 'w') as file:
  file.write(filedata)