---
name: paper2slides
description: "Transform any academic paper PDF into a polished presentation slide deck"
homepage: https://clawhub.ai/skills/paper2slides
allowed-tools: [read, write, exec, pdf, image, canvas, web_search, tavily_search, tavily_extract]
user-invocable: true
---

# Paper2Slides — 论文秒变演示幻灯片

把一篇学术论文 PDF 变成一整套结构清晰、视觉专业的演示幻灯片。
支持 HTML/CSS 幻灯片、Marp Markdown 幻灯片、PPTX 等多种输出格式。

## 适用场景

- 组会汇报前懒得做 PPT → 一键生成
- 读论文时想要快速概览 → 幻灯片即笔记
- 给导师/同事分享论文 → 发一个幻灯片链接

## 工作流程

### 1. 加载论文

用户提供论文 PDF 路径或 URL。

```
@paper2slides paper.pdf
@paper2slides https://arxiv.org/pdf/2401.12345.pdf
@paper2slides paper.pdf --format html --theme dark
```

### 2. 论文理解

使用 `pdf` 工具解析论文全文，提取以下要素：

- **标题 + 作者 + 机构** → 封面页信息
- **摘要** → 核心浓缩
- **研究背景 / 动机** → 为什么做这个
- **方法 / 框架** → 怎么做的
- **实验设置** → 数据集、指标、基线
- **核心结果** → 关键数字、图表、对比
- **结论 + 未来工作** → 收尾和展望
- **图表/公式** → 视觉元素提取

### 3. 幻灯片结构生成

自动设计合理的幻灯片结构：

```
Slide 1:   封面（标题、作者、会议/期刊、年份）
Slide 2:   目录 / 演讲路线图
Slide 3:   研究背景 & 动机
Slide 4:   问题定义
Slide 5:   核心方法（概览图优先）
Slide 6:   方法细节（分步、公式、算法）
Slide 7:   实验设置
Slide 8:   主要结果（可视化！）
Slide 9:   消融/分析实验
Slide 10:  结论 & 贡献
Slide 11:  未来工作 / 讨论
Slide 12:  Q&A / 参考文献
```

**智能调整：**
- 短文（<6页）→ 4-6 张紧凑幻灯片
- 长文/期刊论文 → 12-18 张详细幻灯片
- 有大量图表 → 每张结果幻灯片配一个核心图表
- 理论性强 → 扩展方法论部分

### 4. 幻灯片渲染

#### 格式 A: HTML/CSS 幻灯片（推荐，默认）

使用 reveal.js 风格生成自包含 HTML 幻灯片文件：
- 现代、美观、可直接在浏览器打开
- 图片内嵌（base64），单文件自包含
- 深色/浅色主题可选
- 用 `canvas` 预览或保存为 HTML 文件

生成模板详见 `assets/slides-template.html`。

#### 格式 B: Markdown 幻灯片 (Marp)

生成 Marp 格式的 Markdown：
- 轻量级、易编辑
- 适合进一步手工调整
- 可导出为 PDF/PPTX

#### 格式 C: Python-pptx

生成 .pptx 文件（实验性）：
- 需要安装 python-pptx 库
- 基础布局和内容
- 适合在 PowerPoint 中编辑

### 5. 输出与交付

1. 保存生成的幻灯片文件到用户指定位置
2. 用 `canvas` 预览 HTML 幻灯片（如适用）
3. 提供编辑建议和自定义选项

## 可选参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--format` | 输出格式: html / marp / pptx | html |
| `--theme` | 主题: light / dark / modern | modern |
| `--lang` | 幻灯片语言: en / zh | en |
| `--slides` | 目标幻灯片数量（自动调整） | auto |
| `--focus` | 重点强调方向: method / result / all | all |
| `--no-figures` | 不自动嵌入图表 | false |

## 示例

```
@paper2slides paper.pdf
→ 解析论文，生成 HTML 幻灯片，canvas 预览

@paper2slides attention-is-all-you-need.pdf --theme dark --lang zh
→ 深色主题中文幻灯片

@paper2slides https://arxiv.org/pdf/2303.08774.pdf --format marp --focus result
→ 生成 Marp 格式，重点突出实验结果的幻灯片
```

## 高级特性

### 演讲备注
- 每张幻灯片生成演讲备注（speaker notes）
- 包含关键数据、过渡语、可能被提问的点

### 参考文献脚注
- 在底部的 Q&A 页自动整理参考文献
- 以标准引用格式呈现

## 注意事项

- PDF 格式的论文解析质量取决于 PDF 的结构完整性（扫描版效果较差）
- 生成的幻灯片需要人工校对，特别是数据和数字
- 不能完全替代人工设计，但能节省 80% 的基础工作量
- `--format pptx` 需要 python-pptx 库，首次使用会自动安装提示
