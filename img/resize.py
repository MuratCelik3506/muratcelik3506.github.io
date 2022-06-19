import os
import cv2
BASE = "./img/technicalSkills"
os.chdir(BASE)
print(os.getcwd())
print(os.listdir())

for x in os.listdir():
    try:
        name,ext = x.split(".")
        print(name)
        if ext == "jpg" or ext == "png":
            print(x)
            img = cv2.imread(x, cv2.IMREAD_UNCHANGED)
            img = cv2.resize(img, (256,256), interpolation = cv2.INTER_AREA)
            #cv2.imshow("Resized image", resized)
            cv2.imwrite("resize/" + name + ".png", img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
    except:
        continue