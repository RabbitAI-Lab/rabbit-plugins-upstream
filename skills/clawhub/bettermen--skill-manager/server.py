#!/usr/bin/env python3
"""
Skill Manager SaaS — FastAPI Backend Server
启动: python server.py [--port 8765] [--host 0.0.0.0]
"""

import os
import sys
import json
from pathlib import Path

try:
    from fastapi import FastAPI, Query, HTTPException
    from fastapi.staticfiles import StaticFiles
    from fastapi.responses import FileResponse, JSONResponse
    from fastapi.middleware.cors import CORSMiddleware
except ImportError:
    print("请先安装 fastapi: pip install fastapi uvicorn")
    sys.exit(1)

# 添加 scripts 目录到 path，以便导入 audit 模块
SCRIPT_DIR = Path(__file__).parent / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))
from audit import audit as run_audit, parse_frontmatter

app = FastAPI(
    title="Skill Manager SaaS",
    description="WorkBuddy Skill 全生命周期管理平台",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 默认路径
USER_SKILLS_DIR = os.path.expanduser("~/.workbuddy/skills")
BUILTIN_SKILLS_DIR = None  # 内置 skill 目录，只读


def get_skills_dir():
    return os.path.expanduser("~/.workbuddy/skills")


def get_skill_info(skill_dir_name, base_dir=None):
    """获取单个 skill 的完整信息"""
    if base_dir is None:
        base_dir = get_skills_dir()

    skill_path = os.path.join(base_dir, skill_dir_name)
    skill_md = os.path.join(skill_path, "SKILL.md")

    if not os.path.exists(skill_md):
        return {
            "name": skill_dir_name,
            "dir_name": skill_dir_name,
            "exists": False,
            "error": "SKILL.md not found",
        }

    fm = parse_frontmatter(skill_md)
    if not fm:
        return {
            "name": skill_dir_name,
            "dir_name": skill_dir_name,
            "exists": True,
            "frontmatter_valid": False,
        }

    # 资源探测
    has_scripts = os.path.isdir(os.path.join(skill_path, "scripts"))
    has_references = os.path.isdir(os.path.join(skill_path, "references"))
    has_assets = os.path.isdir(os.path.join(skill_path, "assets"))
    has_market_meta = os.path.exists(os.path.join(skill_path, "_skillhub_meta.json"))

    # 来源类型
    if has_market_meta:
        source_type = "marketplace"
    elif fm.get("agent_created", "").lower() in ("true", "yes", "1"):
        source_type = "agent"
    else:
        source_type = "unknown"

    return {
        "name": fm.get("name", skill_dir_name),
        "dir_name": skill_dir_name,
        "display_name": fm.get("display_name", fm.get("name", skill_dir_name)),
        "version": fm.get("version", "?"),
        "description": (fm.get("description", "") or "")[:200],
        "agent_created": fm.get("agent_created", "").lower() in ("true", "yes", "1"),
        "source_type": source_type,
        "exists": True,
        "frontmatter_valid": True,
        "resources": {
            "scripts": has_scripts,
            "references": has_references,
            "assets": has_assets,
            "marketplace_meta": has_market_meta,
        },
        "raw_frontmatter": fm,
    }


# ============ API Routes ============

@app.get("/api/health")
def health():
    return {"status": "ok", "message": "Skill Manager SaaS is running"}


@app.get("/api/stats")
def stats():
    """获取统计摘要"""
    result = run_audit(get_skills_dir(), output_json=True)
    summary = result["summary"]
    return {
        "total_skills": summary["total_skills"],
        "p0_count": summary["p0_count"],
        "p1_count": summary["p1_count"],
        "p2_count": summary["p2_count"],
        "ok_count": summary["ok_count"],
        "duplicate_groups": summary["duplicate_groups"],
        "agent_count": sum(1 for s in result["skills"] if s.get("source_type") == "agent"),
        "marketplace_count": sum(1 for s in result["skills"] if s.get("source_type") == "marketplace"),
        "project_count": sum(1 for s in result["skills"] if s.get("source") == "项目级"),
    }


@app.get("/api/skills")
def list_skills(
    q: str = Query("", description="搜索关键字"),
    source: str = Query("", description="来源过滤: agent/marketplace/unknown"),
    level: str = Query("", description="严重度过滤: P0/P1/P2/ok"),
    sort: str = Query("name", description="排序字段: name/version/source_type/level"),
    page: int = Query(1, ge=1),
    page_size: int = Query(50, ge=1, le=200),
):
    """列出所有技能，支持搜索、过滤、排序、分页"""
    result = run_audit(get_skills_dir(), output_json=True)
    skills = result["skills"]

    # 过滤
    if q:
        q_lower = q.lower()
        skills = [
            s for s in skills
            if q_lower in s.get("name", "").lower()
            or q_lower in s.get("description", "").lower()
        ]

    if source:
        skills = [s for s in skills if s.get("source_type") == source]

    if level:
        skills = [s for s in skills if s.get("level") == level]

    # 排序
    if sort in ("name", "version", "source_type", "level"):
        skills.sort(key=lambda s: s.get(sort, ""))

    # 分页
    total = len(skills)
    start = (page - 1) * page_size
    end = start + page_size
    page_data = skills[start:end]

    # 附加问题信息
    all_issues = result["issues"]
    skill_issues_map = {}
    for issue in all_issues.get("P0", []) + all_issues.get("P1", []) + all_issues.get("P2", []):
        skill_name = issue.get("name", "")
        if skill_name:
            skill_issues_map.setdefault(skill_name, []).append(issue)

    for s in page_data:
        s["issue_count"] = len(skill_issues_map.get(s["name"], []))

    return {
        "total": total,
        "page": page,
        "page_size": page_size,
        "total_pages": (total + page_size - 1) // page_size,
        "skills": page_data,
    }


@app.get("/api/skills/{skill_name}")
def skill_detail(skill_name: str):
    """获取单个技能详情（含 SKILL.md 完整内容）"""
    base_dir = get_skills_dir()
    skill_path = os.path.join(base_dir, skill_name)

    if not os.path.isdir(skill_path):
        raise HTTPException(status_code=404, detail=f"Skill '{skill_name}' not found")

    info = get_skill_info(skill_name, base_dir)

    # 读取 SKILL.md 完整内容
    skill_md_path = os.path.join(skill_path, "SKILL.md")
    raw_content = ""
    if os.path.exists(skill_md_path):
        try:
            with open(skill_md_path, "r", encoding="utf-8") as f:
                raw_content = f.read()
        except Exception:
            raw_content = "(读取失败)"

    # 文件列表
    files = []
    for root, dirs, filenames in os.walk(skill_path):
        for f in filenames:
            rel = os.path.relpath(os.path.join(root, f), skill_path)
            size = os.path.getsize(os.path.join(root, f))
            files.append({"path": rel, "size": size})

    # 总大小
    total_size = sum(f["size"] for f in files)

    info["raw_content"] = raw_content
    info["files"] = files
    info["total_size"] = total_size
    info["total_files"] = len(files)

    return info


@app.get("/api/audit")
def audit_report(format: str = Query("full", description="输出格式: full/summary/skills")):
    """全量审计报告"""
    result = run_audit(get_skills_dir(), output_json=True)

    if format == "summary":
        return result["summary"]
    elif format == "skills":
        return result["skills"]
    else:
        return result


@app.post("/api/audit/fix")
def audit_fix(confirm: bool = Query(False, description="确认执行修复")):
    """自动修复已知问题（需确认）"""
    if not confirm:
        return {"message": "请添加 ?confirm=true 确认执行修复", "preview": True}

    fixed = []
    base_dir = get_skills_dir()

    # 修复 1: 删除遗留 .zip 文件
    if os.path.isdir(base_dir):
        for entry in os.listdir(base_dir):
            if entry.endswith(".zip"):
                zip_path = os.path.join(base_dir, entry)
                try:
                    os.remove(zip_path)
                    fixed.append(f"已删除遗留 .zip: {entry}")
                except Exception as e:
                    fixed.append(f"删除失败 {entry}: {e}")

    return {"fixed": fixed, "count": len(fixed)}


@app.delete("/api/skills/{skill_name}")
def delete_skill(skill_name: str, confirm: bool = Query(False, description="确认删除")):
    """删除技能（需确认）"""
    if not confirm:
        info = get_skill_info(skill_name)
        return {
            "message": f"即将删除技能: {info.get('display_name', skill_name)}",
            "requires_confirmation": True,
            "preview": info,
        }

    skill_path = os.path.join(get_skills_dir(), skill_name)

    if not os.path.isdir(skill_path):
        raise HTTPException(status_code=404, detail=f"Skill '{skill_name}' not found")

    info = get_skill_info(skill_name)

    # 安全检查：拒绝删除非 agent_created 技能
    if not info.get("agent_created"):
        raise HTTPException(
            status_code=403,
            detail=f"技能 '{skill_name}' 非自建技能，请在 WorkBuddy 技能管理面板操作",
        )

    # 执行删除
    import shutil
    try:
        shutil.rmtree(skill_path)
        return {
            "success": True,
            "message": f"已删除技能: {info.get('display_name', skill_name)} ({skill_name})",
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"删除失败: {e}")


@app.get("/api/skills/{skill_name}/raw")
def skill_raw(skill_name: str):
    """获取原始 SKILL.md 内容"""
    skill_md_path = os.path.join(get_skills_dir(), skill_name, "SKILL.md")
    if not os.path.exists(skill_md_path):
        raise HTTPException(status_code=404, detail="SKILL.md not found")

    with open(skill_md_path, "r", encoding="utf-8") as f:
        content = f.read()

    return {"name": skill_name, "content": content}


# ============ 首页 & 静态文件 ============

ASSETS_DIR = Path(__file__).parent / "assets"
ASSETS_DIR.mkdir(exist_ok=True)


@app.get("/")
def index():
    """Dashboard 首页"""
    index_path = ASSETS_DIR / "index.html"
    if index_path.exists():
        return FileResponse(str(index_path))
    return JSONResponse({"message": "Skill Manager SaaS API", "docs": "/docs", "dashboard": "index.html not found"})


if __name__ == "__main__":
    import uvicorn
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--host", default="0.0.0.0")
    args = parser.parse_args()

    print(f"""
╔══════════════════════════════════════════════╗
║   Skill Manager SaaS                        ║
║   启动地址: http://{args.host}:{args.port}             ║
║   API 文档: http://{args.host}:{args.port}/docs       ║
╚══════════════════════════════════════════════╝
    """)
    uvicorn.run(app, host=args.host, port=args.port, log_level="info")
