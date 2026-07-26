"""
Smart Memory v3 — 中文分词器

基于 jieba 分词，jieba 不可用时降级为字符级分词。
支持中英混合文本，输出词列表。
"""

import re

# 常见中文停用词
_STOP_WORDS = set(
    "的 了 在 是 我 有 和 就 不 人 都 一 一个 上 也 很 到 说 要 去 你 "
    "会 着 没有 看 好 自己 这 他 她 它 们 那 些 什么 怎么 如何 哪 吗 "
    "啊 吧 呢 哦 嗯 可以 需要 应该 能够 可能 已经 因为 所以 但是 如果 "
    "虽然 而且 或者 以及 不仅 还是 只是 不过 然后 之后 之前 之后 之前 "
    "现在 刚才 刚刚 马上 立即 一直 永远 总是 经常 偶尔 从来 忽然 突然 "
    "其实 当然 确实 真的 非常 比较 特别 更加 最 更 很 太 极 挺 有点 "
    "一些 许多 很多 几个 各种 所有 全部 整个 每个 任何 其他 另外 别的 "
    "对 把 被 让 给 用 以 从 到 由 为 与 跟 同 向 朝 往 在 当 于 按 "
    "这个 那个 哪个 这里 那里 哪里 这样 那样 怎样 这么 那么 怎么".split()
)

# 尝试加载 jieba
_jieba = None
try:
    import jieba
    _jieba = jieba
except ImportError:
    pass


def tokenize(text: str) -> list[str]:
    """中英混合分词，返回 token 列表。

    - 优先使用 jieba 分词
    - jieba 不可用时降级为字符级分词（2 字以上中文片段 + 英文/数字片段）
    - 自动过滤停用词和单字
    - 英文/数字统一小写
    """
    if _jieba is not None:
        # jieba 分词模式
        words = _jieba.cut(text)
        tokens = []
        for w in words:
            w = w.strip()
            if not w:
                continue
            # 英文/数字小写
            if re.match(r"^[a-zA-Z0-9_]+$", w):
                w = w.lower()
            if len(w) >= 2 and w not in _STOP_WORDS:
                tokens.append(w)
        return tokens

    # 降级：简易分词（v2 逻辑）
    tokens = []
    # 中文连续片段（2 字以上）
    cjk = re.findall(r"[\u4e00-\u9fff]{2,}", text)
    tokens.extend(cjk)
    # 英文/数字连续片段
    eng = re.findall(r"[a-zA-Z0-9_]{2,}", text)
    tokens.extend([t.lower() for t in eng])
    # 过滤停用词和单字
    tokens = [t for t in tokens if t not in _STOP_WORDS and len(t) >= 2]
    return tokens


def tokenize_set(text: str) -> set[str]:
    """分词后返回集合（用于 decide 快速匹配）。"""
    return set(tokenize(text))


def build_vocab(texts: list[str]) -> dict[str, int]:
    """从文本列表构建词汇表（词 → 出现次数）。

    Args:
        texts: 文本列表

    Returns:
        {词: 频次} 字典，按频次降序排列
    """
    vocab: dict[str, int] = {}
    for text in texts:
        for token in tokenize(text):
            vocab[token] = vocab.get(token, 0) + 1
    return dict(sorted(vocab.items(), key=lambda x: x[1], reverse=True))
