# gov-report-writing

> 国央企/党政机关公文与报告写作专用 WorkBuddy Skill

[![Version](https://img.shields.io/badge/version-1.1.0-blue)](https://github.com)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-WorkBuddy-orange)](https://www.codebuddy.cn)

## 简介

`gov-report-writing` 是一个专为国央企和党政机关公文写作场景设计的 WorkBuddy Skill。它内置了 GB/T 9704-2012 国标公文格式规范、8 种常用报告模板框架以及公文专用措辞词汇库，能够将一份标准公文从"调格式 + 写内容 + 润色"的 2 小时工作压缩到几分钟。

## 核心功能

| 功能 | 说明 |
|------|------|
| 📐 国标排版 | 严格遵循 GB/T 9704-2012，自动设置页边距、字体、字号、行距、层级标题格式 |
| 📋 8 种模板 | 年度总结 / 述职报告 / 党建报告 / 调研报告 / 工作方案 / 会议纪要 / 通知公告 / 汇报材料 |
| ✍️ 公文用语 | 内置政治术语校验、口语→公文替换规则、常用句式库 |
| 🔒 安全红线 | 执行前自动识别涉密信号，占位符机制保护敏感信息 |

## 安装

### 方式一：从 SkillHub 安装（推荐）

```bash
npx clawhub install gov-report-writing
```

### 方式二：手动安装

1. 下载 [gov-report-writing.zip](https://github.com/your-org/gov-report-writing/releases)
2. 解压到 WorkBuddy 技能目录：

```bash
# WorkBuddy
unzip gov-report-writing.zip -d ~/.workbuddy/skills/

# CodeBuddy
unzip gov-report-writing.zip -d ~/.codebuddy/skills/
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
gov-report-writing/
├── SKILL.md                          # 核心技能文件（三阶段工作流程）
├── LICENSE                           # MIT 开源许可证
├── README.md                         # 本文件
└── references/
    ├── gb-t9704-format.md            # GB/T 9704-2012 国标公文格式完整规范
    ├── report-templates.md           # 8 种常用报告模板框架与写作要点
    └── vocabulary-guide.md           # 公文专用词汇、政治术语、措辞规范
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

- 📝 补充更多报告模板（函、请示、批复等 15 种行政公文）
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
