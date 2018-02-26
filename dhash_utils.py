import dhash
from PIL import Image


def compute_hashes(files):
    # compute hash for the images
    hashes = []
    for index, file in enumerate(files):
        try:
            image = Image.open(file)
            row, col = dhash.dhash_row_col(image)
            img_hash = dhash.format_hex(row, col)
            hashes.append(img_hash)
        except OSError:
            print("Can't read this file: {} - removing from the list".format(file))
            del files[index]
    print(hashes)
    return hashes


def compute_hamming_dist(hashes):
    bit_diffs = []

    for index, hash_elem in enumerate(hashes[:-1]):
        bit_diff = dhash.get_num_bits_different(int(hash_elem, 16), int(hashes[index + 1], 16))
        bit_diffs.append(bit_diff)
    print(bit_diffs)
    return bit_diffs
