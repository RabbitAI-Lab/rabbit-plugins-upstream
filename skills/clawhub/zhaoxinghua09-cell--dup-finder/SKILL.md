---
name: dup-finder
description: 重复文件查找器 — 三级哈希（大小→首块→全量SHA1）找重复文件，默认只报告 --apply 删多余保留首个（零依赖） 适用场景：当需要重复文件查找器能力时使用本技能；触发词：dup-finder。
slug: dup-finder
version: 1.0.5
display_name: 重复文件查找器
display_name_en: Duplicate File Finder
agent_created: true
author: 诺声(Logos)@SynomosAI
license: MIT
license_scope: 代码（.py 文件）MIT；本 SKILL.md 与其中理论文本不在 MIT 覆盖范围内（见文末「License & attribution」）
allowed-tools: Read, Glob, Grep, Bash, Write, WebFetch
category: 效率工具
platforms: [claude, codex, cursor, windsurf, workbuddy]
copyright: SynomosAI
read_when:
  - 下载夹/相册堆了大量同名重复副本，想清理省空间
  - 要按三级哈希（大小→首块→全量SHA1）找真重复而非同名误判
  - 默认只报告、--apply 才删除多余保留首个
  - 用户说「找出重复文件」「删掉重复的照片/副本」
description_zh: "重复文件查找器 — 三级哈希（大小→首块→全量SHA1）找重复文件，默认只报告 --apply 删多余保留首个（零依赖）"
description_en: "Find duplicate files via three-level hashing (size, first block, full SHA1); report-only by default, --apply deletes extras keeping the first (zero-dependency)."
classification:
  skillhub: ["productivity"]
  iso_25010: ["Maintainability", "Usability"]
risk_tier: medium
risk_rationale: "门禁批量补丁默认 medium（按默认策略设计为中等风险）：调用 API/读写文件/本地执行，最小权限，密钥走 Secret；若实际涉对外代执行(push/发布/发送/上架)须人工复评，改 high 并走人工批准。"
tags: [dup-finder, 效率工具]
ai_protocol: true
spec: usk/1.0
interface:
  type: cli
  entry_point: scripts/dup_finder.py
  runtime: python3
  call_pattern: args
input_schema:
  args:
    type: string
    description: "命令行参数透传给主脚本，具体取值见各包 --help"
    required: false
output_schema:
  stdout:
    type: string
    description: "标准输出为 JSON 结果，含逐项检查与总体结论"
  exit_code:
    type: integer
    description: "0=PASS/完成；1=FAIL/有警告或待补强；2=用法或参数错误"
capabilities:
  - cli_tool
permissions:
  network: false
  filesystem: false
  subprocess: false
requirements:
  python_packages: []
  min_python: "3.8"
changelog: "1.0.5: Bilingual rewrite (full EN+ZH, English first); 1.0.0: initial upload (USK v3)"

---

> 凡自治之物 · LGD 治理学 · 创造术家族 ｜ 评测协议：见平台质量门禁规范

## English

### When to use
1. Disk cleanup: when you need to scan and sort out redundant files produced by backups or downloads in a local directory.
2. Deduplication management: finding content-duplicated-but-undeleted files in large project storage (e.g. image libraries, log archives).
3. Automated ops: scheduled runs of a config script, using the default report mode to check for redundancy.

### Usage
1. The core script is `dup_finder.py`; run it with a Python interpreter on the PATH.
2. Key parameters: `-r` scans the target folder recursively; `--apply` automatically deletes the extras and keeps the first copy.
3. Example: `python3 dup_finder.py -r -d /path/to/dir --apply`.

### Workflow
1. Confirm the target folder path and make sure you have the needed filesystem permissions.
2. Run the scan command, triggering the three-level comparison: size → first-block hash → full SHA1.
3. Check the terminal output; confirm the duplicate groups and which first copy is kept.
4. To auto-clean, make sure the `--apply` flag is present in the parameters so the deletion instruction executes.
5. Re-scan the target path after the run to verify that the extra copies are gone and no errors occurred.

### Evidence & safety statement
- Evidence: TBD (no evaluation / badge link yet; update here once it is produced)
- Version: 1.0.5
- Security: no independent security scan has been performed (TBD); the conclusion is pending and no endorsement is given until it is completed.

## 中文

### 何时用
1. 磁盘空间清理：当需要扫描并整理本地目录中因备份或下载产生的冗余文件时。
2. 文件去重管理：在大型项目存储（如图片、日志库）中发现内容重复但未删除的文件。
3. 自动化运维场景：用于配置脚本定期运行，利用默认报告机制检查冗余情况。

### 用法
1. 核心脚本为 `dup_finder.py`，需使用 Python 解释器或包含在环境路径中执行。
2. 关键参数含 `-r` 表示递归扫描目标文件夹，及 `--apply` 用于自动删除多余文件保留首个。
3. 调用示例：`python3 dup_finder.py -r -d /path/to/dir --apply`。

### 流程
1. 确定目标文件夹路径并确保具备相应的文件系统操作权限。
2. 执行扫描命令，触发大小、首块哈希及全量 SHA1 的三级比对逻辑。
3. 检查终端输出结果，确认重复文件分组及保留的首个文件位置。
4. 若需自动清理，可确保脚本参数中包含 `--apply` 标志执行删除指令。
5. 运行后再次扫描目标路径以验证多余副本是否已移除且无异常错误。

### 证据与安全声明
- 证据：TBD（暂无评测/徽章链接；产生后在此更新实际链接）
- 版本：1.0.5
- 安全：未做独立安全扫描（TBD），结论待补；补全前不作推荐背书。
