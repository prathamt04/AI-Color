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

    # Define color mapping: You can customize this as needed
    def get_color(value):
        if value < 85:
            return (255, 0, 0)  # Blue
        elif value < 170:
            return (0, 255, 0)  # Green
        else:
            return (0, 0, 255)  # Red

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
        # Display the image using OpenCV (optional)
        cv2.imshow('Colored Image', colored_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
