import cv2
import numpy as np

def grayscale_to_color(image_path, output_path):
    gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if gray_image is None:
        print(f"Error: Unable to read image from {image_path}")
        return None

   
    color_image = cv2.applyColorMap(gray_image, cv2.COLORMAP_JET)
    # Other colormaps can be used, such as COLORMAP_HOT, COLORMAP_COOL, COLORMAP_RAINBOW, etc.

    
    success = cv2.imwrite(output_path, color_image)
    if not success:
        print(f"Error: Unable to save image to {output_path}")
    else:
        print(f"Colorized image saved to {output_path}")
    
    return color_image

if __name__ == "__main__":
    input_path = input("Enter the path to the grayscale image: ")
    output_path = input("Enter the path to save the colored image: ")
    
    colored_image = grayscale_to_color(input_path, output_path)
    
    if colored_image is not None:
        cv2.imshow('Colored Image', colored_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
