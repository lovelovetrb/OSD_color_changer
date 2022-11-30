import cv2


class image:
    def __init__(self, PATH):
        self.img = cv2.imread(PATH)

    def cheack_color(self):
        hit_pixcel = 0

        # 画像の縦横
        h, w = self.img.shape[:2]

        flag = True

        # 色の変更
        for i in range(h):
            for j in range(w):
                b, g, r = self.img[i, j]
                if b != 0 and b != 255:
                    print(b, g, r)
                    flag = False
                    hit_pixcel += 1
                if g != 0 and g != 255:
                    print(b, g, r)
                    flag = False
                    hit_pixcel += 1
                if r != 0 and r != 255:
                    print(b, g, r)
                    flag = False
                    hit_pixcel += 1
        print('illegal pixcel -> ' + str(hit_pixcel) + 'px')
        if flag:
            print('complete img!')

    def change_color(self):

        img = self.img

        # 画像の縦横
        h, w = img.shape[:2]

        # 色の変更
        for i in range(h):
            for j in range(w):
                b, g, r = img[i, j]
                if b != 0 and b != 255:
                    if (b < 255/2):
                        b = 0
                    elif (b > 255/2):
                        b = 255
                    else:
                        print('Please get close color!')
                if g != 0 and g != 255:
                    if (g < 255/2):
                        g = 0
                    elif (g > 255/2):
                        g = 255
                    else:
                        print('Please get close color!')
                if r != 0 and r != 255:
                    if (r < 255/2):
                        r = 0
                    elif (r > 255/2):
                        r = 255
                    else:
                        print('Please get close color!')
                print(b, g, r)
                img[i, j] = (b, g, r)

        cv2.imwrite('./change_image_OSD.png', img)
