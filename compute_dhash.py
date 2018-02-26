import dhash
from PIL import Image


image = Image.open('/home/cbb10g/Documents/imcd_data/lifeloggers_images/imcd_1620601/B00000840_21I7JV_20151113_101252E.JPG')
row, col = dhash.dhash_row_col(image)
hash1 = dhash.format_hex(row, col)
print(hash1)
image2 = Image.open('/home/cbb10g/Documents/imcd_data/lifeloggers_images/imcd_1620601/B00000872_21I7JV_20151113_103228E.JPG')
row, col = dhash.dhash_row_col(image2)
hash2 = dhash.format_hex(row, col)
print(hash2)
result = dhash.get_num_bits_different(int(hash1, 16), int(hash2, 16))
print(result)
