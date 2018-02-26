import dhash
from PIL import Image


image = Image.open('/home/cbb10g/Documents/imcd_data/lifeloggers_images/imcd_1620701/B00000682_21I71I_20150607_154657E.JPG')
row, col = dhash.dhash_row_col(image)
hash1 = dhash.format_hex(row, col)
print(hash1)
image2 = Image.open('/home/cbb10g/Documents/imcd_data/lifeloggers_images/imcd_1620701/B00000683_21I71I_20150607_154703E.JPG')
row, col = dhash.dhash_row_col(image2)
hash2 = dhash.format_hex(row, col)
print(hash2)
result = dhash.get_num_bits_different(int(hash1, 16), int(hash2, 16))
print(result)
