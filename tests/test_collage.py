"""Test for collage.py."""
from collamake.collage import Collage


class TestCollage:
    """Test Collage class."""

    def test_split_box(self) -> None:
        """Test Collage._split_box."""
        b = (0, 0, 100, 10)
        b1, b2 = Collage._split_box(b)
        assert b1 == (0, 0, 50, 10)
        assert b2 == (51, 0, 100, 10)
