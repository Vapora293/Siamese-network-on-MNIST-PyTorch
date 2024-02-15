# import pandas as pd
#
# # Read the CSV file
# df = pd.read_csv('mnist_train.csv')
#
# # Extract all columns except the first one (C1)
# df = df.iloc[:, 1:]
#
# # Save the modified DataFrame to trainMNIST.csv
# df.to_csv('trainMNIST.csv', index=False)

import pandas as pd

# Read the CSV file
df = pd.read_csv('mnist_train.csv')

# Check if the DataFrame has rows
if not df.empty:
    # Extract all columns except the first one (C1)
    df = df["label"]

    # Check if the DataFrame has rows after extraction
    if not df.empty:
        # Save the modified DataFrame to trainMNIST.csv
        df.to_csv('trainMNISTlabels.csv', index=False)
    else:
        print("DataFrame is empty after column extraction.")
else:
    print("DataFrame is empty. Cannot proceed.")

