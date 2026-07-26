#!/usr/bin/env python3
"""
Version Manager — 类Git版本管理与迭代追踪
支持版本快照、Diff对比、回滚、版本树可视化
"""

import json
import os
import sys
import difflib
import hashlib
from datetime import datetime, timezone, timedelta
from pathlib import Path
from dataclasses import dataclass, field, asdict
from typing import Optional

# 中国时区
CST = timezone(timedelta(hours=8))


@dataclass
class VersionRecord:
    """版本记录"""
    version: str
    timestamp: str
    parent: str
    changes: list[dict] = field(default_factory=list)
    score: Optional[float] = None
    score_change: Optional[float] = None
    snapshot_path: str = ""
    checksum: str = ""


class VersionManager:
    """版本管理器"""

    def __init__(self, work_dir: str, project_name: str = "tender"):
        self.work_dir = Path(work_dir)
        self.project_name = project_name
        self.versions_dir = self.work_dir / ".tender_versions"
        self.index_path = self.versions_dir / "version_index.json"

    def init(self) -> dict:
        """初始化版本仓库"""
        self.versions_dir.mkdir(parents=True, exist_ok=True)
        if not self.index_path.exists():
            self._save_index({
                "project": self.project_name,
                "created": datetime.now(CST).isoformat(),
                "current_version": "v1.0",
                "versions": [],
            })
            return {"status": "initialized", "version": "v1.0"}
        return {"status": "already_initialized"}

    def snapshot(self, content: str, version: str = None, changes: list[dict] = None,
                 score: float = None, previous_score: float = None) -> dict:
        """
        创建版本快照

        Args:
            content: 当前标书内容
            version: 版本号(自动计算如果不提供)
            changes: 变更描述列表
            score: 当前评分
            previous_score: 上一版本评分
        """
        self.init()
        index = self._load_index()

        # 自动计算版本号
        if version is None:
            latest = self._latest_version(index)
            version = self._bump_version(latest, changes or [])

        # 生成快照文件
        timestamp_str = datetime.now(CST).strftime("%Y%m%d_%H%M%S")
        snapshot_name = f"{self.project_name}_{version}_{timestamp_str}.md"
        snapshot_path = self.versions_dir / snapshot_name

        with open(snapshot_path, "w", encoding="utf-8") as f:
            f.write(content)

        # 计算checksum
        checksum = hashlib.sha256(content.encode()).hexdigest()[:12]

        # 创建版本记录
        parent = self._latest_version(index) if index["versions"] else "root"
        score_change = None
        if score is not None and previous_score is not None:
            score_change = round(score - previous_score, 1)

        record = VersionRecord(
            version=version,
            timestamp=datetime.now(CST).isoformat(),
            parent=parent,
            changes=changes or [],
            score=score,
            score_change=score_change,
            snapshot_path=str(snapshot_path),
            checksum=checksum,
        )

        index["versions"].append(asdict(record))
        index["current_version"] = version
        self._save_index(index)

        return asdict(record)

    def history(self) -> list[dict]:
        """获取版本历史"""
        self.init()
        index = self._load_index()
        return index["versions"]

    def diff(self, version1: str, version2: str = None) -> str:
        """
        对比两个版本的差异

        Args:
            version1: 版本号1
            version2: 版本号2(默认为current)
        """
        index = self._load_index()
        v1_content = self._get_version_content(index, version1)
        v2_content = self._get_version_content(index, version2)

        if v1_content is None or v2_content is None:
            return "Error: Version not found"

        diff_lines = list(difflib.unified_diff(
            v1_content.splitlines(keepends=True),
            v2_content.splitlines(keepends=True),
            fromfile=version1,
            tofile=version2 or "current",
            lineterm="",
        ))

        return "".join(diff_lines)

    def rollback(self, target_version: str) -> dict:
        """回滚到指定版本"""
        index = self._load_index()
        content = self._get_version_content(index, target_version)
        if content is None:
            return {"error": f"Version {target_version} not found"}

        # 创建回滚快照
        return self.snapshot(
            content=content,
            version=None,  # auto bump
            changes=[{"type": "回滚", "source": f"回滚至{target_version}"}],
        )

    def _latest_version(self, index: dict) -> Optional[str]:
        """获取最新版本号"""
        versions = index.get("versions", [])
        if not versions:
            return None
        return versions[-1]["version"]

    def _bump_version(self, latest: Optional[str], changes: list[dict]) -> str:
        """自动计算版本号"""
        if latest is None:
            return "v1.0"

        try:
            parts = latest.lstrip("v").split(".")
            major, minor = int(parts[0]), int(parts[1])

            # 是否包含结构性变化的变更
            has_major_change = any(
                c.get("type") in ("结构变更", "章节增删") for c in changes
            )

            if has_major_change:
                return f"v{major + 1}.0"
            else:
                return f"v{major}.{minor + 1}"
        except (ValueError, IndexError):
            return "v1.0"

    def _get_version_content(self, index: dict, version: str) -> Optional[str]:
        """读取指定版本的内容"""
        for v in index.get("versions", []):
            if v["version"] == version or (version is None and v == index["versions"][-1]):
                snapshot_path = v.get("snapshot_path", "")
                if snapshot_path and os.path.exists(snapshot_path):
                    with open(snapshot_path, "r", encoding="utf-8") as f:
                        return f.read()
        return None

    def _load_index(self) -> dict:
        """加载版本索引"""
        if self.index_path.exists():
            with open(self.index_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return {"project": self.project_name, "versions": [], "current_version": "v1.0"}

    def _save_index(self, index: dict):
        """保存版本索引"""
        with open(self.index_path, "w", encoding="utf-8") as f:
            json.dump(index, f, ensure_ascii=False, indent=2)

    def version_tree(self) -> str:
        """生成版本树文本表示"""
        index = self._load_index()
        versions = index.get("versions", [])
        if not versions:
            return "暂无版本记录"

        lines = ["# 版本演化树", ""]
        for v in versions:
            score_str = f" | 评分: {v['score']}" if v.get("score") else ""
            change_str = f" | 变更: +{v['score_change']}分" if v.get("score_change") is not None else ""
            lines.append(f"- {v['version']} ({v['timestamp'][:16]}){score_str}{change_str}")
            for ch in v.get("changes", []):
                items = ch.get("items", [])
                if isinstance(items, list):
                    for item in items:
                        lines.append(f"    - {item}")
                else:
                    lines.append(f"    - {ch.get('source', '')}")

        return "\n".join(lines)


def main():
    """CLI入口"""
    import argparse
    parser = argparse.ArgumentParser(description="Version Manager for Tender Documents")
    subparsers = parser.add_subparsers(dest="command")

    # init
    subparsers.add_parser("init", help="Initialize version repository")

    # snapshot
    snap_parser = subparsers.add_parser("snapshot", help="Create version snapshot")
    snap_parser.add_argument("content_file", help="Path to current tender content file")
    snap_parser.add_argument("--score", type=float, help="Current score")
    snap_parser.add_argument("--prev-score", type=float, help="Previous score")

    # history
    subparsers.add_parser("history", help="Show version history")

    # diff
    diff_parser = subparsers.add_parser("diff", help="Show diff between versions")
    diff_parser.add_argument("version1", help="First version")
    diff_parser.add_argument("version2", nargs="?", help="Second version (default: current)")

    # rollback
    rollback_parser = subparsers.add_parser("rollback", help="Rollback to version")
    rollback_parser.add_argument("version", help="Target version")

    # tree
    subparsers.add_parser("tree", help="Show version tree")

    args = parser.parse_args()
    vm = VersionManager(os.getcwd())

    if args.command == "init":
        print(json.dumps(vm.init(), ensure_ascii=False, indent=2))

    elif args.command == "snapshot":
        with open(args.content_file, "r", encoding="utf-8") as f:
            content = f.read()
        result = vm.snapshot(content, score=args.score, previous_score=args.prev_score)
        print(json.dumps(result, ensure_ascii=False, indent=2))

    elif args.command == "history":
        print(json.dumps(vm.history(), ensure_ascii=False, indent=2))

    elif args.command == "diff":
        diff_output = vm.diff(args.version1, args.version2)
        print(diff_output)

    elif args.command == "rollback":
        result = vm.rollback(args.version)
        print(json.dumps(result, ensure_ascii=False, indent=2))

    elif args.command == "tree":
        print(vm.version_tree())

    else:
        # Demo mode
        print("=== Version Manager Demo ===\n")
        vm = VersionManager(os.getcwd(), "demo_project")
        vm.init()

        v1 = vm.snapshot("# 投标方案 v1.0\n\n## 技术方案\n初始版本...", score=72.3)
        print(f"创建 {v1['version']}: 评分 {v1['score']}")

        v2 = vm.snapshot("# 投标方案 v1.1\n\n## 技术方案\n增强后的方案...", score=78.5, previous_score=72.3)
        print(f"创建 {v2['version']}: 评分 {v2['score']} (+{v2['score_change']})")

        print("\n版本树:")
        print(vm.version_tree())


if __name__ == "__main__":
    main()
