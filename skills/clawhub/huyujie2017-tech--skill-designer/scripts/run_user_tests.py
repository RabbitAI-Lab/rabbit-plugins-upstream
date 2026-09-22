"""
run_user_tests.py — skill-designer 真实用户场景回归测试

自动执行 user_test_cases.json 中定义的用例，覆盖从零创建、我拟路径、
蓝图检查、交接产物导出、可视化 SVG、B09 摘要图等核心流程。

用法：
    python scripts/run_user_tests.py [--cases init-create,draft-imagine] [--json]
"""

import json
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

from retry import read_text_robust, write_text_robust

ROOT = Path(__file__).resolve().parent.parent
PYTHON = sys.executable
SD_CLI = ROOT / "scripts" / "sd_cli.py"
CASES_FILE = ROOT / "scripts" / "user_test_cases.json"


def run_cmd(args: list[str]) -> tuple[int, str, str]:
    env = __import__("os").environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"  # 强制整条调用链 UTF-8，避免 Windows 管道按 GBK 输出导致解码崩溃
    proc = subprocess.run(
        [PYTHON, str(SD_CLI), *args],
        cwd=str(ROOT),
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        errors="replace",  # 兜底：个别非法字节以替换符承载，不中断整个套件
        check=False,
    )
    return proc.returncode, proc.stdout, proc.stderr


# ── C7 边界密度门槛的夹具侧配套（v3.17.0）─────────────────────────────
# 背景：check_blueprint 自 v3.15.0 起增加 C7——「十格填齐 ≠ 可交接」，还要求
# 全蓝图边界条目 ≥ BOUNDARY_MIN 且至少 1 条「易混淆正例」。它对应 ③深化设计里
# 的【固定步骤·边界补全】，是真实用户走完流程后**本就该有**的产物。
#
# 于是夹具不能停在「把所有 ______ 换成占位文本」——那模拟的是一个跳过了边界
# 补全的用户：check 返回 2（仅警告），而 export 要求 ok 且退出码 0，警告变成
# 隐性硬拦，check / check --write-iqs / export 三个用例连带失败（实测 22/3）。
#
# 为什么修夹具而不是把期望值放宽到 2：期望值放宽等于把「填满即可交接」写进
# 回归，而那正是 C7 要拦的病（不变量 I4：门禁只增不减）。
#
# 为什么「问检查器」而不是在这里自己数：口径只能有一处权威源（DP-209）。
# 若把关键词表与门槛抄一份进测试，检查器改口径时夹具会静默失配——那正是本项目
# 反复踩的「同一件事两处各写一遍」老病（DP-204 的教训）。
_B01_NONGOAL = re.compile(r"^(\s*[-*]\s*\*\*非目标清单\*\*[：:])\s*.*$", re.M)
_B05_BOUNDARY = re.compile(r"^(\s*[-*]\s*边界\s*B[：:])\s*.*$", re.M)

# 条目数量刻意对齐实证口径（outputs/baseline-vs-with-skill.md：深度人工 18 条），
# 且逐条命中 BOUNDARY_KEYWORDS / CONFUSABLE_RE，不靠模板自身的样板文案凑数。
# 目标 17 条实打实的边界 + 1 条易混淆正例，留出模板漂移余量。
_B01_NONGOAL_ITEMS = (
    "明确不做以下事项（防功能膨胀；④施工蓝图出口条件之一）\n"
    "  - 不做与设计流程无关的通用文档排版\n"
    "  - 不该替代目标 skill 自身的业务判断与运行逻辑\n"
    "  - 排除非 skill 形态的产物（PPT / 视频 / 3D 模型）\n"
    "  - 不接管目标 skill 的发布上线与平台审核流程\n"
    "  - 不负责目标 skill 上线后的运维监控与告警\n"
    "  - 不处理运行时依赖的安装与环境排障\n"
    "  - 不适用多语言场景（当前仅中文）\n"
    "  - 易混淆正例：看似「通用文档排版」其实该本 skill 管——"
    "目标 skill 的 SKILL.md 章节骨架就是本 skill 的产物"
)
_B05_BOUNDARY_ITEMS = (
    "不做什么 / 什么时候必须停下来问\n"
    "  - 不属于本 skill：目标 skill 的具体业务领域知识（如行情、医学诊断）\n"
    "  - 不属于本 skill：目标 skill 运行时的外部服务与数据对接\n"
    "  - 排除：把设计流程当成目标 skill 的运行时依赖\n"
    "  - 拒绝：准入四问未过时继续填充后续格（先定结论再继续）\n"
    "  - 不接管：目标 skill 的版本发布与 SkillHub 上架流程\n"
    "  - 不负责：目标 skill 上线后的用户支持与故障处置\n"
    "  - 不处理：与 skill 设计无关的通用文本改写请求\n"
    "  - 停用条件：目标 skill 与生态内既有 skill 正交性存疑时（先做正交性核验）"
)


def _fill_boundary_completion(bp_dir: Path) -> None:
    """补上 ③固定步骤·边界补全的产物（C7 夹具侧）。

    落位锚在**字段名**（B01 非目标清单 / B05 边界 B）而非目录结构——字段名是
    模板契约的一部分，比行号、比段落位置都稳。两处锚点各须恰好命中 1 次，命中 0
    次立即抛错：批量改写报「0 份更新」而静默跳过，是本项目最危险的一类失败。
    """
    for fname, pattern, items, label in (
        ("01-条件.md", _B01_NONGOAL, _B01_NONGOAL_ITEMS, "B01 非目标清单"),
        ("05-分析.md", _B05_BOUNDARY, _B05_BOUNDARY_ITEMS, "B05 边界 B"),
    ):
        p = bp_dir / fname
        text = read_text_robust(p) or ""
        new_text, n = pattern.subn(lambda m, it=items: m.group(1) + it, text)
        if n != 1:
            raise RuntimeError(
                f"边界补全落空：{label} 在 {fname} 命中 {n} 次（期望 1 次）。"
                f"模板字段名可能已改；请同步 _fill_boundary_completion 的锚点正则，"
                f"不要让它静默跳过（跳过 → C7 触发 → check/export 连带失败）。"
            )
        write_text_robust(p, new_text)


def _assert_boundary_density(bp_dir: Path) -> None:
    """用**检查器自己的口径**复核夹具产物，不足即抛错。

    刻意不在这里重写一遍关键词表：门槛与口径的权威源是 check_blueprint（DP-209）。
    测试若自带一份副本，检查器改口径时夹具会「自己觉得自己合格」——静默失配。
    """
    from check_blueprint import (BLOCKS, BOUNDARY_CONFUSABLE_MIN, BOUNDARY_MIN,
                                 boundary_stats)

    items = conf = 0
    for fname in BLOCKS.values():
        p = bp_dir / fname
        if not p.exists():
            continue
        i, c = boundary_stats(read_text_robust(p) or "")
        items += i
        conf += c
    if items < BOUNDARY_MIN or conf < BOUNDARY_CONFUSABLE_MIN:
        raise RuntimeError(
            f"夹具边界密度不足：边界 {items} 条（门槛 {BOUNDARY_MIN}）、"
            f"易混淆正例 {conf} 条（门槛 {BOUNDARY_CONFUSABLE_MIN}）——"
            f"check 会返回 2（仅警告）并连带堵死 export。"
        )


def fill_blueprint(bp_dir: Path, with_trace: bool = False, skip_boundary: bool = False) -> None:
    """把刚生成的蓝图骨架填充成可通过 check_blueprint.py 的版本。

    含三件事：①把所有填空换成占位文本；②关键字段写死样例值（B01 结论 / B09 分数）；
    ③边界补全（_fill_boundary_completion）——缺第③件则 C7 触发，check 返回 2。

    `skip_boundary=True` 专门给 F1 的反向用例用：十格**全部填满**（IQS 100、errors 0），
    但故意不做边界补全 → 只剩 C7 这一条 warnings → check 退出码 2。
    这正是「仅警告拦人」的形态，用来验证 export 的拒绝消息**回显真实原因**而非鼓励语。
    """
    for md in sorted(bp_dir.glob("*.md")):
        text = read_text_robust(md) or ""
        # 替换所有填空占位符为示例文本（保留小节标题）
        lines = []
        for line in text.splitlines():
            if line.lstrip().startswith("#"):
                lines.append(line)
            else:
                lines.append(line.replace("______", "已填示例"))
        text = "\n".join(lines)
        text = text.replace("☐", "☑")
        write_text_robust(md, text)

    # B01 结论收敛为单一选项「创建」，模拟真实用户已做决定。
    # 注意：这里不要写死模板文案——B01 结论从「做 / 不做 / 转向」演进为
    # 「创建 / 继续蒸馏 / 合并 / 不做 / 转向」后，写死的正则会静默失效，
    # 结论行保持模板原样，C3 就会误判成「结论=不做」。整行替换才不会随模板漂移。
    b01 = bp_dir / "01-条件.md"
    if b01.exists():
        text = read_text_robust(b01) or ""
        text = re.sub(r"^(\s*[-*]\s*结论[:：]).*$", r"\g<1>**创建**（材料齐全，准入四问通过）",
                      text, flags=re.M)
        write_text_robust(b01, text)

    # B09 填具体分数
    b09 = bp_dir / "09-结果.md"
    if b09.exists():
        text = read_text_robust(b09) or ""
        # 注意：[^\n] 不可省略。若用 [^:：]，字符类会跨行匹配，
        # 导致从「内部质量分」一路吃到 9.2 节，把中间的字段行整段吞掉。
        # 只替换值、保留原字段名（\g<1>）——更贴近真实用户「只填值不改键名」的行为，
        # 也让 --write-iqs 的回填断言有效。
        text = re.sub(r"(内部质量分[^:：\n]*[:：])\s*已填示例", r"\g<1>85", text)
        # BR-5 设计期五维：整行替换（含占位符后缀），EVS = 均分 × 20
        text = re.sub(
            r"BR-5 均分[^:：\n]*[:：]\s*已填示例.*",
            "BR-5 均分：4.5（T=5 / R=4 / A=4.5 / C=4.5 / E=4.5）",
            text,
        )
        text = re.sub(r"(外部价值分[^:：\n]*[:：])\s*已填示例", r"\g<1>90", text)
        text = re.sub(r"(综合评分[^:：\n]*[:：])\s*已填示例", r"\g<1>76.5", text)
        text = re.sub(r"(指向的改进项[^:：\n]*[:：])\s*已填示例",
                      r"\g<1>补充边界测试用例；优化输出格式", text)
        if with_trace:
            text = text.replace(
                "机器验证：☑ 已跑 scripts/check_blueprint.py（蓝图完整性）☑ 已跑 scripts/validate_skill.py（目标 skill 已有目录时）",
                "机器验证：☑ 已跑 scripts/check_blueprint.py（蓝图完整性）☑ 已跑 scripts/validate_skill.py（目标 skill 已有目录时）\n- 平台名称（如 SkillHub TRACE / 内部评审）：SkillHub TRACE\n- 外部评分：T=4.8 / R=4.3 / A=4.5 / C=4.4 / E=4.6（五维均 1–5 分）\n- 最低分项及文字评语：R=4.3 缺少自动重试\n- 按维度拆分的补丁清单（P0 必修 / P1 建议 / P2 可选）：P0 增加自动重试；P1 FAQ 加锚点\n- 补丁生成命令：☑ 已跑 `python scripts/trace_patch.py feedback.json`\n- 补丁验证命令：☑ 已跑 `python scripts/validate_skill.py --self`",
            )
        write_text_robust(b09, text)

    # 同步 index 快照与 checkpoint
    index = bp_dir / "index.md"
    if index.exists():
        text = read_text_robust(index) or ""
        text = text.replace("| 当前格 | Phase 0 |", "| 当前格 | 施工蓝图 |")
        text = text.replace("| 已完成 | （无） |", "| 已完成 | B01,B02,B03,B04,B05,B06,B07,B08,B09,B10 |")
        text = text.replace("| 本格产物 | 蓝图骨架已生成，待逐格填充 |", "| 本格产物 | 全部 10 格已填完，机器检查通过 |")
        text = text.replace("| 待确认 | 平台 / 入口 / 通道 |", "| 待确认 | 无 |")
        text = text.replace("| 下一步 | B01 条件积木 |", "| 下一步 | 跑 export_brief.py 生成交接产物 |")
        write_text_robust(index, text)

    # 边界补全（C7）：必须放在填完全部字段之后——C7 只在无结构性缺口时才报，
    # 顺序反了会先撞 C7 再补，两类信号互相淹没。补完立即用检查器口径自证。
    if skip_boundary:
        return
    _fill_boundary_completion(bp_dir)
    _assert_boundary_density(bp_dir)


def fill_remaining_blanks(bp_dir: Path, skip_files: tuple[str, ...] = ()) -> None:
    """补填 deepen 收口后仍留空的 `______` 与未勾 ☐，模拟用户把「能填的」都填完。

    为什么必须补这一步：模板演进后（B01 资源约束三件套 / 非目标清单 / 证据来源，
    B04 GATE，B07 archetype），`deepen --accept-all` 只采纳【AI 建议】条目，
    纯 `______` 空位本就留给用户在③深化设计时手填。夹具若停在 deepen 之后就导出，
    IQS 只有 81，永远够不到 --allow-gap 的默认阈值 90——这是夹具漂移，不是产品缺陷。

    为什么默认跳过 08-行动.md：B08 的「真实场景跑过」必须等 skill 真正落地后才有，
    它是 --allow-gap 要放行的那类**合法**缺口。连它一起填满就变成 IQS 100 无缺口导出，
    「遗留缺口」章节根本不会生成，反向断言反而失去意义。
    """
    for md in sorted(bp_dir.glob("*.md")):
        if md.name in skip_files:
            continue
        text = read_text_robust(md) or ""
        out = []
        for line in text.splitlines():
            if line.lstrip().startswith("#"):
                out.append(line)
            else:
                out.append(line.replace("______", "已填示例"))
        write_text_robust(md, "\n".join(out).replace("☐", "☑"))


def run_setup(name: str, workdir: Path) -> None:
    if name == "fill-check-blueprint":
        bp = workdir / "check-test"
        if bp.exists():
            shutil.rmtree(bp)
        rc, _, _ = run_cmd(["init", str(bp), "--name", "check-test", "--channel", "light", "--entry", "create"])
        if rc != 0:
            raise RuntimeError("init check-test 失败")
        fill_blueprint(bp)
    elif name == "fill-export-blueprint":
        bp = workdir / "export-test"
        if bp.exists():
            shutil.rmtree(bp)
        rc, _, _ = run_cmd(["init", str(bp), "--name", "export-test", "--channel", "light", "--entry", "create"])
        if rc != 0:
            raise RuntimeError("init export-test 失败")
        fill_blueprint(bp)
    elif name == "fill-noboundary-blueprint":
        # F1 反向用例专用：十格全填满（IQS 100、errors 0）但**故意跳过 ③边界补全**
        # → 只剩 C7 一条 warnings → check 退出码 2（「仅警告拦人」）。
        # 旧行为下 export 会把 next_action（「全部 10 格已完成——…进入交接落地」）当原因打印，
        # 用户看到的是拒绝语 + 鼓励语并存；本夹具就是钉住这个形态。
        bp = workdir / "noboundary-test"
        if bp.exists():
            shutil.rmtree(bp)
        rc, _, _ = run_cmd(["init", str(bp), "--name", "noboundary-test",
                            "--channel", "light", "--entry", "create"])
        if rc != 0:
            raise RuntimeError("init noboundary-test 失败")
        fill_blueprint(bp, skip_boundary=True)
    elif name == "fill-b09-blueprint":
        bp = workdir / "b09-test"
        if bp.exists():
            shutil.rmtree(bp)
        rc, _, _ = run_cmd(["init", str(bp), "--name", "b09-test", "--channel", "light", "--entry", "create"])
        if rc != 0:
            raise RuntimeError("init b09-test 失败")
        fill_blueprint(bp, with_trace=True)
    elif name == "init-empty-blueprint":
        # 全新未填蓝图：init 后不做任何填充，用于验证 IQS 判 0
        bp = workdir / "empty-test"
        if bp.exists():
            shutil.rmtree(bp)
        rc, _, _ = run_cmd(["init", str(bp), "--name", "empty-test", "--channel", "light", "--entry", "create"])
        if rc != 0:
            raise RuntimeError("init empty-test 失败")
    elif name == "proto-deepen-blueprint":
        # ③深化设计 / 带缺口导出的前置：用 proto 生成一份②初步方案（含【AI 建议】标记）
        bp = workdir / "deepen-test"
        if bp.exists():
            shutil.rmtree(bp)
        answers = json.dumps({
            "problem": "把读书笔记整理成结构化卡片沉淀到 Obsidian",
            "audience": "爱读书但笔记散乱的人",
            "platform": "workbuddy", "entry": "create",
            "flow": "给一段笔记 → AI 整理成卡片 → 确认 → 存到库",
            "priority": "卡片格式必须统一",
            "example": "给一段《思考，快与慢》的摘抄，输出一张卡片",
        }, ensure_ascii=False)
        rc, _, _ = run_cmd(["proto", str(bp), "--name", "deepen-test", "--answers", answers])
        if rc != 0:
            raise RuntimeError("proto deepen-test 失败")
    elif name == "deepen-ready-blueprint":
        # 带缺口导出的前置：②初步方案 → ③深化设计收口（IQS 提到 90+，只剩 B08 实证项）
        bp = workdir / "deepen-test"
        if bp.exists():
            shutil.rmtree(bp)
        answers = json.dumps({
            "problem": "把读书笔记整理成结构化卡片沉淀到 Obsidian",
            "audience": "爱读书但笔记散乱的人",
            "platform": "workbuddy", "entry": "create",
            "flow": "给一段笔记 → AI 整理成卡片 → 确认 → 存到库",
            "priority": "卡片格式必须统一",
            "example": "给一段《思考，快与慢》的摘抄，输出一张卡片",
        }, ensure_ascii=False)
        rc, _, _ = run_cmd(["proto", str(bp), "--name", "deepen-test", "--answers", answers])
        if rc != 0:
            raise RuntimeError("proto deepen-test 失败")
        rc, _, _ = run_cmd(["deepen", str(bp), "--accept-all",
                            "--set", "B02.正交性=与 card-generator 是上下游：它按既定模板渲染，本 skill 负责素材整理",
                            "--tick", "B01,B02,B03,B04,B05,B06,B07,B09,B10"])
        if rc != 0:
            raise RuntimeError("deepen deepen-test 失败")
        # 补填能填的空位，只留 B08 实证缺口 → IQS 98 ≥ 阈值 90
        fill_remaining_blanks(bp, skip_files=("08-行动.md",))
    elif name == "suite-workbench-ready":
        # suite 型蓝图（多子域工作台）：②初步方案 → ③深化设计收口，供 export 反向断言用
        bp = workdir / "suite-test"
        if bp.exists():
            shutil.rmtree(bp)
        answers = json.dumps({
            "problem": "个人投资者需要一个统一工作台，一站式完成信息收集、信息整理、投资组合监控、组合调整，界面要简洁直观",
            "audience": "个人投资者（非机构散户），每日打开工作台查看持仓、收集资讯、整理成卡片、必要时调整仓位",
            "platform": "workbuddy", "entry": "create",
            "flow": "分几个模块独立完成，每模块内部步骤清晰，调整仓位前需要先看当前持仓确认",
            "priority": "界面简洁、操作直观、数据准确",
            "example": "投资者早上打开工作台：先看昨日组合涨跌汇总，再收集资讯整理成关注卡片",
            "boundary": "不提供投资建议，不代客下单，不做高频量化交易信号，只做信息聚合与持仓记录",
        }, ensure_ascii=False)
        rc, _, _ = run_cmd(["proto", str(bp), "--name", "suite-test", "--answers", answers])
        if rc != 0:
            raise RuntimeError("proto suite-test 失败")
        rc, _, _ = run_cmd(["deepen", str(bp), "--accept-all",
                            "--tick", "B01,B02,B03,B04,B05,B06,B07,B09,B10"])
        if rc != 0:
            raise RuntimeError("deepen suite-test 失败")
        # 同上：补填能填的空位，只留 B08 实证缺口，使 --allow-gap 能放行
        fill_remaining_blanks(bp, skip_files=("08-行动.md",))
    elif name == "fill-br5-only-blueprint":
        # 十格填满，但 09-结果.md 只留 BR-5 五维——IQS / EVS / 综合 全部留空，
        # 用于验证「只评 BR-5，其余分数机器自动算」
        bp = workdir / "br5-test"
        if bp.exists():
            shutil.rmtree(bp)
        rc, _, _ = run_cmd(["init", str(bp), "--name", "br5-test", "--channel", "light", "--entry", "create"])
        if rc != 0:
            raise RuntimeError("init br5-test 失败")
        fill_blueprint(bp)
        b09 = bp / "09-结果.md"
        text = read_text_robust(b09) or ""
        for key in ("内部质量分", "外部价值分", "综合评分"):
            text = re.sub(rf"({key}[^:：\n]*[:：])\s*\d+(?:\.\d+)?", r"\g<1>（留空，测机器算）", text)
        write_text_robust(b09, text)


def check_files(files: list[str]) -> list[str]:
    missing = []
    for f in files:
        if not Path(f).exists():
            missing.append(f)
    return missing


def check_content_contains(items: dict[str, list[str]]) -> list[str]:
    errors = []
    for fpath, needles in items.items():
        p = Path(fpath)
        if not p.exists():
            errors.append(f"{fpath} 不存在，无法检查内容")
            continue
        text = read_text_robust(p) or ""
        for needle in needles:
            if needle not in text:
                errors.append(f"{fpath} 缺少内容：{needle}")
    return errors


def check_content_not_contains(items: dict[str, list[str]]) -> list[str]:
    """反向断言：产物里**不该**出现的内容。

    专治「清理标记时把行首项目符号叠成 `- - `」这类格式回归——
    这类 bug 不影响功能，肉眼也容易漏，必须靠机器守住。
    """
    errors = []
    for fpath, needles in items.items():
        p = Path(fpath)
        if not p.exists():
            continue  # 文件都不存在，自然不含这些串，不算失败
        text = read_text_robust(p) or ""
        for needle in needles:
            if needle in text:
                errors.append(f"{fpath} 不应包含：{needle!r}（出现 {text.count(needle)} 次）")
    return errors


def substitute_args(args: list[str], workdir: Path) -> list[str]:
    return [a.replace("{workdir}", str(workdir)) for a in args]


def run_case(case: dict, workdir: Path) -> dict:
    start = time.time()
    errors: list[str] = []

    cmd = case["command"]
    raw_args = case.get("args", [])

    # init / draft / proto 需要目标目录为空，先清理
    if cmd in ("init", "draft", "proto") and raw_args:
        target = Path(substitute_args([raw_args[0]], workdir)[0])
        if target.exists():
            shutil.rmtree(target)

    setup = case.get("setup")
    if setup:
        try:
            run_setup(setup, workdir)
        except Exception as e:
            return {"id": case["id"], "name": case["name"], "status": "SETUP_FAIL", "errors": [str(e)], "duration": 0}

    args = substitute_args(raw_args, workdir)
    rc, stdout, stderr = run_cmd([cmd, *args])
    output = stdout + stderr

    expected_rc = case.get("expect_exit_code", 0)
    if rc != expected_rc:
        errors.append(f"命令退出码 {rc}，期望 {expected_rc}\n输出：{output[:300]}")

    checks = case.get("checks", {})
    if "files_exist" in checks:
        missing = check_files(substitute_args(checks["files_exist"], workdir))
        if missing:
            errors.append(f"缺少文件：{', '.join(missing)}")
    if "content_contains" in checks:
        content_items = {
            k.replace("{workdir}", str(workdir)): v
            for k, v in checks["content_contains"].items()
        }
        errors.extend(check_content_contains(content_items))
    if "content_not_contains" in checks:
        nc_items = {
            k.replace("{workdir}", str(workdir)): v
            for k, v in checks["content_not_contains"].items()
        }
        errors.extend(check_content_not_contains(nc_items))
    if "stdout_contains" in checks:
        for needle in checks["stdout_contains"]:
            if needle not in output:
                errors.append(f"命令输出缺少：{needle}")
    # stdout_not_contains（v3.19.0 新增）：反向断言「不该出现的东西」。
    # 需要它是因为 F1 这类缺陷是**多说了话**（拒绝语里混进鼓励语），只断言「含什么」抓不到。
    if "stdout_not_contains" in checks:
        for needle in checks["stdout_not_contains"]:
            if needle in output:
                errors.append(f"命令输出不应出现：{needle}")

    return {
        "id": case["id"],
        "name": case["name"],
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "duration": round(time.time() - start, 2),
    }


def main() -> int:
    import argparse
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    ap = argparse.ArgumentParser(description="skill-designer 真实用户场景回归测试")
    ap.add_argument("--cases", help="逗号分隔的用例 ID，默认全部")
    ap.add_argument("--json", action="store_true", help="结构化输出")
    ap.add_argument("--workdir", help="测试工作目录（默认系统临时目录）")
    args = ap.parse_args()

    cases = json.loads(read_text_robust(CASES_FILE) or "[]")
    if args.cases:
        wanted = set(args.cases.split(","))
        cases = [c for c in cases if c["id"] in wanted]

    workdir = Path(args.workdir) if args.workdir else Path(__import__("tempfile").gettempdir()) / "sd-user-tests"
    workdir.mkdir(parents=True, exist_ok=True)

    results = []
    for case in cases:
        results.append(run_case(case, workdir))

    passed = sum(1 for r in results if r["status"] == "PASS")
    failed = len(results) - passed

    if args.json:
        print(json.dumps({"passed": passed, "failed": failed, "results": results}, ensure_ascii=False, indent=2))
    else:
        print(f"\n{'='*72}")
        print(f"skill-designer 用户场景测试：{passed} 通过 / {failed} 失败（共 {len(results)} 项）")
        print(f"{'='*72}")
        for r in results:
            icon = "✅" if r["status"] == "PASS" else "❌"
            print(f"{icon} {r['name']:<30} ({r['duration']:.2f}s)")
            for err in r["errors"]:
                print(f"   → {err}")
        print(f"\n工作目录：{workdir}")

    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
