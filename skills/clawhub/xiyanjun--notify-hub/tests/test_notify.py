"""notify-hub 核心逻辑单元测试（标准库 unittest，零第三方依赖）。

运行：python3 -m unittest discover -s tests -v
"""
import os
import sys
import time
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from core import message
from core import router
from channels.feishu import FeishuChannel
from channels.dingtalk import DingtalkChannel
from channels.email import EmailChannel, _md_to_html, _safe_url


class TableTest(unittest.TestCase):
    def test_table_to_markdown(self):
        out = message.table_to_markdown(["代码", "名称"], [["600583", "海油工程"]])
        self.assertIn("| 代码 | 名称 |", out)
        self.assertIn("| 600583 | 海油工程 |", out)
        self.assertIn(":---", out)

    def test_table_to_text(self):
        out = message.table_to_text(["a", "b"], [["1", "2"]])
        lines = out.split("\n")
        self.assertEqual(len(lines), 3)  # header + separator + row
        self.assertIn("a", lines[0])
        self.assertIn("1", lines[2])


class RouterTest(unittest.TestCase):
    def test_single(self):
        self.assertEqual(router.parse_targets("feishu:群A"), [("feishu", "群A")])

    def test_broadcast(self):
        self.assertEqual(router.parse_targets("feishu:群A,wecom:群B"),
                         [("feishu", "群A"), ("wecom", "群B")])

    def test_no_target(self):
        self.assertEqual(router.parse_targets("feishu"), [("feishu", None)])

    def test_empty(self):
        self.assertEqual(router.parse_targets(""), [])


class SignTest(unittest.TestCase):
    def test_feishu_sign(self):
        # 向量由标准库独立算出：key=timestamp+\n+secret，对空串 HMAC-SHA256 后 base64
        self.assertEqual(FeishuChannel._sign("1234567890", "test_secret"),
                         "3H7JNC7ltBAwibQHFO1KFVN9HTkLtm2virjdsmGcAzw=")

    def test_dingtalk_sign(self):
        # 向量由标准库独立算出：key=secret，msg=timestamp+\n+secret，base64 后 urlencode
        self.assertEqual(DingtalkChannel._sign("1234567890000", "test_secret"),
                         "aE2sGldS6IQKMMyKsXW2e7IOt%2BN6d34%2FPQxwacVycCc%3D")


class EmailTest(unittest.TestCase):
    def test_md_to_html_escapes(self):
        self.assertEqual(_md_to_html("<script>alert(1)</script>"),
                         "&lt;script&gt;alert(1)&lt;/script&gt;")

    def test_md_bold(self):
        self.assertEqual(_md_to_html("**加粗**"), "<b>加粗</b>")

    def test_safe_url_https(self):
        self.assertEqual(_safe_url("https://example.com/x?a=1"),
                         "https://example.com/x?a=1")

    def test_safe_url_javascript_blocked(self):
        self.assertEqual(_safe_url("javascript:alert(1)"), "#")

    def test_render_card_escapes_content(self):
        ch = EmailChannel({})
        out = ch.render_card({"kind": "card", "title": "T", "sections": [
            {"type": "markdown", "content": "<b>raw</b>"},
        ]})
        self.assertIn("&lt;b&gt;raw&lt;/b&gt;", out["body"])
        self.assertNotIn("<b>raw</b>", out["body"])


class FeishuColorTest(unittest.TestCase):
    def test_valid_color(self):
        ch = FeishuChannel({})
        card = ch.render_card({"kind": "card", "title": "T", "color": "green", "sections": []})
        self.assertEqual(card["card"]["header"]["template"], "green")

    def test_invalid_color_falls_back(self):
        ch = FeishuChannel({})
        card = ch.render_card({"kind": "card", "title": "T", "color": "hacker", "sections": []})
        self.assertEqual(card["card"]["header"]["template"], "blue")

    def test_default_color(self):
        ch = FeishuChannel({})
        card = ch.render_card({"kind": "card", "title": "T", "sections": []})
        self.assertEqual(card["card"]["header"]["template"], "blue")


class ThrottleTest(unittest.TestCase):
    def test_first_call_no_wait(self):
        ch = EmailChannel({})
        ch.rate_per_min = 60000  # interval 极小，验证首轮不阻塞
        start = time.time()
        ch._throttle()
        self.assertLess(time.time() - start, 0.1)
        self.assertGreater(ch._last_send, 0)


if __name__ == "__main__":
    unittest.main()
