🌐 **中文** · [繁體中文](README.zh-Hant.md) · [English](README.en.md) · [Français](README.fr.md) · [Español](README.es.md) · [العربية](README.ar.md) · [日本語](README.ja.md) · [Русский](README.ru.md)

<p align="center"><img src="logo.png" alt="Hui Ning IP" width="150"></p>

# Hague Design System · 海牙体系外观设计国际注册实务技能

> *「一句话问清程序，拿回一份能直接用的海牙外观设计实务方案。」*
> *"Ask once. Get a filing-ready Hague design practice answer."*

[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.10.8-blue.svg)](references/changelog.md)
![Agent-Agnostic](https://img.shields.io/badge/Agent-Agnostic-blueviolet)
[![Hague Members](https://img.shields.io/badge/Hague%20Members-83-green)](https://www.wipo.int/en/web/hague-system)
![No-Fabrication](https://img.shields.io/badge/Principle-No--Fabrication-orange)

**一个面向全球外观设计代理师、知识产权律师与企业法务的海牙体系外观设计国际注册全流程实务技能（以 WIPO 国际阶段为主体、各缔约方通用，含可选的中国衔接专章）。**

不是科普问答，而是：提交与审查节点的检查路径、逐条可核的法源依据（协定／细则／行政规程／指南）、视图·单一性·优先权等技术要件的硬指标、费用与期限的可复核参数（含内置费用计算脚本）。

技能遵循通用 Agent Skills 格式（`/SKILL.md`），支持 skills 的 agent 均可使用。

[能做什么](#能做什么) · [装上就能用](#装上就能用) · [核心机制](#核心机制) · [仓库结构](#仓库结构) · [能力边界](#能力边界)

---

## 装上就能用

### 方式一：同步脚本（推荐）

```bash
# Windows
py -3 scripts/sync_to_local.py

# macOS / Linux
python3 scripts/sync_to_local.py

# 常用参数
py -3 scripts/sync_to_local.py --dry-run        # 预演，不写入
py -3 scripts/sync_to_local.py --target D:/path/to/skills   # 指定技能目录
```

脚本把本仓库作为单个技能单向同步到本机技能目录（默认 `~/.workbuddy/skills`，安装为 `hague-design-system/`）：新增/变更文件覆盖写入、陈旧文件清除，**本机元数据（`_user_meta.json` 等）自动保留**；仓库级文件（README、LICENSE、logo 等）不会装入技能目录。

### 方式二：手动复制

把整个仓库文件夹复制到你的技能目录（如 `~/.workbuddy/skills/`）并重命名为 `hague-design-system`，然后重启或重载应用。

> ⚠️ 这是多文件技能：`references/` 下的知识库（协定与实施细则、行政规程、海牙体系指南、可选中国专章等）由 `SKILL.md` 以 `@` 相对路径引用，**缺一即断链**——请整目录复制，勿只取 `SKILL.md`。

## 能做什么

| 域 | 说明 |
|------|------|
| 国际申请 | 提交资格；DM/1 与 eHague 提交；视图技术要求；单一性；优先权；提交路径与程序节点 |
| 注册与公布 | 形式审查与更正；国际注册与注册日；公布与延迟公布；撤回 |
| 审查与救济 | 指定局驳回应对；给予保护与生效差异；无效宣告；驳回/无效后的后续路径 |
| 续展与变更 | 保护期与续展（含宽限期）；所有权变更、名称地址变更、代理人、限制、放弃 |
| 费用 | 七类业务费用模式（申请／续展／所有权变更／注册人数据变更／设计人名称地址变更／限制／放弃）；海牙费用计算器；CHF 规费构成；内置费用计算脚本 |
| 检索 | DesignDB 在先设计与法律状态检索 |
| 可选｜中国专章 | 中国声明事项；CNIPA 审查与驳回救济；转交与系统操作；分案；CNY 口径（非中国从业者可整体跳过） |

## 核心机制

1. **全球通用主体**：以 WIPO 国际阶段程序（各缔约方通用）为主线；中国（CNIPA）衔接为可选专章，非中国从业者可整体跳过；
2. **法源与数据单点维护**：费用、声明等易变数据收敛到唯一权威源，版本历史与文件索引集中治理（`changelog.md`、`11-file-index.md`），避免多处口径漂移；
3. **渐进式披露**：大部头原文（含 286 KB 的《海牙体系指南》）放在 `references/`，按需加载并配行号索引，不撑上下文；
4. **查不到就回「无」**：无把握的信息直接标注，不编造条款、期限与费用数字；交付答复不使用 Markdown 表格（以清单与行内定义呈现）。

## 仓库结构

```text
HAGUE-SKILLS/                        # 仓库根目录 = 技能根目录（单技能仓库）
├── SKILL.md                         # 控制面：角色／任务／上下文／流程／规则／输出格式
├── references/                      # 12 份知识库（含可选中国专章、版本记录与文件索引）
├── scripts/                         # 技能脚本（费用计算、抓取助手）＋ sync_to_local.py（一键同步脚本）
├── README.md                        # 简体中文（本文件 · 默认）
├── README.zh-Hant.md                # 繁體中文
├── README.en.md                     # English
├── README.fr.md                     # Français
├── README.es.md                     # Español
├── README.ar.md                     # العربية（RTL）
├── README.ja.md                     # 日本語
├── README.ru.md                     # Русский
├── LICENSE                          # MIT 许可证
└── logo.png                         # 品牌标识（README 首屏）
```

- 仓库根目录即技能根目录；安装后为严格的 **2 级结构**（`SKILL.md` / `references/` / `scripts/`），符合 WorkBuddy 官方技能结构规范；
- 仓库级文件（`README*.md`、`LICENSE`、`logo.png`、`scripts/sync_to_local.py`）不会被安装到技能目录；
- 技能文件约定：**CRLF、UTF-8 无 BOM**。

## 数据与时效

- 法源以 **WIPO / CNIPA 官方现行版本**为准，技能内标注数据基准日与建议复核周期（§3.0 时效清单）；
- 易变数据（费用、单独指定费、缔约方声明、汇率）请以官方最新公告／费用计算器复核后再用于案卷；
- 输出为实务参考，**不构成法律意见**。

## 能力边界

- 不替代官方与个案判断：期限、费用与程序结论以指定局通知与官方公告为准；
- 不做编造：查不到的数据直接回「无」；
- 法源聚焦海牙体系程序与共同规则层面；各指定缔约方本国实体法与审查实务以其官方口径为准。

## License

[MIT](LICENSE) © 2026 辉宁知识产权（Hui Ning IP）。

- 技能自身内容（`SKILL.md`、`references/` 内的整理与注释）适用 MIT；
- `references/` 中收录／转引的 WIPO 官方文本（协定、实施细则、行政规程、指南等）版权归 WIPO 所有，不受本协议覆盖。

## 联系

- 问题与建议：欢迎在仓库提 Issue；
- 由 辉宁知识产权（中国专利代理师团队）构建与维护。
