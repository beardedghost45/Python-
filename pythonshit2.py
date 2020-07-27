#file open and write
fileobject=open('Sample.txt','w') #open a file and write 
fw.write('Writing some thing and enjoy the beauty of python \n')
fw.write('I like super heros\n')
fw.close()

#file open and read

fr=open('Sample.txt','r')
text=fr.read()
print(text)
fr.close()