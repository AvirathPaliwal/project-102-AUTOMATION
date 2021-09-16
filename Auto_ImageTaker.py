import random
import dropbox
import time
import cv2

start_time = time.time()

def takesnap():
    number = random.randint(1,100)
    vcobj = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    result = True

    while(result):
     
        ret,frame = vcobj.read()
        img_name = 'img'+str(number)+'.png'
     
        cv2.imwrite(img_name,frame)
        start_time = time.time
        result=False
    return img_name
    print('snapshot taken')

    
    vcobj.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
     access_token = 'or6_lH_xIdQAAAAAAAAAAYRU4JU9KY5fkzMIgxFUQIVigiMm38PcFaHGXfCn67GS'
     file = img_name
     file_from = file
     file_to = '/Images/'+(img_name)
     dbx = dropbox.Dropbox(access_token)
     with open(file_from,'rb') as f:
        
          dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
          print('File uploaded')


def main():
    while(True):
        if((time.time()  -  start_time) >=5 ):
            name = takesnap()
            upload_file(name)

main()
    

