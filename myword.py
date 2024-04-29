#generate the logo 
import pyfiglet
text = pyfiglet.figlet_format("ZWN _ CRAWL")
print(text)

import itertools
from tqdm import tqdm

# Get user input
com_char = input("[+]Enter a character to combine: ")
min_len = int(input("[+]Enter the minimum length: "))
max_len = int(input("[+]Enter the maximum length: "))
file = input("[+]Enter the file name: ")

# Open file in append mode
with open(file +".txt","a") as file_open:
    # Generate all combinations with replacements using itertools.product
    for i in tqdm(range(min_len, max_len+1), desc="Generating"):
        for j in itertools.product(com_char, repeat=i):
            # Write each combination to the file
            file_open.write("".join(j) + "\n")

print("Task complete")
