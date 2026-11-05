"""知识库扫描范围限定（policy）—— 单一事实来源

背景（2026-11-05 实测事故）：
  一个 OCR 影子副本树（knowledge/知识库/，863 份 .md）被整体放进 knowledge/，
  导致 249 份「原件早已分析过的影子」重新入队 → 同一文档被分析两遍。
  该目录是 hermes pathmove 误放到 knowledge/ 下的（应在外层 knowledgehub/），已删除。

设计要点（v1.4.12 简化版）：
  1. **扫描范围 = 目录白名单，且在 glob 层限定**（不是扫完再过滤）。
     → 新增任何文件夹都**不会**进入分析范围，这是结构性保证，不靠过滤兜底。
     → 白名单与 AGENTS.md 声明的 knowledge/ 合法结构一一对应。
  2. **不做扩展名白名单** —— glob patterns 本身只匹配 10 种文档扩展名，重复限定是冗余。
  3. **不做体积上限** —— 实测 50MB 上限会误伤 17 份真实业务文件（研报/施工手册/PPT）。
  4. **不做影子兜底** —— knowledgehub/ 是另一套独立功能，与本 skill 无关联，不做耦合。
  5. 仅保留垃圾文件排除（.DS_Store / Office 锁文件 ~$），它们会被 glob 误匹配。

规则只在这里改一处。调用方（run_analysis.py / generate_catalog.py）不再各自实现扫描逻辑。
"""

import glob
import os

# ── 允许扫描的一级目录白名单（= AGENTS.md 声明的 knowledge/ 合法结构）────
SCAN_TOP_DIRS = (
    "Macro Financials",   # 投行研报
    "工程效能专家",        # 工程类知识
    "房产效能专家",        # 房产类知识
    "合同对比",            # 合同模板
    "文章目录",            # 文章索引
    "知识库搭建手册",      # 元知识（怎么搭KB）
    "临时",                # 临时参考
    "temp_docs",           # 待分析投递区
)

# ── 可被 glob 误匹配的垃圾文件 ────────────────────────────────────────
JUNK_NAMES = (".DS_Store", "Thumbs.db", "desktop.ini")
JUNK_PREFIXES = ("~$", ".~")   # Office/WPS 锁文件

# ── 文档扩展名（glob patterns）────────────────────────────────────────
DOC_PATTERNS = (
    "**/*.pdf", "**/*.doc", "**/*.docx",
    "**/*.xls", "**/*.xlsx", "**/*.ppt", "**/*.pptx",
    "**/*.md", "**/*.csv", "**/*.txt",
)


def scan_roots(knowledge_dir):
    """返回允许扫描的一级目录绝对路径列表（只存在的）。"""
    return [
        os.path.join(knowledge_dir, d)
        for d in SCAN_TOP_DIRS
        if os.path.isdir(os.path.join(knowledge_dir, d))
    ]


def is_junk(filename):
    """是否为垃圾/临时文件。"""
    if filename in JUNK_NAMES:
        return True
    return filename.startswith(JUNK_PREFIXES)


def scan_files(knowledge_dir):
    """扫描允许进入分析的文件 —— 唯一入口。

    扫描范围在 glob 层按目录白名单限定：白名单外的目录（含 .analysis/.trash/
    .interpret/.storage 以及任何未来新增的文件夹）根本不会被遍历。
    """
    files = []
    seen = set()
    for root in scan_roots(knowledge_dir):
        for pattern in DOC_PATTERNS:
            for f in glob.glob(os.path.join(root, pattern), recursive=True):
                if f in seen:
                    continue
                if is_junk(os.path.basename(f)):
                    continue
                seen.add(f)
                files.append(f)
    return files
