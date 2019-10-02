import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from skimage import io
from skimage.measure import label, regionprops
from skimage.morphology import closing, square
from skimage.color import label2rgb
from skimage.filters import threshold_otsu
from skimage.segmentation import clear_border

<<<<<<< HEAD
image = io.imread('1.jpg', as_grey=True)
=======
image = io.imread('/home/sh/PycharmProjects/sunspots/data/hmi sunspots/1.tif', as_grey=True)
>>>>>>> 2f795c852f119d824a141e8fd942e7fc45697713


#bw = closing(image > thresh, square(3))
bw = closing(image < 0.5, square(3))


# remove artifacts connected to image border
cleared = clear_border(bw)

label_image = label(cleared)
image_label_overlay = label2rgb(label_image, image=image)

fig, ax = plt.subplots(figsize=(10, 6))
ax.imshow(image_label_overlay)

for region in regionprops(label_image):
	# take regions with large enough areas
	if region.area >= 50:
		print(region.area)
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

ax.set_axis_off()
plt.tight_layout()
plt.show()
