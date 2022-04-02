import shutil
import unittest
import tempfile
import os
from pathlib import Path


class ImageSourceTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp_dir = tempfile.mkdtemp()
        tmp_file_path = os.path.join(self.tmp_dir, 'file')
        self.tmp_file = Path(tmp_file_path)
        self.tmp_file.touch()

    def tearDown(self) -> None:
        self.tmp_file.unlink()
        shutil.rmtree(self.tmp_dir)

    def test_image_source(self):
        from lgtm.image_source import image_source
        from lgtm.image_source import RemoteImage
        from lgtm.image_source import LocalImage
        from lgtm.image_source import KeywordImage

        # 入力値と期待値
        keyword_expected = [(str(self.tmp_file), LocalImage),
                            ('http://example.com', RemoteImage),
                            ('https://example.com', RemoteImage),
                            ('keyword', KeywordImage)]

        # テスト実行
        for keyword, expected in keyword_expected:
            with self.subTest(keyword=keyword, expected=expected):
                self.assertEqual(type(image_source(keyword)), expected)
