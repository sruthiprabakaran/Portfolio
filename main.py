# import the following libraries 
# will convert the image to text string 
import pytesseract
import cv2
from PIL import Image
import PIL.Image
# adds image processing capabilities 
from PIL import Image     
data=310616104100
images = ["310616104100.jpg", "310616104101.jpg","310616104102.jpg"]
 # converts the text to speech   
import pyttsx3            
pytesseract.pytesseract.tesseract_cmd ='C:/Program Files/Tesseract-OCR/tesseract.exe'   
#translates into the mentioned language
d={}
ans = [line.rstrip('\n') for line in open('Answer.txt')]
print("The correct answer")
for i in ans:
    d[int(i[0])]=i[2:]
for j in sorted(d):
    print(j,"--",d[j])
   
for x in images:
    mark=0
    percentage=0.0
 # opening an image from the source path 
    img = cv2.imread(x)      
    data=data+1
# describes image format in the output 
                           
# path where the tesseract module is installed 
    
    # converts the image to result and saves it into result variable 
    result = pytesseract.image_to_string(img)
    #if(answer==result):
    #    print "hello"
    # write text in a text file and save it to source path    
    with open('test.txt',mode ='w') as file:      
          
                     file.write(result)
                     print("======================")
                     print("Roll Number:",data)
                     print("Answers are \n",result)
                     #print("\n")

    t={}
    testans = [line.rstrip('\n') for line in open('test.txt')]
    for k in testans:
      t[int(k[0])]=k[2:]
    #for l in sorted(t):
     # print(l,"--",t[l])

                       

    for key in d.keys():
     if key in t.keys():
        if d[key]==t[key]:
          print("Answer {} is Correct".format(key))
          mark=mark+1
        else:
          print("Answer {} is wrong".format(key))
    print(mark ,"out of {} correct answers".format(len(d)))
    percentage=(mark/3)*100
    print("Mark obtained is {}".format(percentage))
