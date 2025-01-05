import os

from tml.tml import Teemap
from tml.constants import TML_DIR

map_path = os.path.join(TML_DIR, 'maps', 'dm1')
t = Teemap(map_path)

images_dir = 'images'
os.makedirs(images_dir, exist_ok=True)

for image in t.images:
    image_name = image.name + '.png'
    image.save(os.path.join(images_dir, image_name))

print(f'Extracted {len(t.images)} images.')
