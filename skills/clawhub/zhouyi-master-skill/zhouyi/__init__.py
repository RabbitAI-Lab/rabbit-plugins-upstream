#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""周易大师开放平台 Python 客户端（模块化实现包）。

与拆分前的单文件 zhouyi_client.py 完全同源等价：
  - zhouyi_core   : 常量 / ZhouyiApiError / HTTP 传输层（requests 优先，urllib 回退）
  - zhouyi_render : render.html 落盘 Mixin（save_render / extract_html）
  - zhouyi_api    : 49 项开放 API 功能方法 Mixin
  - zhouyi_cli_args / zhouyi_cli_dispatch : CLI 参数解析与命令分发

对外符号（ZhouyiClient / ZhouyiApiError / main 等）由 __init__.py 统一 re-export。
"""

import os
import sys

# 作为独立脚本被直接执行（python3 .../_zhouyi_client/xxx.py）或 zip 解压后运行时，
# 保证同目录兄弟模块可导入（作为包导入时脚本目录不在 sys.path 中）。
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

from zhouyi_core import (  # noqa: E402
    API_KEY_ENV,
    DEFAULT_BASE_URL,
    DEFAULT_OPEN_SOURCE,
    ERROR_MESSAGES,
    ZhouyiApiError,
    ZhouyiClientBase,
    __version__,
)
from zhouyi_render import RenderMixin  # noqa: E402
from zhouyi_api import OpenApiMixin  # noqa: E402


class ZhouyiClient(ZhouyiClientBase, OpenApiMixin, RenderMixin):
    """周易大师开放平台客户端（组合传输层 + 功能方法 + HTML 落盘）。

    :param base_url: 服务地址，默认 https://api.iching.jiuchongju.com（可用环境变量
                     ZHOUYI_BASE_URL 覆盖，本地开发如 http://localhost:8090）
    :param api_key:  官网注册获取的 API-KEY（也可通过环境变量 ZHOUYI_API_KEY 提供）
    :param open_source: X-Open-Source 来源标识，默认 skill（mcp/api 等可配置）
    :param timeout: 请求超时秒数
    """


__all__ = [
    "__version__",
    "DEFAULT_BASE_URL",
    "API_KEY_ENV",
    "DEFAULT_OPEN_SOURCE",
    "ERROR_MESSAGES",
    "ZhouyiApiError",
    "ZhouyiClientBase",
    "OpenApiMixin",
    "RenderMixin",
    "ZhouyiClient",
]
