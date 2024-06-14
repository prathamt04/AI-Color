import cv2
import numpy as np

def grayscale_to_color(image_path, output_path):
    # Read the grayscale image
    gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Check if the image was successfully read
    if gray_image is None:
        print(f"Error: Unable to read image from {image_path}")
        return None

    # Create an empty color image
    color_image = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)

    # Define color mapping
    
    def get_color(value):       
        if value < 28:
            return (128, 0, 128)  # Purple
        elif value < 56:
            return (75, 0, 130)  # Indigo
        elif value < 84:
            return (0, 0, 255)  # Blue
        elif value < 112:
            return (0, 255, 255)  # Cyan
        elif value < 140:
            return (0, 255, 0)  # Green
        elif value < 168:
            return (173, 255, 47)  # Green Yellow
        elif value < 196:
            return (255, 255, 0)  # Yellow
        elif value < 224:
            return (255, 165, 0)  # Orange
        elif value < 252:
            return (255, 69, 0)  # Orange Red
        else:
            return (255, 0, 0)  # Red



    # Apply color mapping
    for i in range(gray_image.shape[0]):
        for j in range(gray_image.shape[1]):
            color_image[i, j] = get_color(gray_image[i, j])

    # Save the colorized image
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
