import os
import utils
import dhash_utils


def static_scene_finder(folder_path):
    print('Detecting static scenes on folder: ', folder_path)
    files_list = [folder_path+f for f in os.listdir(folder_path)
                  if f.endswith('.jpg') or f.endswith('.JPG') or f.endswith('.png')]
    print('Found {} files'.format(files_list))

    # sort files by their date taken
    files_list = utils.sort_images_bydatetaken(files_list)

    # compute hashes of the images
    hashes = dhash_utils.compute_hashes(files_list)
    print('Hashes', hashes)
    # get bits differences (hamming distances of consecutive image pairs)
    bit_diffs = dhash_utils.compute_hamming_dist(hashes)
    print('Hamming distances', bit_diffs)

    if not bit_diffs:
        return []
    # detect the static scenes based on the bit_diffs list
    static_scenes = utils.get_groups(bit_diffs, threshold=6)

    # find the sequences of the actual images
    sequences = []
    for group in static_scenes:
        sequences.append(files_list[group["start_index"]:group["start_index"] + len(group["values"]) + 1])

    return sequences







