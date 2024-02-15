import cv2
import numpy as np
import os

import pandas as pd


# Function to resize and normalize an image
def preprocess_image(image_path):
    # Read the image in color format
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)

    # Resize the image to a square with a side length of 128 pixels
    resized_img = cv2.resize(img, (128, 128))

    # Convert the image to grayscale
    gray_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)

    # Normalize the pixel values to the range [0, 255]
    normalized_img = cv2.normalize(gray_img, None, 0, 255, cv2.NORM_MINMAX)

    # Save the preprocessed image for debugging
    save_path = "C:\\Users\\filip\\PycharmProjects\\Siamese-network-on-MNIST-PyTorch\\debug1"
    debug_save_path = os.path.join(save_path, os.path.basename(image_path).split(".")[0] + ".png")

    cv2.imwrite(debug_save_path, normalized_img)

    # Flatten the 2D array to a 1D array
    flattened_img = normalized_img.flatten()

    return flattened_img

# Function to process all .jpg files in a folder
def process_images_folder(folder_path):
    image_data = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".png"):
            image_path = os.path.join(folder_path, filename)
            flattened_img = preprocess_image(image_path)
            image_data.append(flattened_img)

    columns = [f"{i // 128 + 1}x{i % 128 + 1}" for i in range(128 * 128)]
    df = pd.DataFrame(image_data, columns=columns)

    csv_file_path = "C:\\Users\\filip\\PycharmProjects\\Siamese-network-on-MNIST-PyTorch\\croppedImages.csv"
    df.to_csv(csv_file_path, index=False)
    print(f"CSV file '{csv_file_path}' created successfully.")

# Specify the folder path containing the .png files
folder_path = "C:\\Users\\filip\\FIIT\\Bakalarka\\frame_sample_wrapped\\cropped_images"

# Process all images in the specified folder
process_images_folder(folder_path)
