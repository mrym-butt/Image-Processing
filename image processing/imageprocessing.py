from PIL import Image
import os
import cv2
def background_color(input_path, output_path,rotation_angle, new_size):
    img = cv2.imread(input_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, result = cv2.threshold(img, 145, 250, cv2.THRESH_BINARY)
    adaptive_result = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 41, 5)
    pil_image=Image.fromarray(adaptive_result)
    rotated_image=pil_image.rotate(rotation_angle, expand=True)
    rotated_image.thumbnail(new_size)
    rotated_image.save(output_path)
    print(pil_image.size)
def process_all_images(input_folder, output_folder, rotation_angle, new_size):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith((".jpg", ".jpeg", ".png", ".gif")):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            background_color(input_path,output_path,rotation_angle,new_size)

# input folder path
input_folder = "C:/Users/hp/Desktop/NCL OCR/ImageProcessing"
# output folder path
output_folder = "C:/Users/hp/Desktop/NCL OCR/outputImageProcessing"
rotation_angle = 90
new_size = (800, 600)
process_all_images(input_folder, output_folder, rotation_angle, new_size)
