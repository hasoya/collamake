"""This module includes the class to handle Collage to make images."""
import math
from pathlib import Path
from typing import List, Tuple

import yaml

from collamake.collage import Collage
from collamake.exceptions import NotSupportedNumPics


class CollaMake:
    """Generates collage images based on a given config file."""

    def __init__(self, config_path: Path) -> None:
        """Load a config file."""
        with config_path.open(encoding="utf-8") as f:
            self.config = yaml.safe_load(f)

    @staticmethod
    def _adjust_len_mod(num_pics: int, paths: List[str]) -> List[str]:
        """Return a list of path expanded to fit split_num."""
        mod = len(paths) % num_pics
        if mod == 0:  # Nothing to do.
            return paths

        return paths + [paths[-1]] * (num_pics - mod)

    def generate(self) -> None:
        """Make and save collage images."""
        img_size: Tuple[int, int] = tuple(self.config["size"])
        output_dir = Path(self.config["output_dir"])
        output_dir.mkdir(parents=True, exist_ok=True)

        for c in self.config["input_dir"]:
            dir = Path(c["path"])
            num_pics = c["num_pics"]
            if not dir.is_dir():
                raise NotADirectoryError("An input path must be a directory.")
            if not math.log2(num_pics).is_integer():
                raise NotSupportedNumPics("The number of pics must be the power of two.")

            img_paths = [str(f.resolve()) for f in dir.iterdir() if f.is_file()]
            img_paths = self._adjust_len_mod(num_pics, img_paths)

            for i in range(0, len(img_paths), num_pics):
                target_paths = img_paths[i : i + num_pics]
                clg = Collage(img_size, self.config["margin"])
                clg.make(target_paths)
                output_path = output_dir / f"photo_{num_pics}_{int(i / num_pics)}.jpg"
                clg.save(output_path)
