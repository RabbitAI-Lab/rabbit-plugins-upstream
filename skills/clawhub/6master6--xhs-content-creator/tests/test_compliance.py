"""Tests for the 7-rule content constitution in SKILL.md §1.5.

Each test exercises one rule on synthetic inputs so regressions
(e.g. a banned word list being accidentally widened or narrowed)
are caught at the unit level. Fixtures use generic placeholder
locations ("示例公园", "示例城市") so the suite is portable
across skill maintainers and contains no end-user content.
"""

import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from validate_content import validate, check_title, check_body, check_topics, check_images


# Synthetic fixtures — generic placeholder locations.
VALID_BODY = (
    "示例公园入口处有一座古朴的石门，是这座示例城市的标志性建筑。\n\n"
    "先沿着示例公园环线走一圈，步道在草坪之间弯成一条软软的线，乔木列阵，棕榈成荫，蹬两步就漂起来——风从耳旁掠过，带着树叶的青涩味和湖水反光的凉。走到古朴石门下抬头看，七层仿古塔在蓝天下安静矗立，红柱黛瓦层层而上，像一支千年不灭的烛。\n\n"
    "停车走向示例公园深处，七层仿古塔在蓝天下安静矗立，红柱黛瓦层层而上，像一支千年不灭的烛。绕塔一圈，脚步自然就慢下来，连呼吸都跟着轻。塔身的红柱在阳光下发亮，瓦顶的蓝灰色调与天空融为一体。\n\n"
    "登上塔旁的山坡俯瞰全貌——示例城市在远处连成一片，楼群的玻璃幕墙把阳光切成碎片撒在水面上。再登上示例水库往远处望，湖面如镜，远山如黛，层云铺满半边天空，几座高压电塔沿着山脊线静静延伸，反而给画面添了一分郊野的粗犷。\n\n"
    "山脚有个仿古亭子，瓦檐深褐，栏杆橙红，坐在里面看水光粼粼。换个方向看，又是满眼的绿——荔枝林、龙眼林连成一片，深浅交错，像城市版的小森林。原来城市可以这么安静，不用排队、不用预约、也不用门票，只用在某个周末开车出来，推开一道山门。"
)

VALID_TITLE = "🌄 示例公园·城市远方"

VALID_TOPICS = ["#示例公园", "#示例城市", "#周末漫步", "#城市郊野", "#户外徒步"]


class TestTitleRule(unittest.TestCase):
    def test_under_limit_passes(self):
        v = check_title(VALID_TITLE)
        self.assertEqual(v, [])

    def test_over_limit_flagged(self):
        v = check_title("🌄 " + "啊" * 30)
        self.assertTrue(any(x["rule"] == "title.length" for x in v))

    def test_100pct_banned(self):
        v = check_title("示例城市100%好玩")
        self.assertTrue(any(x["rule"] == "title.banned_phrase" for x in v))

    def test_vx_banned(self):
        v = check_title("示例城市+vx")
        self.assertTrue(any(x["rule"] == "title.banned_phrase" for x in v))

    def test_guarantee_banned(self):
        v = check_title("保证X天瘦X")
        self.assertTrue(any(x["rule"] == "title.banned_phrase" for x in v))

    def test_no_keyword_in_first_8(self):
        # Pure ASCII title without CJK keyword in first 8.
        v = check_title("Beautiful park")
        self.assertTrue(any(x["rule"] == "title.keyword_position" for x in v))


class TestBodyRule(unittest.TestCase):
    def test_valid_body_passes(self):
        v = check_body(VALID_BODY)
        # VALID_BODY has 5 paragraphs each with a location hint → no violations.
        self.assertEqual(v, [])

    def test_body_too_short(self):
        v = check_body("示例公园很美。" * 5)
        self.assertTrue(any(x["rule"] == "body.length" for x in v))

    def test_body_opening_no_location(self):
        # Opening paragraph has no location hint.
        body = (
            "这是一个很美的周末。\n\n"
            "示例公园很美，水波粼粼。\n\n"
            "示例塔很美，红柱黛瓦。\n\n"
            "山脚亭子很美。\n\n"
            "原来示例城市这么安静。"
        )
        v = check_body(body)
        self.assertTrue(any(x["rule"] == "body.opening_location" for x in v))

    def test_body_too_many_paragraphs(self):
        body = "\n\n".join(["示例公园旁有一段。" + "a" * 60] * 7)
        v = check_body(body)
        self.assertTrue(any(x["rule"] == "body.paragraphs" for x in v))

    def test_body_scene_no_location_warns(self):
        # Middle paragraph without location should be a warning, not an error.
        body = (
            "示例公园入口处有一座古朴的石门。\n\n"
            "今天很安静。\n\n"
            "示例塔很美。\n\n"
            "山脚亭子很美。\n\n"
            "原来示例城市这么安静。"
        )
        v = check_body(body)
        warns = [x for x in v if x["severity"] == "warn"]
        self.assertTrue(any(x["rule"] == "body.scene_location" for x in warns))


class TestTopicRule(unittest.TestCase):
    def test_valid_topics_pass(self):
        v = check_topics(VALID_TOPICS)
        self.assertEqual(v, [])

    def test_too_few_topics(self):
        v = check_topics(["#示例公园"])
        self.assertTrue(any(x["rule"] == "topics.count" for x in v))

    def test_too_many_topics(self):
        v = check_topics([f"#t{i}" for i in range(7)])
        self.assertTrue(any(x["rule"] == "topics.count" for x in v))

    def test_missing_hash_prefix(self):
        v = check_topics(["示例公园", "#示例城市"])
        self.assertTrue(any(x["rule"] == "topics.prefix" for x in v))

    def test_generic_topic_warns(self):
        v = check_topics(["#示例公园", "#日常", "#示例城市"])
        self.assertTrue(any(x["rule"] == "topics.generic" for x in v))


class TestImageRule(unittest.TestCase):
    def test_no_images_is_violation(self):
        v = check_images([])
        self.assertTrue(any(x["rule"] == "images.count" for x in v))

    def test_too_many_images(self):
        # Synthetic paths; check_images inspects existence too, so we
        # skip the existence rule by giving all of them an existing parent.
        # Since rules are evaluated independently, the count rule fires first.
        v = check_images([f"/nonexistent/img_{i}.jpg" for i in range(10)])
        # Expect count error AND missing errors.
        self.assertTrue(any(x["rule"] == "images.count" for x in v))

    def test_missing_image(self):
        v = check_images(["/nonexistent/img.jpg"])
        self.assertTrue(any(x["rule"] == "images.missing" for x in v))

    def test_bad_extension(self):
        # Create a real tmp file with .gif extension.
        import tempfile
        with tempfile.NamedTemporaryFile(suffix=".gif", delete=False) as f:
            tmp = f.name
        try:
            v = check_images([tmp])
            self.assertTrue(any(x["rule"] == "images.extension" for x in v))
        finally:
            Path(tmp).unlink(missing_ok=True)


class TestValidate(unittest.TestCase):
    def test_valid_full_payload(self):
        # No real images; use a stub list and accept the missing error as
        # out-of-scope for this rule group.
        result = validate(VALID_TITLE, VALID_BODY, VALID_TOPICS, [])
        # Topics and body valid; images error is expected.
        rule_set = {x["rule"] for x in result["violations"]}
        self.assertNotIn("title.length", rule_set)
        self.assertNotIn("body.length", rule_set)
        self.assertNotIn("topics.count", rule_set)


if __name__ == "__main__":
    unittest.main()