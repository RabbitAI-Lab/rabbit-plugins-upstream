"""Canaries for DoubaoTTS.preprocess_text / split_long_text.

preprocess_text 的输出是（P1 之后）分段缓存 key 的哈希对象，也是实际计费文本——
这里的行为一旦变化，缓存全体失效且计费口径漂移，必须由测试显式暴露。
"""

import pytest
from script_synthesis import DoubaoTTS

pre = DoubaoTTS.preprocess_text
split = DoubaoTTS.split_long_text


class TestPreprocess:
    def test_markdown_marks_stripped(self):
        assert pre("**加粗** 与 *斜体* 与 `代码`") == "加粗 与 斜体 与 代码"

    def test_link_keeps_anchor_text(self):
        assert pre("见 [规范文档](https://example.com/spec)。") == "见 规范文档。"

    def test_chinese_punctuation_preserved(self):
        # 韵律不变量：全角标点绝不能被"规范化"
        s = "第一句。第二句，停顿、顿号！问吗？"
        assert pre(s) == s

    def test_cjk_latin_spacing_added(self):
        assert pre("我们聊聊AI的事") == "我们聊聊 AI 的事"
        assert pre("版本2发布了") == "版本 2 发布了"

    def test_emoji_removed(self):
        assert pre("好消息🎉来了") == "好消息来了"

    def test_whitespace_collapsed(self):
        assert pre("多  个\t空白\n换行") == "多 个 空白 换行"

    def test_hash_inside_sentence_preserved(self):
        # BUG-4 修复：只删行首标题标记，正文里的 # 保留
        assert pre("我们聊聊C#语言") == "我们聊聊 C#语言"


class TestSplitLongText:
    def test_short_text_single_chunk(self):
        assert split("短句。", max_len=200) == ["短句。"]

    def test_chunks_respect_max_len(self):
        text = "这是一个句子。" * 60  # 420 chars
        chunks = split(text, max_len=200)
        assert all(len(c) <= 200 for c in chunks)
        assert len(chunks) >= 3

    def test_no_content_loss_on_sentence_split(self):
        text = "这是一个句子。" * 60
        assert "".join(split(text, max_len=200)) == text

    def test_no_content_loss_on_comma_split(self):
        text = ("超长从句" * 30 + "，") * 4  # sentences longer than max, comma-splittable
        assert "".join(split(text, max_len=200)) == text

    def test_unpunctuated_hard_split_lossless(self):
        text = "字" * 450
        chunks = split(text, max_len=200)
        assert all(len(c) <= 200 for c in chunks)
        assert "".join(chunks) == text
