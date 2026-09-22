#!/usr/bin/env python3
"""
blueprint_proto.py — 四步施工流 Step ②「初步方案」编排器

把 Step ① 概念讨论的结果（answers JSON）经「概念讨论最低标准」机器校验后，
一键生成**有主张的设计稿**（不是空白表格）+ 蓝图总览图（essence）+（可选）文件结构图。

概念讨论最低标准（四步流，references/four-step-flow.md §①）：
    A 组（硬门槛，缺一拒绝出方案）：
        problem   A1 做什么    — 解决什么问题、产出什么（无默认，必须提供）
        audience  A2 给谁用    — 谁在什么场景打开它（无默认，必须提供）
        platform  A3 在哪跑    — 平台/环境（默认 workbuddy）
        entry     A4 新建/改进 — create / improve（默认 create）
    B 组（软门槛，缺则初稿标注粗版、允许出方案）：
        priority  B5 最在意做对哪点
        flow      B6 流程性质  — 一次干完/分步确认、标准化/灵活
        example   B7 一个具体样例
    C 组（加分，不阻塞）：
        boundary  C8 边界 / ecosystem C9 生态 / materials C10 历史资料
        （materials 自 v3.3.0 起进 infer_design：信号扫描 + BR-5 A 维证据；
          仍不阻塞出方案，但会真实影响推断结论）

用法：
    python scripts/blueprint_proto.py <蓝图目录> --name "<skill名>" --answers '<JSON>' [--output <dir>] [--archetype <id>] [--json] [--force]
    python scripts/sd_cli.py proto <蓝图目录> --name "<skill名>" --answers '<JSON>' ...

退出码：0 = 成功；1 = A 组缺失 / 参数错误 / 生成失败。
"""

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

from retry import read_text_robust, write_text_robust

ROOT = Path(__file__).resolve().parent.parent
PYTHON = sys.executable

# ─── 概念讨论最低标准（单一数据源，与 four-step-flow.md §① 对齐）───
A_GROUP = [
    ("problem", "A1 做什么", "解决什么问题、产出什么"),
    ("audience", "A2 给谁用", "谁在什么场景打开它"),
    ("platform", "A3 在哪跑", "平台/环境（默认 workbuddy）"),
    ("entry", "A4 新建/改进", "create / improve（默认 create）"),
]
B_GROUP = [
    ("priority", "B5 最在意做对哪点", "最不能错的是什么"),
    ("flow", "B6 流程性质", "一次干完/分步确认、标准化/灵活"),
    ("example", "B7 一个具体样例", "想象一个人具体怎么用一次"),
]
A_DEFAULTS = {"platform": "workbuddy", "entry": "create"}


def parse_answers(raw: str) -> dict:
    """解析 --answers：支持 JSON 文件路径或 JSON 字符串。"""
    p = Path(raw)
    if p.exists():
        return json.loads(read_text_robust(p))
    return json.loads(raw)


def run(cmd: list[str]) -> subprocess.CompletedProcess:
    """带 UTF-8 环境的子进程运行（同 sd_cli 约定）。"""
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    return subprocess.run(
        cmd, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        text=True, encoding="utf-8", errors="replace", check=False,
    )


def tick_visual_line(bp: Path, has_structure: bool) -> bool:
    """把 B07「可视化产物」行的 ☐ 按**实际产出**勾上。

    ②初步方案确实跑了 visualize_blueprint（必出），archetype 给了才跑 render_structure；
    按事实勾选，而不是留一堆 ☐ 让用户猜跑没跑。
    """
    p = bp / "07-计划.md"
    if not p.exists():
        return False
    text = read_text_robust(p)
    new = text
    if has_structure:
        new = new.replace("☐ 已跑 render_structure.py", "☑ 已跑 render_structure.py")
    new = new.replace("☐ 已跑 visualize_blueprint.py", "☑ 已跑 visualize_blueprint.py")
    if new == text:
        return False
    write_text_robust(p, new)
    return True


def read_design_from_blueprint(bp: Path) -> dict:
    """从既有蓝图的 index.md 回读设计结论（设计模式 / 结构框架）。

    用于「跳过创建」场景（目录已有蓝图、未加 --force）：此时不跑 draft，
    但仍需 archetype 才能出结构图。index.md 的快照表形如：
        | 设计模式（交互×内容） | Generator × D 模板渲染 【AI 建议】 |
        | 结构框架 | template（模板产出型 Generator） |
    解析失败时返回空 dict——降级为不出结构图，不阻塞主流程。
    """
    idx = bp / "index.md"
    if not idx.exists():
        return {}
    try:
        text = read_text_robust(idx)
    except Exception:
        return {}
    out: dict = {}
    m = re.search(r"^\|\s*设计模式[^|]*\|\s*([^|\n]+?)\s*\|", text, re.M)
    if m:
        out["pattern"] = re.sub(r"【[^】]*】", "", m.group(1)).strip()
    m = re.search(r"^\|?\s*结构框架[^|｜]*[|｜]\s*([^|\n]+?)\s*[|｜]?\s*$", text, re.M)
    if m:
        aid = re.sub(r"【[^】]*】", "", m.group(1)).strip()
        aid = re.split(r"[（(，,、\s]", aid)[0].strip()
        if aid:
            out["archetype"] = aid
    # 兜底：从 07-计划.md 的「结构框架 archetype」字段再找一次
    if "archetype" not in out:
        p = bp / "07-计划.md"
        if p.exists():
            try:
                t07 = read_text_robust(p)
            except Exception:
                t07 = ""
            m = re.search(r"结构框架\s*[:：]?\s*(?:archetype\s*)?[：:]?\s*"
                          r"[`'\"]?(\w+)[`'\"]?", t07)
            if m:
                out["archetype"] = m.group(1)
    return out


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

    ap = argparse.ArgumentParser(
        description="四步流 Step② 初步方案：概念讨论最低标准校验 → 有主张的设计稿 → essence 总览图 →（可选）结构图",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="--answers 字段对齐概念讨论最低标准：A 组 problem/audience/platform/entry（前二者必填），B 组 priority/flow/example。",
    )
    ap.add_argument("target", help="目标蓝图目录")
    ap.add_argument("--name", required=True, help="skill 名（写入 index title）")
    ap.add_argument("--answers", required=True,
                    help='概念讨论 JSON：{"problem":...,"audience":...,"platform":...,"entry":...,"priority":...,"flow":...,"example":...}')
    ap.add_argument("--output", "-o", help="可视化产物输出目录（默认 = 蓝图目录）")
    ap.add_argument("--archetype", "-a", help="结构框架 id（可选，给了则额外 render_structure 出结构图；不给则由 infer_design 自动推断）")
    ap.add_argument("--force", action="store_true", help="目标目录非空时先备份为 .bak-<时间戳> 再重建（默认跳过创建只出图）")
    ap.add_argument("--json", action="store_true", help="结构化输出（stdout 只有 JSON，便于机器解析）")
    args = ap.parse_args()

    def fail(msg: str, reason: str, extra: dict | None = None) -> int:
        """统一出口：--json 时只吐 JSON，绝不混入人类可读行。"""
        if args.json:
            payload = {"ok": False, "reason": reason, "error": msg}
            if extra:
                payload.update(extra)
            print(json.dumps(payload, ensure_ascii=False))
        else:
            print(f"❌ {msg}")
        return 1

    # 1. 解析概念讨论
    try:
        answers = parse_answers(args.answers)
        if not isinstance(answers, dict):
            raise ValueError("answers 必须是 JSON 对象")
    except Exception as e:
        return fail(f"--answers 解析失败：{e}", "PARSE_FAILED")

    # 2. A 组硬门槛（以终为始：缺哪项就喂不饱②初步方案对应的积木格）
    missing_a: list[str] = []
    defaults_used: list[str] = []
    for key, label, _ in A_GROUP:
        val = str(answers.get(key, "")).strip()
        if not val:
            if key in A_DEFAULTS:
                answers[key] = A_DEFAULTS[key]
                defaults_used.append(f"{label}={A_DEFAULTS[key]}")
            else:
                missing_a.append(f"{label}（{key}）")
    if missing_a:
        return fail(
            f"概念讨论 A 组硬门槛缺失，拒绝出方案（缺：{'、'.join(missing_a)}）",
            "A_GROUP_MISSING",
            {"missing_a": missing_a,
             "hint": "A1/A2 无默认值必须提供；缺项对应②初步方案的积木格将喂不饱（见 four-step-flow.md §①）"},
        )

    # 3. B 组软门槛（缺则粗版，允许出方案）
    missing_b = [label for key, label, _ in B_GROUP if not str(answers.get(key, "")).strip()]
    rough = len(missing_b) > 0

    # 4. 组装 draft_blueprint 需要的 answers
    #    ⚠️ P0 修复：先前这里只传 5 个字段，flow(B6)/example/boundary/ecosystem 全被丢掉，
    #    导致 infer_design 拿不到流程性质信号，模式只能靠 problem 文本瞎猜。现在整份透传。
    scenario = str(answers.get("audience", "")).strip()
    if answers.get("example"):
        scenario = f"{scenario}；示例：{str(answers['example']).strip()}"
    draft_answers = dict(answers)
    draft_answers["scenario"] = scenario
    draft_answers["name"] = args.name
    draft_answers.setdefault("platform", "workbuddy")
    draft_answers.setdefault("entry", "create")

    # 5. 生成蓝图（目标目录为空 → draft 一键成稿；已存在 → 默认跳过创建只出图，--force 则备份重建）
    target = Path(args.target).resolve()
    existed = target.exists() and any(target.iterdir())
    should_create = (not existed) or args.force
    # ⚠️ 必须在分支外初始化：跳过创建时也要能出结构图（见 §8）与报告（§10）。
    # 先前只在 should_create 分支内赋值，一旦走「跳过创建」就 UnboundLocalError。
    design_info: dict = {}
    if should_create:
        cmd = [
            PYTHON, str(ROOT / "scripts" / "draft_blueprint.py"), str(target),
            "--name", args.name, "--answers", json.dumps(draft_answers, ensure_ascii=False),
            "--platform", str(draft_answers["platform"]), "--entry", str(draft_answers["entry"]),
        ]
        if args.archetype:
            cmd += ["--archetype", args.archetype]
        if args.force:
            cmd += ["--force"]
        # 只调一次，且固定带 --json：草案生成与推断结论同一次拿到，
        # 避免二次调用把 --force 的备份动作又执行一遍。
        cmd += ["--json"]
        proc = run(cmd)
        if proc.returncode != 0:
            # --json 模式下 draft 把错误也写进 stdout 的 JSON，优先解析它
            try:
                err = json.loads(proc.stdout).get("error", "")
            except Exception:
                err = ""
            return fail(err or (proc.stderr or proc.stdout).strip() or "draft_blueprint 执行失败",
                        "DRAFT_FAILED")
        try:
            design_info = json.loads(proc.stdout).get("design", {})
        except Exception:
            design_info = {}
    elif target.joinpath("index.md").exists():
        # 跳过创建（目录已存在且未加 --force）：从既有蓝图读回设计结论，
        # 否则第 8 步拿不到 archetype，结构图会被静默跳过。
        design_info = read_design_from_blueprint(target)

    # 6. 粗版标记写入 index.md（幂等：已打过就不再追加）
    if rough and target.joinpath("index.md").exists():
        idx_path = target / "index.md"
        idx = read_text_robust(idx_path)
        if "粗版标记" not in idx:
            note = "\n> ⚠️ **粗版标记**：本稿为粗版（概念讨论缺 B 组：{}），③深化设计阶段需补齐。\n".format(
                "、".join(missing_b) or "—")
            write_text_robust(idx_path, idx + note)

    # 7. 内容要点总览图（essence）
    out_dir = Path(args.output).resolve() if args.output else target
    out_dir.mkdir(parents=True, exist_ok=True)
    svg = out_dir / "blueprint.svg"
    proc = run([PYTHON, str(ROOT / "scripts" / "visualize_blueprint.py"), str(target),
                "--mode", "essence", "--output", str(svg)])
    if proc.returncode != 0:
        return fail((proc.stderr or proc.stdout).strip() or "visualize_blueprint 执行失败",
                    "VISUALIZE_FAILED")

    # 8.（可选）文件结构图：显式 --archetype 优先，否则用推断结果自动出图。
    #    跳过创建时 design_info 由 read_design_from_blueprint() 从 index.md 回读，
    #    同样能出结构图——此前这里写了 `if should_create else None`，把回读结果丢了。
    structure_svg: str | None = None
    aid = args.archetype or design_info.get("archetype")
    if aid:
        structure_svg = str(out_dir / "structure.svg")
        proc = run([PYTHON, str(ROOT / "scripts" / "render_structure.py"), str(target),
                    "--archetype", aid, "--output", structure_svg])
        if proc.returncode != 0:
            return fail((proc.stderr or proc.stdout).strip() or "render_structure 执行失败",
                        "STRUCTURE_FAILED")

    # 9. 按实际产出回填 B07 的「可视化产物」勾选
    ticked = tick_visual_line(target, bool(structure_svg))

    # 10. 报告
    result = {
        "ok": True,
        "target": str(target),
        "name": args.name,
        "created": should_create,
        "skipped_create": existed and not args.force,
        "rough": rough,
        "missing_b": missing_b,
        "defaults_used": defaults_used,
        "design": design_info,
        "blueprint_svg": str(svg),
        "structure_svg": structure_svg,
        "visual_line_ticked": ticked,
        "next": "进入③深化设计：逐格确认 AI 建议（回「按建议」批量采纳）；标【需用户拍板】的字段必须由用户拍板",
    }
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0

    print(f"✅ A 组达标：4/4（{'；'.join(defaults_used) if defaults_used else '全部显式提供'}）")
    if rough:
        print(f"⚠️ 粗版：缺 B 组（{'、'.join(missing_b)}）→ ③深化设计需多一轮")
    if design_info:
        # 回读场景（跳过创建）只有 archetype id、没有 name/预估分，缺啥就不显示啥，
        # 别打出一堆「—」误导用户。
        aname = design_info.get("archetype_name", "")
        arch = design_info.get("archetype", "—")
        print(f"✅ 设计模式：{design_info.get('pattern', '—')} ｜ 结构框架："
              f"{arch + '（' + aname + '）' if aname else arch}")
        if design_info.get("focus"):
            print(f"   侧重段：{design_info['focus']}")
        if design_info.get("br5_avg"):
            print(f"   BR-5 预估：{design_info['br5_avg']} 分（EVS {design_info.get('evs', '—')}）")
    if should_create:
        print(f"✅ 已生成②初步方案（有主张的设计稿）：{target}")
    else:
        print(f"ℹ️ 蓝图目录已存在（{target}），跳过创建只出图；加 --force 可备份后重建。")
    print(f"✅ 内容要点总览图：{svg}")
    if structure_svg:
        print(f"✅ 文件结构图：{structure_svg}")
    if ticked:
        print("✅ 已按实际产出回填 B07「可视化产物」勾选")
    print("→ 下一步：进入③深化设计，逐格确认 AI 建议；标【需用户拍板】的字段必须由用户拍板。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
