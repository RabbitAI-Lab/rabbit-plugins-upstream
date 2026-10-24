---
name: batch-renamer
description: 批量重命名器 — 规则式批量重命名：前缀/后缀/序号/查找替换/扩展名过滤，默认预览 --apply 才执行（零依赖） 适用场景：当需要批量重命名器能力时使用本技能；触发词：batch-renamer。
slug: batch-renamer
title: batch-renamer
version: 1.0.1
display_name: 批量重命名器
display_name_en: Batch File Renamer
agent_created: true
author: 诺声(Logos)@SynomosAI
license: MIT
license_scope: 代码（.py 文件）MIT；本 SKILL.md 与其中理论文本不在 MIT 覆盖范围内（见文末「License & attribution」）
allowed-tools: Read, Glob, Grep, Bash, Write
category: 效率工具
platforms: [claude, codex, cursor, windsurf, cli]
copyright: SynomosAI
description_zh: "批量重命名器 — 规则式批量重命名：前缀/后缀/序号/查找替换/扩展名过滤，默认预览 --apply 才执行（零依赖）"
description_en: "Rule-based batch file renaming: prefix/suffix/numbering/find-replace/extension filter; preview by default, --apply to execute (zero-dependency)."
read_when:
  - 统一整理下载/归档文件，去除杂乱命名
  - 科研/工程数据批量加项目代码、日期后缀、自动序号
  - 按扩展名过滤（如仅图片/文档）做规则化改名
classification:
  skillhub: ["productivity"]
  iso_25010: ["Maintainability", "Usability"]
risk_tier: medium
risk_rationale: "门禁批量补丁默认 medium：调用 API/读写文件/本地执行，最小权限，密钥走 Secret；若实际涉对外代执行(push/发布/发送/上架)须人工复评，改 high。"
tags: [batch-renamer, 效率工具]
ai_protocol: true
spec: usk/1.0
interface:
  type: cli
  entry_point: scripts/batch_renamer.py
  runtime: python3
  call_pattern: args
input_schema:
  - name: dir
    type: string
    description: 目标目录
    required: true
  - name: prefix
    type: string
    description: 前缀
    required: false
  - name: suffix
    type: string
    description: 后缀
    required: false
  - name: replace
    type: string
    description: 查找替换 旧|新
    required: false
  - name: start
    type: int
    description: 序号起始编号
    required: false
  - name: ext
    type: string
    description: 扩展名过滤如 .jpg
    required: false
  - name: apply
    type: bool
    description: 执行（缺省只预览）
    required: false
  - name: json
    type: bool
    description: JSON 输出
    required: false
output_schema:
  stdout: 预览清单或执行报告
  exit_code:
    type: integer
    description: "0=OK/PASS; 1=findings/warnings; 2=usage or argument error"
capabilities:
  - batch_rename
  - file_ops
  - productivity
permissions:
  network: false
  filesystem: false
  subprocess: false
requirements:
  python_packages: []
  min_python: "3.8"
changelog: "1.0.1: Bilingual rewrite (full EN+ZH, English first); 1.0.0: initial upload (USK v3)"
---

> 凡自治之物 · LGD 治理学 · 创造术家族 ｜ 评测协议：skill-quality-gate（外部公开评测门禁文档）

## English

### When to use
- **Standardize**: tidy downloaded files with messy names into one consistent format.
- **Custom marks**: bulk-add project code, date suffix and auto-numbering to research/engineering data.
- **Filter**: clean a folder by rule-modifying only specific extensions (images or docs).

### Usage
- Main script: `python batch_renamer.py`.
- Key params: prefix/suffix strings; find-replace rule for wildcard text; extension whitelist.
- Execution control: preview-only by default; `--apply` actually renames.

### Flow
1. Load the target directory; auto-scan all files/subfiles.
2. Virtually compute new names per prefix/suffix/replace rules.
3. Confirm the filtered extension list covers the intended types.
4. Print the rename preview list; wait for human confirmation.
5. On approval, apply `--apply` to actually rename files.
6. Emit an execution report; list final names and changes.

### Evidence & safety
- Evidence: TBD. Version: 1.0.1. Security: no independent scan (TBD).

## 中文

### 何时用
- **场景标准化**：当需要统一整理下载后的文件列表，去除原有杂乱命名格式时。
- **定制标识**：针对科研或工程数据，批量添加项目代码、日期后缀及自动序号。
- **筛选过滤**：在清理文件夹时，仅对特定类型扩展名（如图片或文档）进行规则修改。

### 用法
- **主入口脚本**：使用 `python batch_renamer.py` 启动执行环境。
- **关键参数配置**：支持通过命令行传递前缀/后缀字符串参数；可指定查找替换规则；提供扩展名白名单过滤选项。
- **执行控制**：脚本默认进入仅展示预览模式，避免误操作，添加 `--apply` 参数后才会真正覆盖原文件并生成重命名结果。

### 流程
1. 加载目标目录路径，系统自动扫描文件夹内的所有子文件或主文件。
2. 根据预设的前缀、后缀或替换规则进行虚拟文件名计算与校验。
3. 确认过滤后的扩展名列表是否包含需要处理的文件类型。
4. 在控制台输出重命名预览清单，等待用户人工确认无误。
5. 若通过验证，系统应用 `--apply` 指令完成实际文件的名称变更操作。
6. 任务结束并生成执行报告，提示用户查看最终文件列表与修改记录。

### 证据与安全声明
- 证据：TBD（暂无评测/徽章链接；产生后在此更新实际链接）
- 版本：1.0.1
- 安全：未做独立安全扫描（TBD），结论待补；补全前不作推荐背书。
