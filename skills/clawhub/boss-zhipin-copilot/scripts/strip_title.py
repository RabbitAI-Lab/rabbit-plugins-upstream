#!/usr/bin/env python3
"""strip_title.py - 若 --msg 文件首行为「公司名 招聘方名」标题行则剥离，只留正文。

process_job.sh --send 会把 --msg 文件内容原样键入 BOSS 聊天框。
若调用方误把对端标识（公司 招聘方）写进文件首行，会被一起发出。
本脚本检测并剥离此类标题行，仅保留正文；无匹配则原样返回。
"""
import sys, re

t = sys.stdin.read()
lines = t.split('\n')
first = lines[0].strip() if lines else ''

# 「公司名 招聘方名」或带称谓：CJK 2-8 + 空白 + 招聘方名(CJK|·) 2-4 + 可选称谓。
# 注意：招聘方名收紧为 2-4 字（真实中文名上限），避免误剥「王芳 感谢您的回复」这类
# 首行=姓名+长句的正常消息（第二截 6 字会被 {2,4} 拒绝）。2026-07-24 事故根因的「公司 招聘方」
# 标题行（如「可零科技 李洋」）仍会被剥离——公司名 2-8、名 2-4 均满足。
PAT = re.compile(r'^[\u4e00-\u9fa5]{2,8}\s+[\u4e00-\u9fa5·]{2,4}(女士|先生|老师|哥|姐)?$')

if PAT.match(first) and len(lines) > 1:
    sys.stdout.write('\n'.join(lines[1:]))
else:
    sys.stdout.write(t)
