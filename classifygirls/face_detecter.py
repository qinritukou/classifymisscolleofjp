import os
import cv2

def main():
    for srcpath, _, files in os.walk('photos'):
        if len(_):
            continue
        dstpath = srcpath.replace('photos', 'faces')
        if not os.path.exists(dstpath):
            os.makedirs(dstpath)
        for filename in files:
            if filename.startswith('.'):
                continue
            try:
                detect_faces(srcpath, dstpath, filename)
            except:
                continue

def detect_faces(srcpath, dstpath, filename):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    image = cv2.imread('{}/{}'.format(srcpath, filename))
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_image, 1.3, 5)
    # Extract when just one face is detected
    print('{}/{} {}'.format(srcpath, filename, len(faces) == 1))
    if (len(faces) == 1):
        (x, y, w, h) = faces[0]
        image = image[y:y+h, x:x+w]
        image = cv2.resize(image, (100, 100))
        cv2.imwrite('{}/{}'.format(dstpath, filename), image)
    
    # face_cascade_path = '{}/{}'.format(srcpath, filename)
    # face_cascade = cv2.CascadeClassifier(os.path.expanduser(face_cascade_path))
    # face_cascade.load("./haarcascade_frontalface_alt.xml")

    # scale_factor = 1.1
    # min_neighbors = 3
    # min_size = (30, 30)
    # flags = cv2.cv.CV_HAAR_SCALE_IMAGE

    # for infname in sys.argv[2:]:
    #     image_path = os.path.expanduser(infname)
    #     image = cv2.imread(image_path)

    #     faces = face_cascade.detectMultiScale(image, scaleFactor = scale_factor, minNeighbors = min_neighbors, minSize = min_size, flags = flags)
    #     if (len(faces) == 1):
    #         (x, y, w, h) = faces[0]
    #         image = image[y:y+h, x:x+w]
    #         image = cv2.resize(image, (100, 100))
    #         cv2.imwrite('{}/{}'.format(dstpath, filename), image)


if __name__ == '__main__':
    main()