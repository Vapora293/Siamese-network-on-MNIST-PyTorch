import os
import cv2


def calculate_average_size(directory_path):
    total_size = 0
    count = 0
    larger_than_256_count = 0

    for file_name in os.listdir(directory_path):
        if file_name.lower().endswith(".png"):
            image_path = os.path.join(directory_path, file_name)
            image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

            if image is not None:
                height, width = image.shape[:2]
                total_size += height * width
                count += 1

                if height > 30 and width > 30:
                    larger_than_256_count += 1

    if count == 0:
        print("No .jpg files found in the specified directory.")
        return

    average_size = total_size / count
    percentage_larger_than_256 = (larger_than_256_count / count) * 100

    print(f"Average size of pictures: {average_size} pixels")
    print(f"Percentage of pictures larger than 256x256 pixels: {percentage_larger_than_256}%")


# Replace 'your_directory_path' with the actual path to your directory
directory_path = 'C:\\Users\\filip\\FIIT\\Bakalarka\\frame_sample_wrapped\\cropped_images'
calculate_average_size(directory_path)
