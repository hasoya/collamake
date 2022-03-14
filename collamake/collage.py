"""This module includes class to make collage."""
from pathlib import Path
from typing import List, Tuple

from PIL import Image

Box = Tuple[int, int, int, int]


class Collage:
    """Make and save a collage image from listed images."""

    def __init__(self, size: Tuple[int, int], margin: int) -> None:
        """Initialize params."""
        self.img_size = size
        self.img = Image.new("RGB", (size[0], size[1]))
        self.margin = margin

    @staticmethod
    def _split_box(box: Box) -> Tuple[Box, Box]:
        """Return a tuple of box by splitting longer side."""
        box_w = box[2] - box[0]
        box_h = box[3] - box[1]

        if box_w > box_h:
            split_point = int((box[2] - box[0]) / 2)
            box1 = (box[0], box[1], split_point, box[3])
            box2 = (split_point + 1, box[1], box[2], box[3])
        else:
            split_point = int((box[3] - box[1]) / 2)
            box1 = (box[0], box[1], box[2], split_point)
            box2 = (box[0], split_point + 1, box[2], box[3])

        return box1, box2

    def _collage(self, img_paths: List[str], box: Box) -> None:
        """Paste resized images in the given box by recursive manner."""
        if len(img_paths) == 1:  # Paste an image.
            with Image.open(img_paths[0]) as im:
                img_w, img_h = im.size
                box_w = box[2] - box[0] - 2 * self.margin
                box_h = box[3] - box[1] - 2 * self.margin

                # Rotate if necessary.
                if (img_w - img_h) * (box_w - box_h) < 0:  # Image orientation is different.
                    p = im.rotate(90, expand=True)
                    img_w, img_h = p.size
                else:
                    p = im

                # Calculate the box and resize an image.
                w_ratio = box_w / img_w
                h_ratio = box_h / img_h
                resize_ratio = min(w_ratio, h_ratio)
                resized_img = p.resize((int(img_w * resize_ratio), int(img_h * resize_ratio)))

                dest_box = (box[0] + self.margin, box[1] + self.margin)
                self.img.paste(resized_img, dest_box)
        else:  # Split a box.
            box1, box2 = self._split_box(box)
            middle_idx = int(len(img_paths) / 2)  # The length of image paths is always even.
            self._collage(img_paths[:middle_idx], box1)
            self._collage(img_paths[middle_idx:], box2)

    def make(self, img_paths: List[str]) -> None:
        """Make a collage image combined given images."""
        self._collage(img_paths, (0, 0, self.img_size[0], self.img_size[1]))

    def save(self, output_path: Path) -> None:
        """Save a collage image."""
        self.img.save(output_path)
