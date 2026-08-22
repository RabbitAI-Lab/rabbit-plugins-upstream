# 公文写作（gongwen-writing）

> 国央企/党政机关公文与报告写作专用 WorkBuddy Skill

[![Version](https://img.shields.io/badge/version-1.4.0-blue)](https://github.com)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-WorkBuddy-orange)](https://www.codebuddy.cn)

> 🚀 已上线 ClawHub，即搜即装。在 WorkBuddy 技能市场搜索「公文写作」或「gongwen-writing」即可一键安装。

## 简介

`gongwen-writing`（中文名：公文写作）是一个专为国央企和党政机关公文写作场景设计的 WorkBuddy Skill。它内置了 GB/T 9704-2012 国标公文格式规范（含企业级扩展）、25+ 种模板框架（8 类工作模板 + 7 种行政公文 + 10 种专题模板 + 信函式文件）以及公文专用措辞词汇库，能够将一份标准公文从"调格式 + 写内容 + 润色"的 2 小时工作压缩到几分钟。

## 核心功能

| 功能 | 说明 |
|------|------|
| 📐 国标排版 | 严格遵循 GB/T 9704-2012，自动设置页边距、字体、字号、行距、层级标题格式 |
| 📋 25+ 种模板 | 8类工作模板 + 7种行政公文 + 10种专题模板（民主生活会/务虚会/党课/心得/述职述廉/组织生活会/表态发言/先进事迹/整改方案/巡视汇报） |
| ✍️ 公文用语 | 内置政治术语校验、口语→公文替换规则、常用句式库 |
| 🔒 安全红线 | 执行前自动识别敏感信号，占位符机制保护敏感信息 |

## 效果演示

> 📹 使用演示（点击播放）

![公文写作（gongwen-writing）使用演示](./assets/demo.gif)

*演示场景：在 WorkBuddy 中输入「帮我写一份年度工作总结」→ 自动识别报告类型 → 套用模板 → 按国标格式输出 Word 文档。全程约 30 秒。*

---

## 安装

### 方式一：从 SkillHub 安装（推荐）

```bash
npx clawhub install gongwen-writing
```

### 方式二：手动安装

1. 下载 [gongwen-writing.zip](https://github.com/Mogician11111/gov-report-writing/releases)
2. 解压到 WorkBuddy 技能目录：

```bash
# WorkBuddy
unzip gongwen-writing.zip -d ~/.workbuddy/skills/

# CodeBuddy
unzip gongwen-writing.zip -d ~/.codebuddy/skills/
```

3. 重启 WorkBuddy 或刷新技能列表

## 使用方法

在 WorkBuddy 中直接对话即可触发：

```
帮我写一份人力资源部 2025 年度工作总结，3000 字左右
```

```
按公文格式写个述职报告，侧重业务创新和团队建设
```

```
把这份会议录音转写稿整理成正式会议纪要
```

Skill 会自动识别报告类型 → 加载对应模板 → 按国标排版 → 输出 Word 文档。

## 目录结构

```
gongwen-writing/
├── SKILL.md                          # 核心技能文件（三阶段工作流程 + 错误处理机制）
├── LICENSE                           # MIT 开源许可证
├── README.md                         # 本文件
├── references/
│   ├── gb-t9704-format.md            # GB/T 9704-2012 国标格式规范（含信函/纪要/联合行文/企业扩展）
│   ├── report-templates.md           # 25+ 种报告模板框架与写作要点
│   ├── vocabulary-guide.md           # 公文词汇、政治术语、52 项表述检查清单
│   ├── ai-traces.md                  # AI 痕迹 12 类检测规则
│   ├── policy-database.md            # 常用政策文件速查库
│   └── polishing-guide.md            # 篇章级润色指南（语病/句式/过渡/数据一致性）
└── scripts/
    └── format_check.py               # 跨平台格式自动检查脚本（--json/--quiet）
```

## 支持的文档类型

| 文档类型 | 触发关键词 | 语气特点 |
|----------|-----------|----------|
| 年度工作总结 | 总结、年度、全年、回顾 | 务实、数据支撑、成绩与问题平衡 |
| 述职报告 | 述职、履职、述廉 | 第一人称、谦虚务实、体现反思 |
| 党建报告 | 党建、党委、支部、思想政治 | 庄重严肃、政治性强 |
| 调研报告 | 调研、课题、研究 | 客观理性、数据驱动 |
| 工作方案 | 方案、计划、安排、部署 | 明确具体、可操作、有时限 |
| 会议纪要 | 纪要、会议、决议 | 客观实录、不评论 |
| 通知公告 | 通知、公告、通报 | 简洁明了、一事一文 |
| 汇报材料 | 汇报、向上级 | 突出亮点、建议有针对性 |
| 函 | 商洽、询问、答复、函告 | 一事一函、平等对等 |
| 请示 | 请示、审批、申请 | 一事一请、缘由充分 |
| 批复 | 批复、批示 | 态度明确、针对请示 |
| 报告（行政） | 报送、答复、汇报 | 客观汇报、不夹带请示 |
| 议案 | 审议、提请 | 政府→人大、严格法定 |
| 决定 | 决定、奖惩、变更 | 权威果断 |
| 意见 | 意见、建议、处理办法 | 见解明确、多向灵活 |
| 民主生活会发言 | 民主生活会、对照检查、批评 | 诚恳具体、触及思想 |
| 务虚会发言 | 务虚会、思路、设想 | 思想碰撞、前瞻创新 |
| 党课讲稿 | 党课、讲稿、宣讲 | 理论通俗化、感染力 |
| 心得体会 | 心得体会、学习感受 | 真情实感、结合实际 |
| 述职述廉报告 | 述职述廉、述廉 | 述廉专章、如实报告 |
| 组织生活会对照检查 | 组织生活会、检视剖析 | 见人见事见思想 |
| 任前表态发言 | 表态、就职、任职 | 诚恳朴实、3-5分钟 |
| 先进事迹材料 | 先进事迹、榜样 | 事例驱动、细节说话 |
| 整改方案 | 整改方案、整改 | 表格化、责任到人 |
| 巡视汇报材料 | 巡视汇报、巡视 | 实事求是、数据支撑 |
| 信函式文件 | 信函、便函、函件 | 双线版式、平行对等 |

## 安全特性

- 执行前自动检测涉密信号（密级标注、项目代号、技术参数）
- 敏感信息自动用 `XX` 占位，防止泄露
- 全程本地处理，不上传云端
- 每份输出文档附带安全提示

## 技术要求

- **平台**：WorkBuddy / CodeBuddy (Cursor/Windsurf/Claude Code 兼容)
- **字体**（国标排版需要）：
  - 方正小标宋简体
  - 仿宋_GB2312
  - 楷体_GB2312
  - 黑体
  > 如系统缺少以上字体，Skill 会正常设置字体名并提醒用户安装。

## 贡献指南

欢迎提交 Issue 和 Pull Request！

### 贡献方式

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 创建 Pull Request

### 贡献方向

- 📝 补充更多报告模板（目前已覆盖 25+ 种）
- 🛠 增加格式检查脚本（`scripts/format_check.py`）
- 🎨 优化模板措辞和示例
- 🐛 修复格式规范错误

## 常见问题

**Q: 生成的文档字体不对？**
A: 请确认系统已安装仿宋_GB2312、楷体_GB2312 和方正小标宋简体。可从 Windows 字体库或 WPS 安装目录获取。

**Q: 能否处理涉密文件？**
A: 不能。本 Skill 内���安全检测机制，遇到涉密信号会自动拒绝处理。请将文档脱敏后再使用。

**Q: 支持 PDF 输出吗？**
A: 当前默认输出 Word (.docx)，可配合 WorkBuddy 的 PDF 转换功能导出为 PDF。

## 许可证

本项目采用 [MIT License](LICENSE)。

---

*Made with ❤️ for 体制内打工人*
