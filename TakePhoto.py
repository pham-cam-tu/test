import cv2
import numpy as np
 
 
def takePhoto():
    """顔を検出してマスクする"""
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()

    while(True):
        # 画面に表示する
        cv2.imshow('frame',frame)
    # キーボード入力待ち
        key = cv2.waitKey(1) & 0xFF
    # qが押された場合は終了する
        if key == ord('q'):
            break
    # sが押された場合は保存する
        if key == ord('s'):
            path = "image/photo.jpg"
            cv2.imwrite(path,frame)

    cap.release()
    cv2.destroyAllWindows()
 
if __name__ == '__main__':
    takePhoto()
