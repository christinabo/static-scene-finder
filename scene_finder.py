import os
import dhash
from PIL import Image
from itertools import cycle

if __name__ == '__main__':
    # load the images
    root_folder = '/home/cbb10g/Documents/imcd_data/lifeloggers_images/imcd_1620701/'
    files_list = [f for f in os.listdir(root_folder) if f.endswith('.JPG')]
    files_list.sort()

    # compute hash for the images
    hashes = []
    for index, file in enumerate(files_list):
        try:
            image = Image.open(root_folder+file)
            row, col = dhash.dhash_row_col(image)
            img_hash = dhash.format_hex(row, col)
            hashes.append(img_hash)
        except OSError:
            print("Can't read this file: {} - removing from the list".format(file))
            del files_list[index]
    print(hashes)

    # get bits differences
    bit_diffs = []

    for index, hash_elem in enumerate(hashes[:-1]):
        bit_diff = dhash.get_num_bits_different(int(hash_elem, 16), int(hashes[index+1], 16))
        bit_diffs.append(bit_diff)
    print(bit_diffs)

    groups = [{"start_index": 0, "values": [bit_diffs[0]]}]
    for index, x in enumerate(bit_diffs[1:]):
        if abs(x - groups[-1].get("values")[-1]) < 7:
            groups[-1]["values"].append(x)
        else:
            groups.append({"start_index": index, "values": [x]})

    # discard unwanted scenes
    keep_groups = [group for group in groups if all(element < 7 for element in group["values"])]

    # find the sequences of the images
    sequences = []
    for group in keep_groups:
        print(group)
        print(len(group["values"]))
        sequences.append(files_list[group["start_index"]:group["start_index"] + len(group["values"]) + 1])
    for sequence in sequences:
        print(sequence)
        print(len(sequence))
    # get the actual names of the images corresponding to the groups



