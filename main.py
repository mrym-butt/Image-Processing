# # from PIL import Image
# #
# # img= Image.open("C:/Users/hp/Desktop/NCL OCR/image.jpg")
# # img90 = img.rotate(0)
# # img90.save("C:/Users/hp/Desktop/NCL OCR/rimage.jpg")
# #
#
# # from PIL import Image, ExifTags
# #
# #
# # def transform_image(input_path, output_path, rotation_angle, new_size):
# #     # Open the image
# #     image = Image.open(input_path)
# #
# #     try:
# #         exif = image._getexif()
# #     except AttributeError:
# #         exif = None
# #
# #     if exif is not None:
# #         if 274 in exif:
# #             orientation = exif[274]
# #             if orientation == 1:
# #                 pass
# #             elif orientation == 3:
# #                 image = image.rotate(180, expand=True)
# #             elif orientation == 6:
# #                 image = image.rotate(-90, expand=True)
# #             elif orientation == 8:
# #                 image = image.rotate(90, expand=True)
# #     else:
# #         # Rotate the image
# #         rotated_image = image.rotate(rotation_angle, expand=True)
# #
#         # # Resize the image
#         # rotated_image.thumbnail(new_size)
# #
# #         # Save the transformed image
# #         rotated_image.save(output_path)
# #
# #
# # # Example usage
# # input_path = "C:/Users/hp/Desktop/NCL OCR/imagehaiyar.jpg"
# # output_path = "C:/Users/hp/Desktop/NCL OCR/outputimage.jpg"
# # rotation_angle = 0  # Set the desired rotation angle (in degrees)
# # new_size = (800, 600)  # Set the desired new size (width, height)
# # transform_image(input_path, output_path, rotation_angle, new_size)
#
#
# from PIL import Image, ExifTags
#
#
# def auto_orient(input_path, output_path, new_size):
#     # Open the image
#     image = Image.open(input_path)
#
#     # Get the EXIF data (if available)
#     try:
#         exif = image._getexif()
#     except AttributeError:
#         exif = None
#
#     if exif is not None:
#         # Check for the orientation tag (key 274)
#         for tag, value in exif.items():
#             if tag in ExifTags.TAGS.keys() and ExifTags.TAGS[tag] == 'Orientation':
#                 orientation = value
#                 if orientation == 1:
#                     # Normal (no rotation needed)
#                     pass
#                 elif orientation == 3:
#                     # Upside down
#                     image = image.rotate(180, expand=True)
#                 elif orientation == 6:
#                     # 90 degrees counter-clockwise
#                     image = image.rotate(-90, expand=True)
#                 elif orientation == 8:
#                     # 90 degrees clockwise
#                     image = image.rotate(90, expand=True)
#
#     else:
#         # Rotate the image (assuming 90 degrees clockwise in this case)
#         image = image.rotate(90, expand=True)
#         # Resize the image
#         image.thumbnail(new_size)
#
#     # Save the corrected image
#     image.save(output_path)
#
#
# # Example usage with no EXIF data
# input_path = "C:/Users/hp/Desktop/NCL OCR/image.jpg"
# output_path = "C:/Users/hp/Desktop/NCL OCR/outputimage.jpg"
# new_size=(500,600)
# auto_orient(input_path, output_path,new_size)
#
#


import cv2
img= cv2.imread("C:/Users/hp/Desktop/NCL OCR/ImageProcessing/pic4.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img= cv2.resize(img,(560,900))
_, result=cv2.threshold(img,145,250,cv2.THRESH_BINARY)
adaptive_result =cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,41,5)
cv2.imshow("result",result)
cv2.imshow("original",img)
cv2.imwrite("C:/Users/hp/Desktop/NCL OCR/outputImageProcessing/outputimage.jpg", result)
cv2.waitKey(0)

# img = img = cv2.imread(input_path)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img = cv2.resize(img, (560, 900))
# _, result = cv2.threshold(img, 145, 250, cv2.THRESH_BINARY)
# adaptive_result = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 41, 5)
# # cv2.imshow("result", result)
# # cv2.imshow("original", img)
# cv2.imwrite(output_path, img)
# cv2.waitKey(0)