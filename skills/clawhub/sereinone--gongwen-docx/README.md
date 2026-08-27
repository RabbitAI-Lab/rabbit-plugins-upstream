# gongwen-docx

将 Markdown（含 IMA 导出的 md、纯文本）转换为符合 **GB/T 9704-2012《党政机关公文格式》** 及通用公文排版规范的 Word 文档。

## 核心能力
- 四级层次序数：`一、` 黑体 / `（一）` 楷体 / `1、` 仿宋 / `（1）` 仿宋（分点）。
- 标题（二号方正小标宋）、正文（三号仿宋_GB2312）、阿拉伯数字（Times New Roman）。
- 所有层级与正文统一首行缩进 2 字（twips + 字符双单位），两端对齐。
- 表格默认四号字体、`根据内容调整表格`（AutoFit）、表头居中。
- 自动识别并清理 IMA 外壳、HTML 实体、`*`/`**` markdown 标记（替换为空）。
- **中文引号 `“ ”` `‘ ’`（及全角形式）随上下文字体渲染**：属高 ANSI 码位，已做拆分 run 强制用对应中文字体，不再呈罗马字体。
- 报告模式（含「第X部分 / 第X章」）自动进入，干净无抬头无落款；所有模式默认不加落款。
- 居中页码、A4 公文页边距、固定行距 28 磅。

## 用法
```bash
# 1. 生成 docx（需先 npm install docx 到托管 node workspace）
NODE_PATH=<node_workspace>/node_modules <node> scripts/generate_gongwen_docx.js input.md output.docx

# 2. 后处理（补全 eastAsia 字体、双单位缩进、显式 Normal 样式、引号中文字体）
python scripts/fix_fonts.py output.docx
```

## 目录
- `scripts/generate_gongwen_docx.js`：Markdown → 公文 核心生成脚本。
- `scripts/fix_fonts.py`：字体 / 缩进 / 引号 后处理脚本（支持任意路径参数）。
- `references/workflow.md`：生成工作流要点与校验清单。

## 版本与更新日志

### v1.0.0（2026-07-29）
首个可发布版本，整合全部能力：
- 四级层次序数自动判定与重排（`一、`/`（一）`/`1、`/`（1）`，无 `1）` 写法）。
- 字体：标题二号方正小标宋、一级黑体/二级楷体/三级仿宋/四级仿宋、正文三号仿宋_GB2312；阿拉伯数字 Times New Roman。
- 所有层级与正文统一首行缩进 2 字（twips + 字符双单位），两端对齐。
- 表格默认四号、`根据内容调整表格`（AutoFit）、表头居中。
- 报告模式（第X部分/第X章）自动进入，无抬头无落款；所有模式默认不加落款。
- IMA 外壳 / HTML 实体自动清理；`*`/`**` markdown 标记批量替换为空。
- 中文引号随上下文字体正确渲染（不再呈罗马字体）。
- 中文与中文 / 中文与标点之间的多余空格自动清除（保留 中文+拉丁/数字 空格）。
- 居中页码、A4 公文页边距、固定行距 28 磅。

