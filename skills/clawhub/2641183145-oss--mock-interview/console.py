"""Windows 控制台默认 GBK,打印中文和 ✓ 会抛 UnicodeEncodeError。

每个入口脚本开头 import 一下就好。Python 3.15 起 UTF-8 是默认值,
到时这个模块可以删掉。
"""

import sys


def setup():
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass  # 被重定向成非 TextIO 时忽略


setup()
