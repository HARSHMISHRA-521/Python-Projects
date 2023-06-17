print(":::::::::::::::::::::::::::: WELCOME TO IMAGE RESIZER ::::::::::::::::::::::::::::::::::::::::::::::::")
print("_____________________________      BY  HMC            ________________________________________________")

import cv2

# configurable parameters
source = "Harsh.JPG"
destination = 'newImage.png'
scale_percent = 50

src = cv2.imread("Harsh.JPG", cv2.IMREAD_UNCHANGED)
# cv2.imshow("title", image)

# Calculate the percent of the original dimension
new_width =int(src.shape[1] * scale_percent/100)
new_height =int(src.shape[0] * scale_percent/100)

# resize image
output = cv2.resize(src,(new_width,new_height))

cv2.imwrite(destination,output)
print("Image resized succesfully !")


# cv2.waitKey(0)
# cv2.destroyAllWindows()
