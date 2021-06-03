import cv2

def capture():
  cap=cv2.VideoCapture(0)
  model=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

  while True:
      ret, photo=cap.read()
      faces=model.detectMultiScale(photo)
      if len(faces) ==0:
          pass
      else:
          for num_face in range(len(faces)):
              x1=faces[num_face][0]
              y1=faces[num_face][1]
              x2=x1+faces[num_face][2]
              y2=y1+faces[num_face][3]

              aphoto=cv2.rectangle(photo, (x1,y1),(x2,y2),[0,255,0],5)

              cphoto=photo[x1:x2, y1:y2]
              cv2.imwrite("image.jpg", cphoto)
              
          cv2.imshow('hi',aphoto)
          if cv2.waitKey(10)==13:
              break

  cv2.destroyAllWindows()
  cap.release()              
