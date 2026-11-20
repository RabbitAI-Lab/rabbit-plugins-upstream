"""只读检查标准 Phase → Task 清单中的显式依赖，支持 Python 3.9+。"""

import argparse
from graphlib import CycleError, TopologicalSorter
from pathlib import Path
import re


def check(text: str, *, require_final: bool = False) -> tuple[int, int]:
    declarations = {}
    dependencies = {}
    owners = {}
    phases = set()
    phase = current = None
    final = None
    fence = ""
    for number, raw in enumerate(text.splitlines(), 1):
        line = raw.strip()
        if fence:
            if line.startswith(fence) and not line.strip(fence[0]):
                fence = ""
            continue
        marker = re.match(r"^(`{3,}|~{3,})", line)
        if marker:
            fence = marker[1]
            continue

        if require_final and (match := re.fullmatch(r"- (?:最终 Phase|Final Phase)\s*[：:]\s*(P[0-9]+)[。.]?", line)):
            if final is not None:
                raise ValueError("最终 Phase 声明重复")
            final = match[1]
            continue
        if re.match(r"^##\s+Phase\b", line):
            match = re.match(r"^##\s+Phase\s+(P[0-9]+)(?=[\s：:]|$)", line)
            if not match:
                raise ValueError(f"第 {number} 行阶段编号不属于标准 P 格式，需原位核对")
            phase = current = match[1]
            phases.add(phase)
        elif line.startswith("## "):
            phase = current = None
            continue
        elif re.match(r"^- \[[ xX]\]", line):
            match = re.match(r"^- \[[ xX]\]\s+(T[0-9]+)(?=[\s：:]|$)", line)
            if not match or phase is None:
                raise ValueError(f"第 {number} 行任务缺少标准 Phase 归属或 T 编号，需原位核对")
            current = match[1]
            owners[current] = phase
        elif match := re.match(r"^- (?:(?:额外)?依赖|Dependencies)\s*[：:]\s*(.*)$", line):
            if current is None or current in dependencies:
                raise ValueError(f"第 {number} 行依赖没有唯一的归属项")
            value = match[1].strip().rstrip("。.")
            if value.lower() in {"无", "none"}:
                dependencies[current] = []
            elif re.fullmatch(r"[PT][0-9]+(?:\s*[、,，]\s*[PT][0-9]+)*", value):
                dependencies[current] = re.split(r"\s*[、,，]\s*", value)
            else:
                raise ValueError(f"第 {number} 行 {current} 的依赖须为编号列表或“无”，其他写法需人工核对")
            continue
        else:
            continue
        if current in declarations:
            raise ValueError(f"第 {number} 行 {current} 重复，首次声明在第 {declarations[current]} 行")
        declarations[current] = number

    if not phases:
        raise ValueError("未识别标准 Phase / Task 清单，请按原格式核对")
    for item in declarations:
        if item not in dependencies:
            raise ValueError(f"{item} 缺少依赖字段")
        for dep in dependencies[item]:
            if dep not in declarations:
                raise ValueError(f"{item} 引用了未声明的 {dep}")
    empty = phases.difference(owners.values())
    if empty:
        raise ValueError(f"阶段没有所属 Task：{'、'.join(sorted(empty))}")
    predecessors = {item: set(deps) for item, deps in dependencies.items()}
    for item, deps in dependencies.items():
        phase = owners.get(item, item)
        for dependency in deps:
            prerequisite_phase = owners.get(dependency, dependency)
            if prerequisite_phase != phase:
                predecessors[phase].add(prerequisite_phase)
    for task, parent in owners.items():
        # 阶段完成要等所属任务。每项任务开工要等阶段前置。
        predecessors[parent].add(task)
        predecessors[task].update(dependencies[parent])
    try:
        list(TopologicalSorter(predecessors).static_order())
    except CycleError as error:
        raise ValueError("存在依赖环：" + " → ".join(error.args[1])) from error
    if require_final:
        if final not in phases:
            raise ValueError("需要声明已存在的最终 Phase，例如“- 最终 Phase：P002。”")
        reached = set()
        pending = [final]
        while pending:
            node = pending.pop()
            if node not in reached:
                reached.add(node)
                pending.extend(predecessors[node])
        missing = phases - reached
        if missing:
            raise ValueError(f"最终阶段 {final} 未依赖阶段：{'、'.join(sorted(missing))}")
    return len(phases), len(owners)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tasks", type=Path, help="按包内模板编写的任务清单")
    parser.add_argument("--require-final", action="store_true", help="检查重型清单的最终阶段及其依赖覆盖")
    args = parser.parse_args()
    try:
        phase_count, task_count = check(args.tasks.read_text(encoding="utf-8"), require_final=args.require_final)
    except (ValueError, OSError) as error:
        parser.exit(1, f"{error}\n")
    print(f"显式依赖通过：{phase_count} 个阶段，{task_count} 个任务。验收条件和实际进度另行核对。")
