#!/usr/bin/env python3
"""
errors.py — skill-designer 统一错误码与友好反馈出口（Reliability 维核心证据）

为什么需要这个文件：
    本 skill 有 20 个脚本各自报错，此前每个脚本自成一套文案——有的直接把
    `json.JSONDecodeError` 的**英文原文**透传给用户（"Expecting ',' delimiter:
    line 1 column 34"），有的退出码 2 有的 1，有的在 GBK 控制台直接乱码。
    对用户而言这是"失败反馈不可理解"，对自动化编排而言这是"退出码不可依赖"。

    统一为一个错误码表 + 一个出口函数后，任何脚本失败都输出同样结构的三段式：
        ❌ <错误码> <一句人话>
           下一步：<一个可执行动作>
           详情：<指向 fix-toolbox 的锚点>（原始信息）

设计原则：
- **人话优先**：错误码是给机器编排用的，人只需要看第二行"下一步"
- **原始信息降级为附注**：英文 traceback / 库报错一律放括号末尾，不占主视觉
- **退出码统一为 1**：业务失败一律 1（0 成功 / 2 仅警告 / 3 打包卫生拦截，见 SKILL.md §6）
- **不吞异常**：脚本仍可自行 try/except 做恢复，只在最终放弃时调 fail()

用法：
    from errors import fail, enable_utf8
    enable_utf8()                      # 脚本入口处调一次，防 Windows GBK 控制台乱码
    ...
    return fail("E002", detail=str(e)) # 打印三段式并 return 1
"""

import sys

# 错误码 → (一句人话, 一个可执行动作, fix-toolbox 锚点)
CODES = {
    "E001": (
        "找不到这个文件或目录",
        "确认路径拼写与当前所在目录，或改用绝对路径重试",
        "references/fix-toolbox.md#e001",
    ),
    "E002": (
        "JSON 内容有语法错误",
        "把文件贴到任意 JSON 校验器，补上缺失的逗号、引号或括号",
        "references/fix-toolbox.md#e002",
    ),
    "E003": (
        "缺少运行依赖（通常是 Python 未装或版本过低）",
        "按提示安装一行即可（平台通常自带 Python，零配置）",
        "references/fix-toolbox.md#e003",
    ),
    "E004": (
        "目标目录已存在且非空，拒绝覆盖",
        "换一个新目录名，或进入已有目录续填（不删已有内容）",
        "references/fix-toolbox.md#e004",
    ),
    "E005": (
        "缺少必填内容，无法继续",
        "按提示补齐标记项后重跑（可回「按建议」批量采纳）",
        "references/fix-toolbox.md#e005",
    ),
    "E006": (
        "写入文件失败（权限不足 / 磁盘满 / 文件被占用）",
        "关闭占用该文件的程序后重试，或换一个有写权限的目录",
        "references/fix-toolbox.md#e006",
    ),
    "E007": (
        "蓝图缺口太多，未达导出门槛",
        "先按报告补齐缺口格再导出；确需带缺口导出请加 --allow-gap",
        "references/fix-toolbox.md#e007",
    ),
    # ── E008–E010：知识库契约层（ADR-001 阶段0 · knowledge.py）───────────────
    # 为什么单列而不用 E001 兜：三者后果不同、动作不同。DP-210 明令「错误归因不得降级」——
    # 「索引过期」的正确动作是重建索引，「编号断裂」的正确动作是补条目，混成一个码就等于没给动作。
    "E008": (
        "知识库索引缺失、损坏或与脚本不同代",
        "跑 `python scripts/knowledge.py index --write` 重建索引后重试",
        "references/fix-toolbox.md#e008",
    ),
    "E009": (
        "知识库索引与权威源不一致（条目被改动 / 新增 / 删除，索引没跟上）",
        "先跑 index --write 重建；若重建后仍不一致，说明权威源被手工改过——用 git diff 核对改动是否合法",
        "references/fix-toolbox.md#e009",
    ),
    "E010": (
        "知识条目 ID 编号空间断裂（缺号或重复）",
        "ID 永久稳定、不得重编号：缺号补齐条目，重复则合并去重，然后重建索引",
        "references/fix-toolbox.md#e010",
    ),
    "E011": (
        "条目库视图不一致（分片条数 / 视图一声明 / 速查表 / 头部计数 四者对不上）",
        "按报告逐格修正落点，再跑 index --write 重建索引复核（阶段1 编译器落地后此错应绝迹）",
        "references/fix-toolbox.md#e011",
    ),
    "E012": (
        "设计观条目引用了不存在的做法条目",
        "修正该 DP「来源」行里的 D 编号，或补上被引用的条目后重建索引",
        "references/fix-toolbox.md#e012",
    ),
    # ── E013：生成物层（ADR-001 阶段1 · compile_library.py）──────────────────
    # 阶段1 起 references/*.md 全部降级为**生成物**，权威源是 library/*.json。
    # 此码单列的理由：动作与 E009 完全不同——E009 是"重建索引"，E013 是"**改 json 再编译**"。
    # 若混用 E009，用户会本能地去重建索引 → md 的手改被"洗白"，权威源唯一化名存实亡。
    "E013": (
        "生成物与权威源不一致（references/*.md 被手工改动，或未随 library/*.json 重新编译）",
        "改内容请改 `library/*.json`，然后跑 `python scripts/compile_library.py --write` 重编译；"
        "若是为了看差异，跑 `--check --report <路径>`",
        "references/fix-toolbox.md#e013",
    ),
    # ── E014：远程增强服务不可用 / 需授权（ADR-001 阶段1 预留 · knowledge_remote.py）──
    # **熔断语义（DP-210）**：远程走不通时**绝不静默降级**，也绝不用模型记忆补内容。
    # 动作必须可执行：要么切本地、要么拿到授权——而不是"稍后重试"这种不可执行的话。
    "E014": (
        "远程增强服务不可用或需要授权（知识条目在付费层 / 未配置服务地址 / 服务故障）",
        "① 免费路径：加 `--backend local` 用本地全量（功能不减弱）；"
        "② 免费兜底：加 `--backend auto` 让它在远程不可用时自动回落本地；"
        "③ 增强路径：配置环境变量（见 library/remote_config.json）或完成支付授权",
        "references/fix-toolbox.md#e014",
    ),
    # ── E015：吸收登记册腐烂（ADR-001 阶段1 · absorb_intake.py / dedup_index.json）──
    # 登记册里 `equivalent` 指向的条目/文件在当前库中已不存在，说明"不收"的判据悬空了。
    # 与 E012（引用悬空）的区别：E012 是**知识条目**引用悬空（影响召回），
    # E015 是**查重登记**引用悬空（影响吸收裁决）——动作不同，故单列。
    "E015": (
        "吸收登记册腐烂（dedup_index.json 的等价物指向已不存在的条目或文件）",
        "① 跑 `python scripts/absorb_intake.py --check-dedup` 看逐条清单；"
        "② 改判：等价物确实没了 ⇒ 把 verdict 改为接受/重估并注明改判轮次；"
        "③ 若只是 ID 变了 ⇒ 更新 equivalent 到新 ID",
        "references/fix-toolbox.md#e015",
    ),
    # ── E016：版本协商未通过（ADR-001 阶段1 措施 2.4 · knowledge_remote.check_flow_version）──
    # 第四处一致性面：条目 ID 契约 / manifest 契约 / 检索签名契约 之外的「版本契约」。
    # 不复用 E014 的理由：动作完全不同——E014 是「切本地或配置地址」，E016 是「升级本体」。
    # 语义风险：旧流程读新库会产出"看起来正常但语义错位"的知识注入，故**熔断而非降级**。
    "E016": (
        "版本协商未通过（本地流程版本低于远程知识库声明的最低流程版本）",
        "① 升级 skill-designer 本体（推荐，本地库与远程库需同代）；"
        "② 应急：加 `--backend local` 走本地全量（功能完整，不影响使用）；"
        "③ 加 `--backend auto` 可自动回落本地并打印告警",
        "references/fix-toolbox.md#e016",
    ),
}

EXIT_OK = 0
EXIT_FAIL = 1          # 业务失败（统一）
EXIT_WARN = 2          # 仅警告（check_blueprint 缺口 / validate 仅 WARN），非本文件使用
EXIT_HYGIENE = 3       # 打包卫生拦截（sd_cli package 专用），非本文件使用


def enable_utf8():
    """把 stdout / stderr 重配为 UTF-8，防 Windows GBK 控制台中文乱码。

    为什么两个流都要配：只配 stdout 时，警告与错误信息（大多走 stderr）仍然乱码，
    而那恰恰是失败时用户唯一能看到的内容。
    """
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError, OSError):
            pass  # 非标准流（如已被重定向为管道且不支持重配）时静默跳过


def fail(code: str, detail: str = "", script: str = "") -> int:
    """打印三段式友好错误并返回统一退出码 1。

    Args:
        code:   错误码，如 "E002"；未登记的错误码降级为 E000 且不报错
        detail: 原始错误信息（英文 traceback / 库报错），降级为括号附注
        script: 调用方脚本名，用于前缀定位（可选）
    Returns:
        恒为 1，便于 `return fail(...)` 直接收尾
    """
    enable_utf8()
    human, action, anchor = CODES.get(
        code, ("出现未分类错误", "按下方原始信息排查，或重跑一次", "references/fix-toolbox.md")
    )
    prefix = f"[{script}] " if script else ""
    print(f"❌ {prefix}{code} {human}", file=sys.stderr)
    print(f"   下一步：{action}", file=sys.stderr)
    tail = f"（原始信息：{detail}）" if detail else ""
    print(f"   详情：{anchor}{tail}", file=sys.stderr)
    return EXIT_FAIL


def warn(message: str, script: str = "") -> None:
    """非致命警告：只提示不中断，退出码仍由调用方决定。"""
    enable_utf8()
    prefix = f"[{script}] " if script else ""
    print(f"⚠️  {prefix}{message}", file=sys.stderr)


if __name__ == "__main__":
    # 自检：列出全部错误码，供文档与 evals 对照
    enable_utf8()
    print(f"已登记 {len(CODES)} 个错误码：")
    for code, (human, action, anchor) in CODES.items():
        print(f"  {code}  {human}")
        print(f"        下一步：{action}")
        print(f"        详情：{anchor}")
