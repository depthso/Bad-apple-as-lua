from PIL import Image
import cv2, string, random, time
from playsound import playsound
from fpstimer import FPSTimer

ImageName = "Image.jpeg"
Video = "badapple.mp4" #"badapple.mp4"

cap = cv2.VideoCapture(Video)
totalFrames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
vidFPS:float = cap.get(cv2.CAP_PROP_FPS)

Size = 30 # 200

Size = (Size,Size)

#Size = (int(float(Size/1.5)), int(float(Size/1.5)))

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

Strings2 = {
    "000": "",
    "010": "",
    "001": "huh=''    ",
    "100": "      V=''",
    "101": "h=    'us'",
    "110": "   print()",
    "011": "n='ig'    ",
    "111": "local b=69",
    "69":  "          ", # Example string size
}

Strings = {}
timer = FPSTimer(vidFPS)

for String in Strings2:
    New = String.replace("1","2").replace("0","1").replace("2","0")
    Strings[New] = Strings2[String]

time.sleep(0.1)
playsound("music.mp3",False)
time.sleep(0.6)

for Frame in range(0, totalFrames, 1):
    # GetFrame(Video,Frame)

    cap.set(1, Frame)
    ret, frame = cap.read()
    frame = cv2.resize(frame, Size)
    cv2.imwrite(ImageName, frame)

    im = Image.open(ImageName)
    im = im.convert('1') 

    FrameString = f"Frame [{Frame}] / {totalFrames}"

    frame = cv2.resize(frame, (Size[0]*10,Size[1]*10))

    cv2.imshow("Preview", frame)
    cv2.setWindowTitle("Preview", f"Preview - {FrameString}")
    cv2.waitKey(1)

    Done = ""

    for row in range(0, Size[1]):
        for pixel in range(0, Size[0],3):
            color = int(im.getpixel((pixel,row)) / 255)
            color2 = int(im.getpixel((pixel-1,row)) / 255)
            color3 = int(im.getpixel((pixel-2,row)) / 255)

            Strings["000"] = "local b=69".replace("b",randomword(1))
            Strings["011"] = "      V=''".replace("V",randomword(1))

            Final = f"{color}{color2}{color3}"

            Done += f"{Strings[Final]}".ljust(11)

            #print(string)
			
        Done += "\n"

    Out_File = open("Out.lua","w")
    Out_File.writelines(Done)
    Out_File.close()

    timer.sleep()
