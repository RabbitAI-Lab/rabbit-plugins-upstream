#!/usr/bin/env python3
"""
Skill Packager - 校验后打包 skill 为 zip，并可一键安装到多个 Agent 宿主

Usage:
    python package_skill.py <path/to/skill-folder> [output-directory]
    python package_skill.py skills/public/my-skill
    python package_skill.py skills/public/my-skill ./dist
    python package_skill.py skills/public/my-skill --target agents          # 默认：用户级跨客户端
    python package_skill.py skills/public/my-skill --target all             # 全部标准位置
    python package_skill.py skills/public/my-skill --target codex,copilot   # agent 名 = 共享位置别名

流程：先调 validate.py 硬钳校验 → FAIL 即拒打包 → PASS 后生成 zip → 可按 --target 复制到各宿主 skills 目录

跨 Agent 安装设计（2026-08-31 重构）：
agentskills.io 规范**不规定** skill 目录位置，但生态已收敛到共享位置 `.agents/skills/`
（项目级）与 `~/.agents/skills/`（用户级）——这是规范定义的"跨客户端互操作"位置，
Codex / Copilot / Gemini / Cursor / Hermes / Augment 等合规客户端都扫描它。
因此**无需为每个 agent 单独硬编码目录**：codex/copilot/cursor/gemini/hermes 等
只是同一共享位置的别名，装一次即可被多 agent 自动发现。
仅 Claude 原生 `~/.claude/skills/`、WorkBuddy 原生 `~/.workbuddy/skills/`、
豆包/Coze 私有 `.agent/skills/` 作为独立标准位置单列。
"""
import sys
import os
import shutil
import subprocess
import zipfile
from pathlib import Path

# validate.py 在同目录
SCRIPT_DIR = Path(__file__).parent.resolve()
VALIDATE_PY = SCRIPT_DIR / "validate.py"

# ── 规范定义的"跨客户端互操作"位置（agentskills.io integrate 指南）─────────
# 合规客户端（Codex/Copilot/Gemini/Cursor/Hermes/Augment…）都扫描这两个，
# 因此它们是安装 skill 的"最小充分集"，无需枚举每个 agent 的私有目录。
STANDARD_TARGETS = {
    "agents":         "~/.agents/skills",     # 用户级跨客户端（默认安装位置）
    "agents-project": ".agents/skills",       # 项目级跨客户端（可随 git 提交团队共享）
    "claude":         "~/.claude/skills",     # Claude Code 原生位置
    "claude-project": ".claude/skills",       # 项目级 Claude
    "workbuddy":      "~/.workbuddy/skills",  # WorkBuddy 原生（用户级，跨项目）
    "coze":           ".agent/skills",        # 豆包/Coze 私有约定（云端 .skill 打包另处）
}

# ── agent 名别名 → 规范目标（消除"9 目录硬钳"）──────────────────────────
# 这些 agent 都扫描 `.agents/skills/`，故统一指向 "agents" 共享位置；
# 用户用 --target codex / copilot / ... 时，实质装到同一处，多 agent 自动发现。
TARGET_ALIASES = {
    "copilot":  "agents",
    "codex":    "agents",
    "openclaw": "agents",
    "cursor":   "agents",
    "gemini":   "agents",
    "hermes":   "agents",
}

# 合并：规范目标 + 别名，供安装时统一查表
TARGET_MAP = {**STANDARD_TARGETS, **{a: STANDARD_TARGETS[c] for a, c in TARGET_ALIASES.items()}}

# 打包时跳过的开发期文件
SKIP_FILES = ('.gitkeep', '.gitignore', '.DS_Store')
SKIP_DIR_PARTS = ('__pycache__',)


def safe_print(message):
    try:
        print(message)
    except UnicodeEncodeError:
        import re
        clean = re.sub(r'[\U0001F300-\U0001F9FF]', '', message)
        print(clean.strip())


if sys.platform == 'win32':
    try:
        if hasattr(sys.stdout, 'reconfigure'):
            sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass


def run_validate(skill_path):
    """调用 validate.py 校验。返回 (passed, exit_code)。"""
    if not VALIDATE_PY.exists():
        safe_print("⚠️  validate.py 未找到，跳过校验（不推荐）")
        return True, 0

    # 用当前 python 解释器跑 validate.py
    py = sys.executable or "python"
    try:
        result = subprocess.run(
            [py, str(VALIDATE_PY), str(skill_path)],
            capture_output=True, text=True, encoding='utf-8', errors='replace'
        )
    except Exception as e:
        safe_print(f"⚠️  调用 validate.py 失败：{e}，跳过校验")
        return True, 0

    # 打印校验输出
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr)

    # 退出码：0=PASS, 1=ERROR(拒), 2=WARNING(可过)
    if result.returncode == 1:
        safe_print("❌ 校验失败（ERROR），拒绝打包")
        return False, 1
    elif result.returncode == 2:
        safe_print("⚠️  校验通过但有 WARNING，继续打包（建议修复）")
        return True, 2
    else:
        return True, 0


def _resolve_target_dir(raw):
    """解析宿主安装目录：绝对/~ 路径展开家目录；相对路径相对 CWD。"""
    if raw.startswith('~') or raw.startswith('/') or (len(raw) > 1 and raw[1] == ':'):
        return Path(raw).expanduser().resolve()
    return Path(raw).resolve()


def install_to_target(skill_path, target_name, targets_map=None):
    """把 skill 复制到指定宿主/位置的 skills 目录。返回是否成功。"""
    targets_map = targets_map or TARGET_MAP
    # 解析 agent 别名 → 规范目标（如 codex → agents）
    canon = TARGET_ALIASES.get(target_name, target_name)
    if canon not in targets_map:
        accepted = ', '.join(sorted(set(list(STANDARD_TARGETS) + list(TARGET_ALIASES))))
        safe_print(f"❌ 未知 target：{target_name}（可选：{accepted}）")
        return False

    dest_root = _resolve_target_dir(targets_map[canon])
    skill_name = skill_path.name
    dest = dest_root / skill_name

    # 清旧后写入（幂等）
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True, exist_ok=True)

    count = 0
    for f in skill_path.rglob('*'):
        if not f.is_file():
            continue
        if f.name in SKIP_FILES:
            continue
        if any(part in SKIP_DIR_PARTS for part in f.parts):
            continue
        rel = f.relative_to(skill_path)
        target = dest / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(f, target)
        count += 1

    safe_print(f"✅ 已安装到 [{canon}] {dest}（{count} 文件）")
    return True


def package_skill(skill_path, output_dir=None):
    """打包 skill 为 zip。返回 zip 路径或 None。"""
    skill_path = Path(skill_path).resolve()

    if not skill_path.exists():
        safe_print(f"❌ 目录不存在：{skill_path}")
        return None
    if not skill_path.is_dir():
        safe_print(f"❌ 不是目录：{skill_path}")
        return None

    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        safe_print(f"❌ 缺 SKILL.md：{skill_path}")
        return None

    # 硬钳校验
    safe_print("🔍 运行 validate.py 硬钳校验...")
    passed, _ = run_validate(skill_path)
    if not passed:
        safe_print("   请修复校验错误后再打包。")
        return None
    print()

    # 输出位置
    skill_name = skill_path.name
    if output_dir:
        output_path = Path(output_dir).resolve()
        output_path.mkdir(parents=True, exist_ok=True)
    else:
        output_path = Path.cwd()

    zip_filename = output_path / f"{skill_name}.zip"

    # 打包
    try:
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            count = 0
            for file_path in skill_path.rglob('*'):
                if file_path.is_file():
                    # 跳过开发期文件（不入包）：.gitkeep/.gitignore/.DS_Store/__pycache__
                    if file_path.name in SKIP_FILES:
                        continue
                    if any(part in SKIP_DIR_PARTS for part in file_path.parts):
                        continue
                    arcname = file_path.relative_to(skill_path.parent)
                    zipf.write(file_path, arcname)
                    count += 1
            safe_print(f"✅ 打包完成：{zip_filename}（{count} 文件）")
            return zip_filename
    except Exception as e:
        safe_print(f"❌ 打包失败：{e}")
        return None


def main():
    argv = sys.argv[1:]

    # 解析 --target（支持单值 / all / 逗号列表），其余按位置参数处理
    targets = None
    positional = []
    i = 0
    while i < len(argv):
        if argv[i] == '--target':
            targets = argv[i + 1] if (i + 1) < len(argv) else 'all'
            i += 2
        else:
            positional.append(argv[i])
            i += 1

    if len(positional) < 1:
        print("Usage: python package_skill.py <path/to/skill-folder> [output-directory] [--target agents|claude|workbuddy|coze|all|<agent名>]")
        print("\nExamples:")
        print("  python package_skill.py skills/public/my-skill")
        print("  python package_skill.py skills/public/my-skill ./dist")
        print("  python package_skill.py skills/public/my-skill --target agents")
        print("  python package_skill.py skills/public/my-skill --target all")
        print("  python package_skill.py skills/public/my-skill --target codex,copilot,claude")
        sys.exit(1)

    skill_path = positional[0]
    output_dir = positional[1] if len(positional) > 1 else None

    safe_print(f"📦 打包 skill: {skill_path}")
    if output_dir:
        safe_print(f"   输出目录: {output_dir}")
    if targets:
        safe_print(f"   多目标安装: {targets}")
    print()

    result = package_skill(skill_path, output_dir)

    # 多目标安装（校验已通过才会走到这）
    if targets and result:
        if targets == 'all':
            tlist = list(STANDARD_TARGETS.keys())
        else:
            seen = set()
            tlist = []
            for t in [x.strip() for x in targets.split(',') if x.strip()]:
                canon = TARGET_ALIASES.get(t, t)
                if canon not in seen:
                    seen.add(canon)
                    tlist.append(canon)
        print()
        safe_print(f"🎯 多目标安装（{len(tlist)} 个位置）")
        ok = 0
        for t in tlist:
            if install_to_target(Path(skill_path).resolve(), t):
                ok += 1
        safe_print(f"   已安装到 {ok}/{len(tlist)} 个目标")

    sys.exit(0 if result else 1)


if __name__ == "__main__":
    main()
