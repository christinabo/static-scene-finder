import os
import utils
import dhash_utils


if __name__ == '__main__':
    # load the images
    root_folder = '/home/cbb10g/Documents/imcd_data/lifeloggers_images/imcd_1091201/'
    files_list = [root_folder + f for f in os.listdir(root_folder) if f.endswith('.jpg')]
    # files_list.sort()
    files_list = utils.sort_images_bydatetaken(files_list)
    # compute hashes of the images
    hashes = dhash_utils.compute_hashes(files_list)

    # get bits differences (hamming distances of consecutive image pairs)
    bit_diffs = dhash_utils.compute_hamming_dist(hashes)

    # detect the static scenes based on the bit_diffs list
    static_scenes = utils.get_groups(bit_diffs, threshold=7)

    # find the sequences of the actual images
    sequences = []
    for group in static_scenes:
        sequences.append(files_list[group["start_index"]:group["start_index"] + len(group["values"]) + 1])

    for sequence in sequences:
        print(sequence)
        print(len(sequence))
