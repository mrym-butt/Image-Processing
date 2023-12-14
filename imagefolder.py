from PIL import Image, ImageOps, ImageFilter
import os
import cv2
import numpy
# def image_processing(input_path, output_path, rotation_angle, new_size):
#     image = Image.open(input_path)
#     print(image.size)
#     imagegray = image.convert('L')
#     rotated_image = imagegray.rotate(rotation_angle, expand=True)
#     rotated_image.thumbnail(new_size)
#     rotated_image.save(output_path)
#     print(rotated_image.size)

def background_color(input_path, output_path,rotation_angle, new_size):
    img = cv2.imread(input_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # img = cv2.resize(img, (560, 900))
    _, result = cv2.threshold(img, 145, 250, cv2.THRESH_BINARY)
    adaptive_result = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 41, 5)
    height, width=adaptive_result.shape[:2]
    # translation matrix
    matrix=cv2.getRotationMatrix2D((width/2,height/2),rotation_angle,1)
    # applying the matrix to the image
    translated=cv2.warpAffine(adaptive_result,matrix,(width,height))
    # convert numPy array to PIL image
    pil_image=Image.fromarray(translated)
    # rotated_image=pil_image.rotate(rotation_angle, expand=True)
    pil_image.thumbnail(new_size)
    pil_image.save(output_path)
    print(pil_image.size)
    # cv2.imshow("result", result)
    # cv2.imshow("original", img)
    # cv2.imwrite(output_path, result)
    # cv2.waitKey(0)

def process_all_images(input_folder, output_folder, rotation_angle, new_size):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith((".jpg", ".jpeg", ".png", ".gif")):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            # image_processing(input_path, output_path, rotation_angle, new_size)
            background_color(input_path,output_path,rotation_angle,new_size)

input_folder = "C:/Users/hp/Desktop/NCL OCR/ImageProcessing"
output_folder = "C:/Users/hp/Desktop/NCL OCR/outputImageProcessing"
rotation_angle = 90
new_size = (800, 600)
process_all_images(input_folder, output_folder, rotation_angle, new_size)
