from PIL import Image


def sort_images_bydatetaken(files):
    exifs = []
    for index, file in enumerate(files):
        try:
            image = Image.open(file)
            xf = image._getexif()[36867]
            exifs.append(xf)
        except OSError:
            exifs.append('')
            print('Skipping {}'.format(file))
    sorted_files = [x for _, x in sorted(zip(exifs, files))]
    return sorted_files


def get_groups(bit_diffs, threshold):
    """
    Method that detects groups of interest on the bit_diffs sequence.
    A sequence in considered of interest if
    - succesive elements differ no more than the threshold
    - no element is bigger than the threshold
    - it contains at least 5 elements
    Each group is a dict with keys:
    - "values": holds the bit_diffs
    - "start_index": holds the index of the first value on the bit_diffs list

    :param bit_diffs: List holding the bit_diffs (hamming distance values)
    :return: groups of interest
    """
    groups = [{"start_index": 0, "values": [bit_diffs[0]]}]
    for index, x in enumerate(bit_diffs[1:]):
        if abs(x - groups[-1].get("values")[-1]) < threshold:
            groups[-1]["values"].append(x)
        else:
            groups.append({"start_index": index, "values": [x]})

    # keep just the sequences that satisfy our conditions
    keep_groups = [group for group in groups
                   if all(element < threshold for element in group["values"])
                   and len(group["values"]) >= 5]
    return keep_groups
