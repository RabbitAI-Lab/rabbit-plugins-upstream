# Resume Creator

> **[English](./README.md)** | **简体中文**

基于已核实事实，生成 Reactive Resume JSON 或可离线打开的单文件 HTML 简历。

[![许可证：MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Reactive Resume](https://img.shields.io/badge/Reactive%20Resume-compatible-1558d6.svg)](https://rxresu.me/)
[![Agent Skill](https://img.shields.io/badge/Agent-Skill-orange.svg)](./SKILL.md)

---

## 能做什么

**Resume Creator** 可将经过核实的简历事实生成：可导入
[Reactive Resume](https://rxresu.me/) 的 JSON、可直接双击打开的单文件 HTML
简历，或两者兼有。不会编造工作经历、日期、量化数据、教育背景、链接或资质。

```text
“根据这份 Markdown 制作双语 HTML 简历。”
→ 询问输出、语言与视觉路径
→ 生成一份含内联 CSS、响应式与打印样式的 .html 文件
```

## 为什么使用

| | 没有本技能 | 使用 Resume Creator |
|---|---|---|
| 事实边界 | 润色时可能偏离原始材料 | 只使用用户提供或明确批准的事实 |
| 交付物 | 页面可能依赖构建或外部资源 | 单文件离线 HTML 或可导入 JSON |
| 视觉选择 | 可能被静默套用某个风格 | 从 15 个视觉改编或 3 种原生 HTML 风格中明确选择 |
| 发布验证 | 误把本地预览当作公网可用 | 分别核验隐私、哈希、DNS/TLS 与干净渲染 |

## 适用场景

| 场景 | 适配度 | 说明 |
|---|---:|---|
| 制作、优化专业简历 | ✅ | 收集事实、内容、输出、语言与视觉选择 |
| 导入 Reactive Resume | ✅ | 按维护的 schema 参考生成 JSON |
| 可携带简历网站或打印友好 HTML | ✅ | 生成语义化、响应式、内联 CSS 的 HTML |
| 已明确授权的静态部署 | ✅ | 使用同一 HTML 源文件并核验公网交付 |
| 完整求职投递管理 | ⚠️ | 仅在用户明确要求时进入 application-tracking 模式 |
| 通用作品集、落地页或产品网站 | ❌ | 应使用专门的前端或作品集工作流 |
| 编造经历或补写未经支持的主张 | ❌ | 先提供可核实事实 |

## 触发关键词

**中文：** `制作简历`、`生成简历`、`创建简历`、`写简历`、`优化简历`、`改简历`、
`做一份简历`、`简历网站`、`HTML 简历`、`单文件简历`、`在线简历`、`静态简历网站`、
`双语简历`、`中文简历`、`英文简历`、`Reactive Resume JSON`、`简历 JSON`、
`打印简历`、`简历 PDF 排版`、`部署简历`、`简历模板`、`简历美化`。

**English:** `create a resume`, `make a resume`, `build my CV`, `write my CV`,
`improve my resume`, `resume website`, `HTML resume`, `single-file resume`,
`online resume`, `static resume site`, `bilingual resume`, `Reactive Resume JSON`,
`printable resume`, `deploy my resume`, `resume template`.

## 快速开始

### 安装

```bash
# ClawHub
clawhub install 0xcjl/resume-creator

# 或克隆后暴露到所用 Agent 的 skill 目录
git clone https://github.com/0xcjl/resume-creator.git
```

### 使用

提供简历、Markdown 笔记或经过核实的职业材料，然后说“制作一份双语 HTML
简历”。中文交互使用中文回复，英文交互使用英文回复。

## 先选择，再生成

对于新简历，技能只收集尚未给出的选择：

1. 交付物：Reactive Resume JSON、单文件 HTML 或两者。
2. 语言：中文、英文或双语。
3. 视觉路径：15 个 Reactive Resume 视觉改编之一，或 3 种原生 HTML 风格之一。

技能会说明所有选项，并基于材料推荐 5 个视觉改编，但不会静默替用户选择。
这 15 个选项是受模板启发、重新编写的自包含 HTML 视觉改编，不是对 Reactive
Resume 应用的像素级导出承诺。

## HTML 输出与部署

HTML 输出为完整的单一 `.html` 文件：语义化结构、内联 CSS、系统字体、响应式布局、
可见焦点样式和打印规则；不依赖构建步骤、远程样式表、图片 CDN 或凭据。

部署是可选项，且必须获得明确授权。获授权后，部署验收会检查：

- 用户是否同意公开手机、邮箱、地址等联系方式；
- HTTPS 公网内容是否与最终本地源文件一致（哈希或等价比对）；
- 自定义域名的 DNS 记录与证书是否就绪；
- 干净浏览器/配置文件中的桌面、窄屏和打印版式。

浏览器扩展可能在页面加载后注入或改写文本。技能会先与无扩展渲染对比，再判断问题
是否属于 HTML 或托管环境。

## 质量与安全

- 所有事实必须来自用户提供或明确批准的材料。
- HTML 会检查语义结构、单文件约束、语言锚点、重复经历项对齐及最后一项包装错误。
- 长段正文才按视觉需要对齐；标题、日期、项目符号、元信息与技能标签不作为正文两端对齐。
- 本地预览验收与公网部署验收是两个独立步骤。

完整可复用指令见 [SKILL.md](./SKILL.md)，HTML 与部署检查见
[references/html-quality-check.md](./references/html-quality-check.md)。

## 目录结构

```text
resume-creator/
├── SKILL.md
├── references/
│   ├── schema.md
│   ├── template-selection.md
│   ├── html-styles.md
│   ├── html-quality-check.md
│   └── application-tracking.md
├── README.md
├── README.zh-CN.md
└── LICENSE
```

## 排错

| 现象 | 原因 | 处理方式 |
|---|---|---|
| 公网页面与本地文件不同 | 缓存、CDN 或部署了不同文件 | 对比公网抓取内容与源文件哈希 |
| 某个浏览器中出现重复、缩进或极窄文字 | 浏览器扩展改写了 DOM | 用无扩展配置文件检查；为该站暂停扩展 |
| 某段经历的项目符号跑到日期旁 | 包装或 Grid 边界错误 | 执行 item-header 的结构与视觉检查 |
| JSON 导入失败 | schema 字段或 UUID 不合法 | 按 `references/schema.md` 重新校验 |

## 致谢

- 本技能的 JSON 工作流与模板术语参考
  [Reactive Resume](https://github.com/AmruthPillai/Reactive-Resume)。
- Reactive Resume 使用 MIT 许可证；本技能为独立、兼容的指令包，并非官方产品。

## 许可证

[MIT](./LICENSE) © 2026 Jialin Cao (0xcjl)
