#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自动故障捕获钩子（供各脚本在启动时挂一行）
=====================================================================
把「未捕获异常」自动变成一份**脱敏**的故障快照，使用人不用手动复述报错。

接入方式（每个脚本的入口处两行即可）：

    try:
        from _feedback_hook import install; install()
    except Exception:
        pass

设计要点
-------------------------------------------------------------------
1. **绝不影响主流程**：整个钩子被 try/except 包住，反馈模块出任何问题
   都静默跳过，原始 traceback 照常打印。反馈功能永远不能把分析搞崩。
2. **默认关闭也安全**：可用环境变量 `INS_FEEDBACK=0` 关闭自动捕获
   （不写文件、不弹任何提示），适合不方便落盘的环境。
3. **只抓未捕获异常**：脚本里那些 `sys.exit(1)` 的**主动硬失败**
   （如「未找到演示表」「总保费为 0」）不在此列 —— 它们带明确提示，
   不是 bug。若使用人认为某次硬失败属于误报，请用 `feedback.py report`
   手动提「数据问题」。
4. **落盘前强制脱敏**：由 feedback.sanitize 处理，路径与 4 位以上数字
   会被抹掉，不会写入姓名 / 身份证 / 保单号 / 金额。
=====================================================================
"""
import os
import sys


def install(skill_version=None):
    """注册 sys.excepthook。重复调用无害。"""
    if os.environ.get("INS_FEEDBACK") == "0":
        return False
    if getattr(sys, "_ins_feedback_installed", False):
        return True

    here = os.path.dirname(os.path.abspath(__file__))
    if here not in sys.path:
        sys.path.insert(0, here)

    def hook(etype, value, tb):
        try:
            import feedback
            path = feedback.record_crash(etype, value, tb, sys.argv)
            if path:
                print("", file=sys.stderr)
                print("─" * 60, file=sys.stderr)
                print(f"已自动生成故障快照（脱敏后）：{path}", file=sys.stderr)
                print("可用 `python scripts/feedback.py export` 打包并发给作者。",
                      file=sys.stderr)
                print("不想收集故障快照？设环境变量 INS_FEEDBACK=0 即可关闭。",
                      file=sys.stderr)
                print("─" * 60, file=sys.stderr)
                print("", file=sys.stderr)
        except Exception:
            pass
        sys.__excepthook__(etype, value, tb)

    sys.excepthook = hook
    sys._ins_feedback_installed = True
    return True
