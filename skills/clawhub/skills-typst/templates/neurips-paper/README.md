# neurips-paper — kirklin Typst 模板

一套单栏、NeurIPS 风格的学术论文模板，**完整复刻** 原论文 **《Attention Is All You
Need》**（Vaswani et al., NeurIPS 2017）：带上下横线的标题、4/3/1 多作者块加等贡献脚注
（`*`/`†`/`‡`）、全部编号章节、行内与行间公式、`booktabs` 风格的四张表（含最复杂的 Model
Variations 合并表头/跨行表）、**真实的架构图与注意力可视化图片**（`Figures/`、`vis/`，用
`image()` 嵌入，不是手绘）、数字编号引用（ACM 样式，贴近原文 `plain`）、40 条参考文献，以及附录里的注意力可视化。

## 自成一体，离线可编译

样式全部写在本地的 `neurips.typ` 里（一个 `#neurips(...)` 函数），**不依赖任何
`@preview` 包**，所以无需联网下载、在沙箱里也能编译。为贴近真实 NeurIPS 版式，正文用
**Times New Roman**、公式用 **STIX Two Math**（Times 兼容的数学字体）——都是 Typst
自带字体，`typst fonts` 可查。标题的粗/细双横线、加粗作者名、`*`/`†`/`‡` 页脚脚注、
第一页会议脚注、其后页码，都按 `nips_2017.sty` 的观感复刻。

```bash
# 在仓库根目录
bash scripts/compile.sh templates/neurips-paper/paper.typ --preview

# 或直接用 typst
typst compile templates/neurips-paper/paper.typ
```

产物为 15 页 PDF。Typst 单遍编译即可解析交叉引用、引文与目录——没有 latexmk 多轮那一套。

## 文件结构

```
paper.typ               主文件：标题 / 作者 / 摘要，并 #include 各章节 + 参考文献
neurips.typ             样式函数 #neurips(...)（样式的核心，改这里换版式）
introduction.typ        第 1 节 Introduction
background.typ          第 2 节 Background
model-architecture.typ  第 3 节 Model Architecture（公式 + Figure 1/2 真实图片）
why-self-attention.typ  第 4 节 Why Self-Attention（含复杂度表 Table 1）
training.typ            第 5 节 Training（含学习率公式）
results.typ             第 6 节 Results（WMT / Model Variations / Parsing 三张表）
visualizations.typ      附录 Attention Visualizations（Figure 3/4/5 真实图片）
references.bib          BibTeX 参考文献库，40 条（Typst 原生读取 .bib）
Figures/ModalNet-*.png  Figure 1 架构图、Figure 2 注意力示意图
vis/*.png               附录注意力可视化（原为 PDF，已转 PNG 供 Typst 嵌入）
```

## 改成你自己的论文

1. **标题与作者**：改 `paper.typ` 里 `neurips.with(...)` 的 `title` 和 `authors`。
   `authors` 是字典数组，键为 `name` / `affiliation` / `email`，外加可选的 `note`
   （给该作者单独挂一个脚注，符号自动排为 `†`、`‡`…）；`affiliation` 留空则不显示那一行。
   全体作者共享 `*` 等贡献脚注，正文由 `equal-contribution:` 参数给出。
   **作者分行**由 `authors-per-row:` 控制：给整数是等分（如 `4`），给数组是逐行指定
   （如 `(4, 3, 1)`——本样张即用它复刻了原论文 4/3/1 的排布）。第一页底部的会议信息由
   `venue:` 给出，其后页面自动居中页码。
2. **摘要**：改 `abstract:` 的内容。
3. **章节**：逐个替换 `*.typ` 的正文；不需要的章节，把 `paper.typ` 里对应的 `#include`
   删掉即可。用 `= 标题` 建一级节、`==` 二级、`===` 三级。
4. **图**：图都用真实图片，`#figure(image("Figures/…png", width: …))` 嵌入。注意 Typst
   的 `image()` 支持 **PNG/JPG/SVG，但不支持 PDF**——PDF 图请先转 PNG/SVG（本模板 `vis/`
   即由 `pdftoppm -png` 从原论文 PDF 转来）。换你自己的图：替换 `Figures/`、`vis/` 里的
   文件并改 `image()` 路径即可。
5. **表**：`results.typ` 用 `#table(stroke: none)` + `table.hline()` 做三线表；最复杂的
   Model Variations 表用 `table.cell(rowspan: …)` 做 (A)–(E) 分组标签、`table.cell(colspan:
   …)` 做合并表头，`table.vline()` 加竖分隔线。
6. **参考文献**：往 `references.bib` 加条目，正文用 `@bibkey` 引用。样张用
   `style: "association-for-computing-machinery"`（全名 + 数字编号 + 字母序，最接近
   LaTeX 的 `plain`）；换风格改 `paper.typ` 末尾的 `bibliography(...)`（如 `"ieee"`、
   `"apa"`、`"chicago-author-date"`）。

## 出处与署名

本模板的正文、图表与参考文献取自《Attention Is All You Need》（arXiv:1706.03762），
仅作**排版样张**。把它当模板使用时，请替换为你自己的内容。样式函数 `neurips.typ`
是对 NeurIPS 版式的近似复刻，非官方文件。
