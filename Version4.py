import cv2
import time
import numpy as np
import Hand_Tracking_module as htm
import math


wCam, hCam = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0
detector = htm.handDetector(detectionCon=0.7)

count = 0
rep = 0
CN = 25
word = []
pword = " "
str = " "


def call(let):
    global pword, count, rep
    if (pword == let):
        rep = rep + 1
    if (pword != let):
        word.append(let)
        pword = let
    if (rep > 5):
        pw = "".join(word)
        word.clear()
        word.append(pw)
        word.append(" ")
        rep = 0


while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    cv2.line(img, (0, 400), (640, 400), (0, 0, 0), 3)

    cv2.rectangle(img, (0, 40), (300, 400), (0, 0, 0), 3)

    pw = " ".join(word)
    cv2.putText(img, pw, (50, 450),
                cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 255, 255))

    if len(lmList) != 0:

        Tx, Ty = lmList[4][1], lmList[4][2]
        T2x, T2y = lmList[3][1], lmList[3][2]
        Ix, Iy = lmList[8][1], lmList[8][2]
        Sx, Sy = lmList[20][1], lmList[20][2]
        M4x, M4y = lmList[9][1], lmList[9][2]
        M3x, M3y = lmList[10][1], lmList[10][2]
        Mx, My = lmList[12][1], lmList[12][2]
        Px, Py = lmList[0][1], lmList[0][2]
        I3x, I3y = lmList[6][1], lmList[6][2]
        I4x, I4y = lmList[5][1], lmList[5][2]
        Rx, Ry = lmList[16][1], lmList[16][2]
        R2x, R2y = lmList[15][1], lmList[15][2]
        R3x, R3y = lmList[14][1], lmList[14][2]
        M2x, M2y = lmList[11][1], lmList[11][2]
        S3x, S3y = lmList[12][1], lmList[12][2]
        R4x, R4y = lmList[13][1], lmList[13][2]
        S2x, S2y = lmList[19][1], lmList[19][2]

        R4TH = math.hypot(R4x - Tx, R4y - Ty)
        R2TH = math.hypot(R2x - Tx, R2y - Ty)
        INTH = math.hypot(Ix - Tx, Iy - Ty)
        M4TH = math.hypot(M4x - Tx, M4y - Ty)
        M3TH = math.hypot(M3x - Tx, M3y - Ty)
        M2TH = math.hypot(M2x - Tx, M2y - Ty)
        MI = math.hypot(Mx - Ix, My - Iy)
        IP = math.hypot(Ix - Px, Iy - Py)
        I3TH = math.hypot(I3x - Tx, I3y - Ty)
        RS = math.hypot(Rx-Sx, Ry-Sy)
        ST = math.hypot(Sx-Tx, Sy-Ty)
        T2M = math.hypot(T2x-Tx, T2y-Ty)
        MT = math.hypot(Mx-Tx, My-Ty)
        SI = math.hypot(Sx-Ix, Sy-Iy)
        MR = math.hypot(Mx-Rx, My-Ry)
        RI = math.hypot(Rx-Ix, Ry-Iy)
        RT = math.hypot(Rx-Tx, Ry-Ty)
        S3TH = math.hypot(S3x-Tx, S3y-Ty)
        S2TH = math.hypot(S2x-Tx, S2y-Ty)
        R3TH = math.hypot(R3x-Tx, R3y-Ty)
        I4I = math.hypot(I4x-Ix, I4y-Iy)
        print(INTH)

        # if (I3TH >= 150 and I3TH <= 200):  # backspace
        #     count = count + 1
        #     if (len(word) != 0):
        #         if count > 25:
        #             word.pop()
        #             pword = " "
        #             count = 0

        if (I3TH > 30 and I3TH < 40):
            count = count + 1
            if count > CN:
                let = "A"
                count = 0
                call(let)

        if (R4TH < 3):
            count = count + 1
            if count > CN:
                let = "B"
                count = 0
                call(let)

        if (ST < 340 and ST > 330):
            count = count + 1
            if count > CN:
                let = "C"
                count = 0
                call(let)

        if (MT < 8):
            count = count + 1
            if count > CN:
                let = "D"
                count = 0
                call(let)

        if (ST < 10):
            count = count + 1
            if count > CN:
                let = "E"
                count = 0
                call(let)

        if (INTH < 15):
            count = count + 1
            if count > CN:
                let = "F"
                count = 0
                call(let)

        if (I3TH < 5):
            count = count + 1
            if count > CN:
                let = "G"
                count = 0
                call(let)

        if (M3TH < 5):
            count = count + 1
            if count > CN:
                let = "H"
                count = 0
                call(let)

        if (ST < 300 and ST > 280):
            count = count + 1
            if count > CN:
                let = "I"
                count = 0
                call(let)

        if (ST < 200 and ST > 170):
            count = count + 1
            if count > CN:
                let = "J"
                count = 0
                call(let)

        if (I3TH < 15 and I3TH > 10 and M3TH > 20 and M3TH < 30):
            count = count + 1
            if count > CN:
                let = "K"
                count = 0
                call(let)

        if (INTH > 310):
            count = count + 1
            if count > CN:
                let = "L"
                count = 0
                call(let)

        # if (ST < 200 and ST > 170):
        #     count = count + 1
        #     if count > CN:
        #         let = "J"
        #         count = 0
        #         call(let)

        if (S3TH < 60 and S3TH > 50 and R3TH > 10 and R3TH < 30):
            count = count + 1
            if count > CN:
                let = "M"
                count = 0
                call(let)

        if (M3TH < 40 and M3TH > 30 and R3TH > 10 and R3TH < 20):
            count = count + 1
            if count > CN:
                let = "N"
                count = 0
                call(let)

        if (RT < 15):
            count = count + 1
            if count > CN:
                let = "O"
                count = 0
                call(let)

        if (M2TH < 15):
            count = count + 1
            if count > CN:
                let = "P"
                count = 0
                call(let)

        if (INTH < 100 and INTH > 80):
            count = count + 1
            if count > CN:
                let = "Q"
                count = 0
                call(let)

        if (MI < 10):
            count = count + 1
            if count > CN:
                let = "R"
                count = 0
                call(let)

        if (S2TH < 10):
            count = count + 1
            if count > CN:
                let = "S"
                count = 0
                call(let)

        if (R2TH < 10):
            count = count + 1
            if count > CN:
                let = "T"
                count = 0
                call(let)

        if (MI < 30 and MI > 20):
            count = count + 1
            if count > CN:
                let = "U"
                count = 0
                call(let)

        if (MI < 100 and MI > 80):
            count = count + 1
            if count > CN:
                let = "V"
                count = 0
                call(let)

        if (MI < 60 and MI > 50 and MR < 60 and MR > 50):
            count = count + 1
            if count > CN:
                let = "W"
                count = 0
                call(let)

        # if (I4I < 120 and I4I > 110):
        #     count = count + 1
        #     if count > CN:
        #         let = "X"
        #         count = 0
        #         call(let)

        # if (ST > 350):
        #     count = count + 1
        #     if count > CN:
        #         let = "Y"
        #         count = 0
        #         call(let)

        # if (INTH > 170 and INTH < 200):
        #     count = count + 1
        #     if count > CN:
        #         let = "Z"
        #         count = 0
        #         call(let)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (450, 50),
                cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)

    cv2.imshow("Img", img)
    cv2.waitKey(1)
