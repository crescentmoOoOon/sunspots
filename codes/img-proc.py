import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from skimage import io
from skimage.measure import label, regionprops
from skimage.morphology import closing, square
from skimage.color import label2rgb
from skimage.segmentation import clear_border

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(BASE_DIR, 'data/hmi-sunspots/')
imageList = os.listdir(path)


def img_proc(image):
    image = io.imread(path + image, as_grey=True)
    # bw = closing(image > thresh, square(3))
    bw = closing(image < 0.4, square(3))
    # remove artifacts connected to image border
    cleared = clear_border(bw)

    label_image = label(cleared)
    image_label_overlay = label2rgb(label_image, image=image)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.imshow(image_label_overlay)
    # result = {}
    for region in regionprops(label_image):
        # take regions with large enough areas
        if region.area >= 100:
            area = (region.area)
            print(area)
            # draw rectangle around segmented coins
            minr, minc, maxr, maxc = region.bbox
            rect = mpatches.Rectangle(
                (minc, minr),
                maxc - minc,
                maxr - minr,
                fill=False, edgecolor='red',
                linewidth=2
            )
            ax.add_patch(rect)
            # result[image] = list(area)
    # print(result)
    ax.set_axis_off()
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    for file in imageList:
        img_proc(file)
