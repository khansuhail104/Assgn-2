import sys
from imageops.DSImage import MyImage as MyImage
from dpcourse import Stack
from dpcourse import Queue
import random


class RegionAnalysis:

    def __init__(self, image):
        try:
            if not isinstance(image,MyImage):
                raise TypeError
        except TypeError:
            print('Image has to be type MyImage.')
            sys.exit(2)
        try:
            if image.get_channels() != 1:
                raise TypeError
        except TypeError:
            print("Image has to be binary image.")
            sys.exit(2)
        self.binary_image = image
        self.height = image.get_height()
        self.width = image.get_width()
        self.label_image = MyImage()
        self.label_image.new_image(self.width, self.height, [0, 0, 0])
        self.num_regions = 0

    def get_binary_image(self):
        return self.binary_image

    def get_label_image(self):
        return self.label_image

    def get_num_regions(self):
        return self.num_regions

    def connected_components_stack(self):
        # Implement connected component analysis using Stack
        pass

    def connected_components_queue(self):
        # Implement connected component analysis using Queue
        pass


