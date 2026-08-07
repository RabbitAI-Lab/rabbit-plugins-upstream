---
name: MC Ecosystem Adaptation Engineer
name_zh: MC全生态智能适配工程师
slug: mc-ecosystem-adapt-engineer
version: 1.0.1
description: One-stop Minecraft mod ecosystem intelligent management tool with 10+ features including mod search, environment setup, Mixin conflict scanning, crash fix, translation, migration assessment, and intelligent multi-language support (11 languages with auto-detection via IP geolocation)
description_zh: Minecraft 模组全生态智能适配工具，支持模组检索、环境搭建、Mixin冲突扫描、崩溃修复、汉化、移植评估等10大功能，新增智能多语言支持（11种语言，IP定位自动切换）
author: Liang030214
homepage: https://github.com/Liang030214/mc-skill-v1
icon: assets/icon-market.jpg
icon_local: assets/icon-local.jpg
tags:
  - minecraft
  - mod
  - forge
  - fabric
  - neoforge
  - quilt
  - mixin
  - translation
  - crash-fix
  - migration
  - chinese
  - i18n
  - multilingual
category: games
license: MIT
language: en
languages_supported: ["en", "zh", "ja", "ko", "ru", "es", "it", "el", "th", "hi"]
min_agent_version: "1.0.0"
---

# MC Ecosystem Adaptation Engineer

One-stop Minecraft mod environment intelligent management tool.

# MC 全生态智能适配工程师

一站式 Minecraft 模组环境智能管理工具。

## Feature List

| # | Feature | Description |
|---|---------|-------------|
| F1 | JAR Structure Parser | Parse mod JAR metadata (mcmod.info, fabric.mod.json, mods.toml) |
| F2 | Mod Search & Download | Search and download mods from Modrinth with version and loader filters |
| F3 | Environment Setup Guide | Intelligently recommend MC version and loader combinations |
| F4 | Mixin Conflict Scanner | Detect Mixin injection conflicts between multiple mods |
| F5 | Resource Repacker | Repack and optimize mod resource files |
| F6 | Save Sync | Backup and restore game saves |
| F7 | Base Translation | Translate mods to target languages (Chinese, English, Japanese, Korean, etc.) |
| F8 | Crash Fix | Intelligently analyze crash logs and provide fix suggestions |
| F8.1 | Auto Fix | One-click mod upgrade to resolve crash issues |
| F9 | Migration Feasibility Assessment | Assess feasibility of cross-version/cross-loader migration |

## 功能列表

| # | 功能 | 说明 |
|---|------|------|
| F1 | JAR结构解析 | 解析模组 JAR 文件元数据（mcmod.info、fabric.mod.json、mods.toml） |
| F2 | 模组检索下载 | 从 Modrinth 搜索下载模组，支持版本和加载器筛选 |
| F3 | 环境引导搭建 | 智能推荐 MC 版本和加载器组合 |
| F4 | Mixin 冲突扫描 | 检测多个模组间的 Mixin 注入冲突 |
| F5 | 资源重打包 | 模组资源文件重打包优化 |
| F6 | 存档同步 | 存档备份与恢复 |
| F7 | 多语言翻译 | 模组目标语言翻译（中文、英文、日文、韩文等） |
| F8 | 报错修复 | 智能分析崩溃日志，给出修复建议 |
| F8.1 | 自动修复 | 一键升级模组修复崩溃问题 |
| F9 | 移植可行性评估 | 评估模组跨版本/跨加载器迁移可行性 |

## Usage

### Method 1: Direct Command Line

```bash
# Parse mod JAR
python main.py --feature jar_parser --jar-path "create.jar"

# Search mods
python main.py --feature mod_searcher --query "Create" --mc-version "1.21.1" --loader "neoforge"

# Scan Mixin conflicts
python main.py --feature mixin_scanner --mods-dir "./mods"

# Analyze crash log
python main.py --feature crash_analyzer --crash-log "crash-2024-01-01.txt"

# Assess migration feasibility
python main.py --feature migration_assess --jar-path "create.jar" --from-mc-version "1.20.1" --to-mc-version "1.21.1" --from-loader "forge" --to-loader "neoforge"
```

### Method 2: Interactive Menu

```bash
python main.py
# or
python mc-skill-start.bat
```

### Method 3: Agent AI Invocation

Agents can invoke each feature through the wrapper scripts in the scripts directory, returning JSON-format results.

## 使用方式

### 方式1：命令行直接运行

```bash
# 解析模组 JAR
python main.py --feature jar_parser --jar-path "create.jar"

# 搜索模组
python main.py --feature mod_searcher --query "Create" --mc-version "1.21.1" --loader "neoforge"

# 扫描 Mixin 冲突
python main.py --feature mixin_scanner --mods-dir "./mods"

# 分析崩溃日志
python main.py --feature crash_analyzer --crash-log "crash-2024-01-01.txt"

# 评估模组移植可行性
python main.py --feature migration_assess --jar-path "create.jar" --from-mc-version "1.20.1" --to-mc-version "1.21.1" --from-loader "forge" --to-loader "neoforge"
```

### 方式2：交互式菜单

```bash
python main.py
# 或
python mc-skill-start.bat
```

### 方式3：Agent AI 调用

Agent 可通过 scripts 目录下的封装脚本调用各功能，返回 JSON 格式结果。

## Supported Loaders

- Forge
- NeoForge
- Fabric
- Quilt

## 支持的加载器

- Forge
- NeoForge
- Fabric
- Quilt

## Supported MC Versions

- 1.16.5 ~ 1.21.x

## 支持的 MC 版本

- 1.16.5 ~ 1.21.x

## Language Support

This skill supports 11 languages with automatic detection:

| Code | Language | Auto-Detect |
|------|----------|-------------|
| en | English | ✅ |
| zh | 中文 (Chinese) | ✅ |
| ja | 日本語 (Japanese) | ✅ |
| ko | 한국어 (Korean) | ✅ |
| ru | Русский (Russian) | ✅ |
| es | Español (Spanish) | ✅ |
| it | Italiano (Italian) | ✅ |
| el | Ελληνικά (Greek) | ✅ |
| th | ไทย (Thai) | ✅ |
| hi | हिन्दी (Hindi) | ✅ |

**Auto-Detection Strategy:**
- The skill automatically detects the user's language from the conversation context and responds in the preferred language.
- Users can also manually specify the language via the `--lang` parameter when calling commands.
- Translation (F7) supports bidirectional conversion between any two supported languages.

## 语言支持

本 Skill 支持 11 种语言，并具备自动检测能力：

| 代码 | 语言 | 自动检测 |
|------|------|----------|
| en | English (英语) | ✅ |
| zh | 中文 | ✅ |
| ja | 日本語 | ✅ |
| ko | 한국어 | ✅ |
| ru | Русский (俄语) | ✅ |
| es | Español (西班牙语) | ✅ |
| it | Italiano (意大利语) | ✅ |
| el | Ελληνικά (希腊语) | ✅ |
| th | ไทย (泰语) | ✅ |
| hi | हिन्दी (印地语) | ✅ |

**自动检测策略：**
- Skill 会根据对话上下文自动检测用户语言，并以用户偏好的语言回复。
- 用户也可在调用命令时通过 `--lang` 参数手动指定语言。
- 翻译功能（F7）支持任意两种语言之间的双向互译。

## Runtime Environment

- Python 3.10+
- Windows / macOS / Linux
- Network connection (required for mod search feature)
- UTF-8 compatible terminal for multilingual support
- For full i18n functionality, ensure the system locale supports Unicode (UTF-8)

## 运行环境

- Python 3.10+
- Windows / macOS / Linux
- 网络连接（模组搜索功能需要）
- 兼容 UTF-8 的终端以支持多语言显示
- 完整国际化功能需要系统区域设置支持 Unicode（UTF-8）

## License

MIT License

## 许可证

MIT License