#!/usr/bin/env python3
"""
Skill Scanner — Scans installed Skills and outputs structured analysis reports

Usage:
    python3 scan_skills.py --path ~/.qclaw/skills --output [json|table|markdown]
    python3 scan_skills.py --path ~/.qclaw/skills --output json --match "map,document"
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

# Risk keywords
RISK_HIGH_KEYWORDS = ["rm -rf", "sudo", "chmod 777", "eval(", "exec(", "subprocess.call", "os.system",
                       "token", "password", "secret", "apikey", "api_key", "credential",
                       "upload", "delete", "send", "publish", "deploy", "ssh"]
RISK_MEDIUM_KEYWORDS = ["api", "http", "fetch", "request", "oauth", "auth", "login",
                         "write", "update", "modify", "create_dir", "mkdir",
                         "pip install", "npm install", "brew install"]


def parse_frontmatter(content: str) -> dict:
    """Parse YAML frontmatter from SKILL.md"""
    fm = {}
    if not content.startswith("---"):
        return fm
    end = content.find("---", 3)
    if end == -1:
        return fm
    frontmatter = content[3:end].strip()
    for line in frontmatter.split("\n"):
        if ":" in line:
            key, _, val = line.partition(":")
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            if val and val != "|":
                fm[key] = val
    return fm


def assess_risk(skill_dir: Path, scripts: list) -> tuple:
    """Assess skill risk level"""
    risk_level = "low"
    risk_notes = []

    # Check script content
    for script_path in scripts:
        try:
            content = script_path.read_text(encoding="utf-8", errors="ignore").lower()
            for kw in RISK_HIGH_KEYWORDS:
                if kw in content:
                    risk_level = "high"
                    risk_notes.append(f"Script {script_path.name} contains high-risk keyword: {kw}")
            if risk_level != "high":
                for kw in RISK_MEDIUM_KEYWORDS:
                    if kw in content:
                        if risk_level == "low":
                            risk_level = "medium"
                        risk_notes.append(f"Script {script_path.name} contains medium-risk keyword: {kw}")
        except Exception:
            pass

    # Check for network-related files
    skill_files = list(skill_dir.rglob("*"))
    for f in skill_files:
        if f.is_file():
            try:
                content = f.read_text(encoding="utf-8", errors="ignore").lower()
                if any(kw in content for kw in ["curl", "wget", "requests.get", "fetch(", "http://", "https://"]):
                    if risk_level == "low":
                        risk_level = "medium"
                    risk_notes.append(f"File {f.name} involves network requests")
            except Exception:
                pass

    # Check for privilege-related content
    for f in skill_files:
        if f.is_file() and f.suffix in [".sh", ".py", ".js"]:
            try:
                content = f.read_text(encoding="utf-8", errors="ignore").lower()
                if "sudo" in content or "chmod" in content:
                    risk_level = "high"
                    risk_notes.append(f"File {f.name} involves privilege modification")
            except Exception:
                pass

    if not risk_notes:
        risk_notes.append("No obvious risks detected")

    return risk_level, risk_notes[:3]  # Return at most 3 notes


def get_dir_size(path: Path) -> float:
    """Get directory size (KB)"""
    total = 0
    for f in path.rglob("*"):
        if f.is_file():
            try:
                total += f.stat().st_size
            except Exception:
                pass
    return round(total / 1024, 1)


def scan_single_skill(skill_dir: Path) -> dict:
    """Scan a single skill directory"""
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return None

    content = skill_md.read_text(encoding="utf-8", errors="ignore")
    fm = parse_frontmatter(content)

    # Collect scripts
    scripts_dir = skill_dir / "scripts"
    scripts = list(scripts_dir.glob("*.py")) + list(scripts_dir.glob("*.sh")) + \
              list(scripts_dir.glob("*.js")) if scripts_dir.exists() else []

    # Collect reference docs
    refs_dir = skill_dir / "references"
    refs = list(refs_dir.glob("*.md")) if refs_dir.exists() else []

    # Collect assets
    assets_dir = skill_dir / "assets"
    assets = list(assets_dir.rglob("*")) if assets_dir.exists() else []

    # Detect dependencies
    dependencies = []
    all_content = content
    for s in scripts:
        try:
            all_content += "\n" + s.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            pass

    dep_patterns = {
        "python3": r"python3|pip3|pip install",
        "node": r"node|npm|npx",
        "go": r"\bgo \w+|go build|go run",
        "ffmpeg": r"ffmpeg",
        "curl": r"\bcurl\b",
        "java": r"java|jar|jdk",
        "docker": r"docker",
    }
    for dep, pattern in dep_patterns.items():
        if re.search(pattern, all_content, re.IGNORECASE):
            dependencies.append(dep)

    # Risk assessment
    risk_level, risk_notes = assess_risk(skill_dir, scripts)

    return {
        "name": fm.get("name", skill_dir.name),
        "description": fm.get("description", "(no description)"),
        "dir_size_kb": get_dir_size(skill_dir),
        "file_count": sum(1 for _ in skill_dir.rglob("*") if _.is_file()),
        "has_scripts": len(scripts) > 0,
        "has_references": len(refs) > 0,
        "has_assets": len(assets) > 0,
        "scripts_list": [s.name for s in scripts],
        "dependencies": list(set(dependencies)),
        "risk_level": risk_level,
        "risk_notes": risk_notes,
    }


def scan_all_skills(skills_path: str) -> list:
    """Scan all skills"""
    base = Path(skills_path).expanduser()
    if not base.exists():
        return []

    results = []
    for item in sorted(base.iterdir()):
        if item.is_dir() and not item.name.startswith("."):
            info = scan_single_skill(item)
            if info:
                results.append(info)
    return results


def print_table(skills: list):
    """Table output"""
    print(f"\n{'='*120}")
    print(f"📋 Installed Skills Inventory ({len(skills)} total)")
    print(f"{'='*120}")
    print(f"{'Name':<30} {'Size(KB)':<10} {'Files':<8} {'Scripts':<8} {'Deps':<20} {'Risk':<8}")
    print(f"{'-'*120}")
    for s in skills:
        deps = ",".join(s["dependencies"]) if s["dependencies"] else "-"
        print(f"{s['name']:<30} {s['dir_size_kb']:<10} {s['file_count']:<8} "
              f"{'✓' if s['has_scripts'] else '✗':<8} {deps:<20} {s['risk_level']:<8}")
    print(f"{'='*120}\n")

    # Risk summary
    high_risk = [s for s in skills if s["risk_level"] == "high"]
    medium_risk = [s for s in skills if s["risk_level"] == "medium"]
    print(f"⚠️  Risk Summary: {len(high_risk)} high risk, {len(medium_risk)} medium risk, {len(skills)-len(high_risk)-len(medium_risk)} low risk")
    if high_risk:
        print("\n🔴 High-risk skills:")
        for s in high_risk:
            print(f"  - {s['name']}: {'; '.join(s['risk_notes'])}")
    print()


def print_markdown(skills: list):
    """Markdown output"""
    print(f"# 📋 Installed Skills Inventory ({len(skills)} total)\n")
    print(f"| Name | Size(KB) | Files | Scripts | Deps | Risk |")
    print(f"|------|----------|-------|---------|------|------|")
    for s in skills:
        deps = ", ".join(s["dependencies"]) if s["dependencies"] else "-"
        print(f"| {s['name']} | {s['dir_size_kb']} | {s['file_count']} | "
              f"{'✓' if s['has_scripts'] else '✗'} | {deps} | {s['risk_level']} |")

    # Risk summary
    high_risk = [s for s in skills if s["risk_level"] == "high"]
    medium_risk = [s for s in skills if s["risk_level"] == "medium"]
    low_risk = [s for s in skills if s["risk_level"] == "low"]

    print(f"\n## ⚠️ Risk Summary\n")
    print(f"- 🟢 Low risk: {len(low_risk)}")
    print(f"- 🟡 Medium risk: {len(medium_risk)}")
    print(f"- 🔴 High risk: {len(high_risk)}")

    if high_risk:
        print(f"\n### 🔴 High-Risk Skill Details\n")
        for s in high_risk:
            print(f"- **{s['name']}**: {'; '.join(s['risk_notes'])}")
    if medium_risk:
        print(f"\n### 🟡 Medium-Risk Skill Details\n")
        for s in medium_risk:
            print(f"- **{s['name']}**: {'; '.join(s['risk_notes'])}")

    # Functional categories
    print(f"\n## 📊 Functional Categories\n")
    categories = {
        "Document Processing": ["docx", "pdf", "xlsx", "tencent-docs", "kdocs", "youdaonote", "notion"],
        "Email & Communication": ["email-skill", "agent-email", "imap-smtp-email", "personal-mail-skill"],
        "Maps & Location": ["tencentmap-jsapi-gl-skill", "tencentmap-webservice-skill", "baidu-ai-map"],
        "Financial Data": ["hithink-mcp", "tongdaxin-mcp", "qcc-company", "qibook-mcp", "yuandian"],
        "Travel & Transportation": ["chengxin", "flyai", "meituan-travel", "wendao-partner-qclaw-skill", "meituan-paotui"],
        "Enterprise Collaboration": ["lark-setup", "wecomcli-setup", "wecom-weisheng-scrm", "tencent-meeting-mcp"],
        "Development Tools": ["qclaw-env", "qclaw-skill-creator", "find-skills", "mcporter", "codex", "xbrowser"],
        "Content Creation": ["qclaw-generate-image", "fbs_bookwriter", "aippt", "tencent-musician-skills"],
        "Lifestyle Services": ["mcd-mcp", "mtunion-product-ai-guide", "qqmusic", "weread-skills", "tencent-news"],
        "System Management": ["qclaw-rules", "qclaw-cron-skill", "persona-switch", "another_them", "skill-manager"],
        "Cloud Storage": ["cloud-upload-backup", "weiyun", "bdpan-storage"],
        "Legal & Compliance": ["tencent-esign-contract", "tencent-survey", "tencentads"],
    }

    for cat, names in categories.items():
        matched = [s for s in skills if s["name"] in names]
        if matched:
            print(f"### {cat}")
            for s in matched:
                desc = s["description"][:60] + "..." if len(s["description"]) > 60 else s["description"]
                print(f"- **{s['name']}**: {desc}")
            print()


def match_skills(skills: list, keywords: str) -> list:
    """Match skills by keywords"""
    kw_list = [k.strip().lower() for k in keywords.split(",")]
    matched = []
    for s in skills:
        text = (s["name"] + " " + s["description"]).lower()
        for kw in kw_list:
            if kw in text:
                matched.append(s)
                break
    return matched


def main():
    parser = argparse.ArgumentParser(description="Scan installed QClaw/OpenClaw skills")
    parser.add_argument("--path", default="~/.qclaw/skills", help="Skills directory path")
    parser.add_argument("--output", choices=["json", "table", "markdown"], default="table", help="Output format")
    parser.add_argument("--match", help="Keyword match (comma-separated) to filter skills relevant to the current task")
    args = parser.parse_args()

    skills = scan_all_skills(args.path)

    if not skills:
        print("No installed skills found.", file=sys.stderr)
        sys.exit(1)

    if args.match:
        skills = match_skills(skills, args.match)
        if not skills:
            print(f"No skills matching '{args.match}' found.", file=sys.stderr)
            sys.exit(0)

    if args.output == "json":
        print(json.dumps(skills, ensure_ascii=False, indent=2))
    elif args.output == "table":
        print_table(skills)
    elif args.output == "markdown":
        print_markdown(skills)


if __name__ == "__main__":
    main()
