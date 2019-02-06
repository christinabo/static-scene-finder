from static_scene_finder import static_scene_finder
from PIL import Image
import dhash

imgpath1 = '/home/cbb10g/Documents/imcd_data/lifeloggers_static_scenes/imcd_1413401/2/MTQxMzQwMTIwMTUtMDgtMTQgMTQ6MTU6MDguMjM5MjMzNDM3ICswMTAwIEJTVA==.jpg'
imgpath2 = '/home/cbb10g/Documents/imcd_data/lifeloggers_static_scenes/imcd_1413401/2/MTQxMzQwMTIwMTUtMDgtMTQgMTQ6MTU6MDcuOTc2NzgwNDcgKzAxMDAgQlNU.jpg'

image1 = Image.open(imgpath1)
image2 = Image.open(imgpath2)

row, col = dhash.dhash_row_col(image1)
img_hash1 = dhash.format_hex(row, col)

row, col = dhash.dhash_row_col(image2)
img_hash2 = dhash.format_hex(row, col)

bit_diff = dhash.get_num_bits_different(int(img_hash1, 16), int(img_hash2, 16))
print(img_hash1)
print(img_hash2)
print(bit_diff)

sequences = static_scene_finder('/home/cbb10g/Documents/imcd_data/lifeloggers_images/imcd_1500202/')
