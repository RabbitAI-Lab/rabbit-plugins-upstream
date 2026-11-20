"""Check explicit dependencies in a standard Phase / Task list (Python 3.9+)."""

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
                raise ValueError("Final Phase declared more than once")
            final = match[1]
            continue
        if re.match(r"^##\s+Phase\b", line):
            match = re.match(r"^##\s+Phase\s+(P[0-9]+)(?=[\s：:]|$)", line)
            if not match:
                raise ValueError(f"Line {number}: expected a phase ID starting with P")
            phase = current = match[1]
            phases.add(phase)
        elif line.startswith("## "):
            phase = current = None
            continue
        elif re.match(r"^- \[[ xX]\]", line):
            match = re.match(r"^- \[[ xX]\]\s+(T[0-9]+)(?=[\s：:]|$)", line)
            if not match or phase is None:
                raise ValueError(f"Line {number}: expected a T ID inside a Phase")
            current = match[1]
            owners[current] = phase
        elif match := re.match(r"^- (?:(?:额外)?依赖|Dependencies)\s*[：:]\s*(.*)$", line):
            if current is None or current in dependencies:
                raise ValueError(f"Line {number}: dependency field is unowned or duplicated")
            value = match[1].strip().rstrip("。.")
            if value.lower() in {"无", "none"}:
                dependencies[current] = []
            elif re.fullmatch(r"[PT][0-9]+(?:\s*[、,，]\s*[PT][0-9]+)*", value):
                dependencies[current] = re.split(r"\s*[、,，]\s*", value)
            else:
                raise ValueError(f"Line {number}: dependencies of {current} must be IDs or none")
            continue
        else:
            continue
        if current in declarations:
            raise ValueError(f"Line {number}: duplicate {current}, first declared on line {declarations[current]}")
        declarations[current] = number

    if not phases:
        raise ValueError("No standard phases found. Review custom formats directly")
    for item in declarations:
        if item not in dependencies:
            raise ValueError(f"Missing Dependencies field for {item}")
        for dep in dependencies[item]:
            if dep not in declarations:
                raise ValueError(f"{item} references unknown ID {dep}")
    empty = phases.difference(owners.values())
    if empty:
        raise ValueError(f"Phases without tasks: {', '.join(sorted(empty))}")
    predecessors = {item: set(deps) for item, deps in dependencies.items()}
    for item, deps in dependencies.items():
        phase = owners.get(item, item)
        for dependency in deps:
            prerequisite_phase = owners.get(dependency, dependency)
            if prerequisite_phase != phase:
                predecessors[phase].add(prerequisite_phase)
    for task, parent in owners.items():
        # Phase completion waits for its tasks. Each task inherits the phase prerequisites.
        predecessors[parent].add(task)
        predecessors[task].update(dependencies[parent])
    try:
        list(TopologicalSorter(predecessors).static_order())
    except CycleError as error:
        raise ValueError("Dependency cycle: " + " → ".join(error.args[1])) from error
    if require_final:
        if final not in phases:
            raise ValueError("Declare an existing final phase, e.g. - Final Phase: P002")
        reached = set()
        pending = [final]
        while pending:
            node = pending.pop()
            if node not in reached:
                reached.add(node)
                pending.extend(predecessors[node])
        missing = phases - reached
        if missing:
            raise ValueError(f"Final phase {final} does not cover: {', '.join(sorted(missing))}")
    return len(phases), len(owners)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tasks", type=Path, help="Task list in the bundled format")
    parser.add_argument("--require-final", action="store_true", help="Require the final phase to depend on every other phase")
    args = parser.parse_args()
    try:
        phase_count, task_count = check(args.tasks.read_text(encoding="utf-8"), require_final=args.require_final)
    except (ValueError, OSError) as error:
        parser.exit(1, f"{error}\n")
    print(f"Explicit dependencies OK: {phase_count} phases, {task_count} tasks. Check acceptance and actual progress separately.")
