"""Run with the converter's dependencies: uv run --with ... python this_file."""

import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from bs4 import BeautifulSoup

import md2twitter as converter


class ArticleExportTests(unittest.TestCase):
    def test_article_assembly_preserves_code_and_order(self):
        with tempfile.TemporaryDirectory(dir="/tmp/opencode") as tmp:
            root = Path(tmp)
            source = root / "article.md"
            (root / "figure.png").write_bytes(b"fixture")
            source.write_text(
                '# A title\n\n**Opening** [link](other.md)\nsoft line\n\n'
                '![Figure](figure.png)\n\n'
                '```sh\nprintf "<tag> & text"\n  echo indented\n\n'
                'echo after-blank\n```\n\n'
                '- Nested example\n\n'
                '    ```sql\n    select 1;\n    ```\n\n'
                '| A | B |\n| --- | --- |\n| 1 | 2 |\n\n'
                '```\nresult  ok\n```\n\nClosing.\n',
                encoding="utf-8",
            )
            out = root / "article-twitter-article.html"
            with patch.object(converter, "render_block_png") as render:
                with contextlib.redirect_stdout(io.StringIO()):
                    converter.export_article(source, out, article_code="native")
                render.assert_called_once()
            body = BeautifulSoup(out.read_text(), "html.parser")
            self.assertIsNone(body.find("h1"))
            self.assertIsNone(body.find("pre"))
            self.assertIsNone(body.find("img"))
            self.assertIsNone(body.find("table"))
            self.assertEqual(body.find("strong").text, "Opening")
            self.assertIsNotNone(body.find("br"))
            self.assertEqual(body.find("a")["href"], converter.BASE + "other.md")
            manifest = json.loads(out.with_suffix(".json").read_text())
            self.assertEqual(manifest["title"], "A title")
            items = manifest["items"]
            self.assertEqual([i["id"] for i in items],
                             ["IMAGE-01", "CODE-01", "CODE-02", "TABLE-01", "CODE-03"])
            blocks = [i for i in items if i["kind"] == "code"]
            self.assertEqual([i["language"] for i in blocks], ["Bash", "SQL", "Plain text"])
            self.assertEqual(Path(blocks[0]["path"]).read_text(),
                             'printf "<tag> & text"\n  echo indented\n\necho after-blank')
            self.assertEqual(Path(blocks[1]["path"]).read_text(), "select 1;")
            self.assertEqual(Path(blocks[2]["path"]).read_text(), "result  ok")
            for item in items:
                self.assertEqual(body.get_text().count(item["id"]), 1)

    def test_article_cannot_post(self):
        for flags in (["--post"], ["--limit", "25000"], ["--at", "1"],
                      ["--tables", "image"], ["--out", "body.txt"]):
            with patch("sys.argv", ["md2twitter", "missing.md", "--article", *flags]):
                with contextlib.redirect_stderr(io.StringIO()):
                    with self.assertRaises(SystemExit) as error:
                        converter.main()
                self.assertEqual(error.exception.code, 2)

    def test_default_fences_preserve_code_without_placeholders(self):
        with tempfile.TemporaryDirectory(dir="/tmp/opencode") as tmp:
            source = Path(tmp) / "source.md"
            source.write_text('# Title\n\nBefore\n\n```sh\nprintf "<tag> & text"\n'
                              '  echo indented\n\n  echo done\n```\n\nAfter\n')
            out = Path(tmp) / "article.html"
            with contextlib.redirect_stdout(io.StringIO()):
                converter.export_article(source, out)
            body = BeautifulSoup(out.read_text(), "html.parser")
            code = body.find("pre").find("code")
            self.assertEqual(code["class"], ["language-bash"])
            self.assertEqual(code.get_text(), '```bash\nprintf "<tag> & text"\n'
                             '  echo indented\n\n  echo done\n```')
            self.assertNotIn("CODE-01", body.get_text())
            self.assertEqual(len(body.find_all("p")), 2)
            manifest = json.loads(out.with_suffix(".json").read_text())
            self.assertEqual(manifest["articleCode"], "fenced")
            guide = out.with_name("article-instructions.md").read_text()
            self.assertNotIn("Choose Insert → Code.", guide)

    def test_missing_image_is_not_silently_dropped(self):
        with tempfile.TemporaryDirectory(dir="/tmp/opencode") as tmp:
            source = Path(tmp) / "source.md"
            source.write_text("# Title\n\n![Missing](absent.png)\n")
            with self.assertRaisesRegex(ValueError, "Missing article image"):
                converter.export_article(source, Path(tmp) / "out.html")

    def test_long_post_stays_plain_text(self):
        posts, _ = converter.convert("# Title\n\nHello **world**.\n\n```sh\necho ok\n```",
                                     Path("."), limit=25000)
        self.assertEqual(len(posts), 1)
        self.assertEqual(posts[0].text, "Title\nHello world.\necho ok")


if __name__ == "__main__":
    unittest.main()
