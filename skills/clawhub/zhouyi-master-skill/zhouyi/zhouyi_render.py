#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""zhouyi_render — render.html 落盘 Mixin（save_render / extract_html）。"""

from __future__ import annotations

import os
import re
import time
from typing import Dict, List, Optional

from zhouyi_core import ZhouyiApiError


class RenderMixin:
    """把响应中的 render.html 落盘（文件名规范 {功能名}_{关键参数}_{yyyyMMdd}.html）。"""

    @staticmethod
    def _sanitize(value: str, max_len: int = 40) -> str:
        value = re.sub(r'[\\/:*?"<>|\s]+', "_", str(value)).strip("_")
        return value[:max_len] or "default"

    def save_render(self, result: Dict, output_dir: str = ".",
                    func_name: str = "result", key_params: Optional[List[str]] = None) -> str:
        """把响应中的 render.html 落盘，文件名规范 {功能名}_{关键参数}_{yyyyMMdd}.html。

        :param result: 接口返回的完整响应字典
        :param output_dir: 输出目录（不存在则创建）
        :param func_name: 功能名（如 bazi/lingqian）
        :param key_params: 关键参数列表，拼入文件名
        :return: 写入的文件路径；无 render.html 时抛出 ZhouyiApiError
        """
        render = (result or {}).get("render") or {}
        html = render.get("html") if isinstance(render, dict) else None
        if not html:
            raise ZhouyiApiError(-1, "响应中无 render.html，无法保存")
        os.makedirs(output_dir, exist_ok=True)
        parts = [self._sanitize(func_name)]
        for kp in (key_params or []):
            if kp is not None and str(kp) != "":
                parts.append(self._sanitize(str(kp)))
        parts.append(time.strftime("%Y%m%d"))
        path = os.path.join(output_dir, "_".join(parts) + ".html")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(html)
        return path

    @staticmethod
    def extract_html(result: Dict) -> Optional[str]:
        """便捷方法：从响应中取 render.html（不存在返回 None）。"""
        render = (result or {}).get("render") or {}
        return render.get("html") if isinstance(render, dict) else None
