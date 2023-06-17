#Image Resizer

This code is a simple image resizing script using the OpenCV library. It allows you to resize an image by specifying a scale percentage. The resized image is saved to a new file.

#Usage

Make sure you have the necessary dependencies installed, particularly OpenCV for Python.

Run the script in a Python environment.

Configure the following parameters according to your needs:

source: The path to the source image file.
destination: The path where the resized image will be saved.
scale_percent: The percentage of scaling to be applied to the image.
Execute the script.

The resized image will be saved to the specified destination path.

Example

```import cv2

source = "Harsh.JPG"
destination = 'newImage.png'
scale_percent = 50

src = cv2.imread(source, cv2.IMREAD_UNCHANGED)

new_width = int(src.shape[1] * scale_percent/100)
new_height = int(src.shape[0] * scale_percent/100)

output = cv2.resize(src, (new_width, new_height))

cv2.imwrite(destination, output)
print("Image resized successfully!")
```

Dependencies
OpenCV for Python
Note
The script currently comments out the display of the resized image using cv2.imshow() and the wait key functionality. If you want to view the resized image, uncomment the relevant lines (cv2.imshow(), cv2.waitKey(), and cv2.destroyAllWindows()).

Ensure that you have the appropriate permissions to read the source image file and write to the destination path.