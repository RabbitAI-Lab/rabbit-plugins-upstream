#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zhouyi_client.py — 周易大师开放平台 Python 客户端（薄入口）

本文件为模块化拆分后的对外入口，实现位于同目录 `zhouyi/` 包：
  - zhouyi/zhouyi_core.py          常量 / ZhouyiApiError / HTTP 传输层
  - zhouyi/zhouyi_api.py           49 项开放 API 功能方法
  - zhouyi/zhouyi_render.py        render.html 落盘
  - zhouyi/zhouyi_cli_args.py      CLI 参数解析
  - zhouyi/zhouyi_cli_dispatch.py  CLI 命令分发与 main

开放 API 约定（与 jcjasp-backend /api/open/** 保持一致）：
  - 鉴权头：X-API-Key（官网注册获取）；来源标识头：X-Open-Source（默认 skill）
  - 统一响应：{"code":0,"message":"ok","data":{...},"render":{"html":"..."},"meta":{...}}
  - 错误码：40001 参数错误 / 40101 KEY 无效 / 40301 额度过期 /
            42901 每日额度用尽 / 50301 算力接口不可用

作为库使用（用法与拆分前完全一致）：
    from zhouyi_client import ZhouyiClient
    client = ZhouyiClient(api_key="your-key")  # 默认调用 https://api.iching.jiuchongju.com
    # 本地开发可用环境变量 ZHOUYI_BASE_URL 覆盖，如 export ZHOUYI_BASE_URL=http://localhost:8090
    result = client.bazi(name="张三", gender="男", birthDate="1990-01-15", birthTime="10:30")
    print(result["data"])
    client.save_render(result, func_name="bazi", key_params=["张三"], output_dir="./html")

作为 CLI 使用（用法与拆分前完全一致）：
    export ZHOUYI_API_KEY=your-key
    python3 zhouyi_client.py bazi --name 张三 --gender 男 --birth-date 1990-01-15 --birth-time 10:30 --save-html ./html
    python3 zhouyi_client.py quota

依赖：Python 3（requests 可选，未安装时自动回退标准库 urllib）。
"""

from __future__ import annotations

import os
import sys

# 直接以脚本方式执行时脚本目录已在 sys.path；作为包被导入时（如 mcp-server 从
# 其他工作目录引入），需保证本目录在 sys.path 中才能找到 zhouyi 包。
# 兼容两种包布局：扁平（zhouyi/ 与 scripts/ 平级，位于包根）与包裹（zhouyi/ 位于 scripts/ 内）——
# 因此同时把本目录与其父目录（包根）加入 sys.path，导出包无需调用方手改。
_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(_HERE)
for _p in (_HERE, _ROOT):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from zhouyi import (  # noqa: E402
    API_KEY_ENV,
    DEFAULT_BASE_URL,
    DEFAULT_OPEN_SOURCE,
    ERROR_MESSAGES,
    OpenApiMixin,
    RenderMixin,
    ZhouyiApiError,
    ZhouyiClient,
    ZhouyiClientBase,
    __version__,
)
from zhouyi.zhouyi_cli_args import _add_common_args, _emit, _print_result, build_parser  # noqa: E402
from zhouyi.zhouyi_cli_dispatch import _dispatch, main  # noqa: E402

__all__ = [
    "__version__",
    "DEFAULT_BASE_URL",
    "API_KEY_ENV",
    "DEFAULT_OPEN_SOURCE",
    "ERROR_MESSAGES",
    "ZhouyiApiError",
    "ZhouyiClient",
    "ZhouyiClientBase",
    "OpenApiMixin",
    "RenderMixin",
    "build_parser",
    "main",
]


if __name__ == "__main__":
    sys.exit(main())
