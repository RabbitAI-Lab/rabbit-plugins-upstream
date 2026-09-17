---
name: brand-pdf-deck-replica
description: |
  把一份「PowerPoint 导出的品牌 PDF 报告」（贝莱德智库/BII、麦肯锡、摩根士丹利等范式）复刻成
  同尺寸的 pptx + pdf + html 三件套，并把每张图表的数据从矢量图形反解成 CSV。
  核心能力：① 探针判定该 PDF 的图表是矢量还是着色蒙版位图；② 用「矢量路径取点 + 刻度文字坐标
  线性拟合」还原数值，并以 clipPath 矩形与 PIL 像素扫描做三路交叉校验；③ 按原稿页面尺寸
  （如 792×594pt）1:1 重建版式（含页脚文件编号、页码、色带、深色面板）；④ CSS @page 出 PDF；
  ⑤ python-pptx 满幅铺底 + 演讲者备注封装 PPTX。
  当用户给出一个品牌 PDF 并要求「复刻」「仿照这个风格」「全要数复刻提取」「做成贝莱德智库风格」
  的 pptx/pdf/html，或要求把 PDF 图表里的数字扒出来时使用。也用于任何「按原稿页面尺寸 1:1 重建
  + 数据还原」的交付。
homepage: https://github.com/yjkj999999/brand-pdf-deck-replica
author: 王东杰 (Wang Dong Jie) · yjkj999999
license: MIT-0
version: 1.0.0
read_when:
  - 用户给出一个品牌 PDF 报告并要求复刻成 pptx/pdf/html
  - 用户要求「全要数复刻提取」「把图里的数据扒出来」
  - 用户说「做成某某智库风格」「按这个 PDF 的版式来一份」
  - 需要从 PowerPoint 导出的 PDF 中反解图表原始数值
metadata:
  openclaw:
    emoji: 🧬
    version: "1.0.0"
    author: 王东杰 (Wang Dong Jie) / yjkj999999
    homepage: https://github.com/yjkj999999/brand-pdf-deck-replica
    license: MIT-0
    requires:
      binaries:
        - python3
        - pdftotext
        - pdftocairo
        - pdftoppm
        - pdfinfo
        - pdfimages
    python_packages:
      - python-pptx
      - Pillow
  security:
    credentials_usage: |
      本技能不联网、不需要任何凭证。全部处理在本地完成：读取用户提供的 PDF，输出本地文件。
      不发送任何数据到外部服务。唯一的外部依赖是可选的 html-to-pdf-cdp 技能（本地 Chrome + CDP）。
    allowed_domains: []
---

# 品牌 PDF 报告复刻（同尺寸 pptx + pdf + html + 数据 CSV）

作者：**王东杰 (Wang Dong Jie) · yjkj999999**
许可：**MIT-0**（可自由使用、修改、再分发，无需署名）

本技能解决一类固定任务：**用户丢来一份品牌 PDF（通常是 PowerPoint 导出），要求复刻版式并还原其中数据**。
技能的核心不是"画得好看"，而是**判定口径与验收门**——它规定了「什么能还原、什么必须承认不能还原」，
避免交出一份看着漂亮但数据是编的报告。

---

## Step 0 · 先探针，别急着动手（4 条命令定性质）

一键探针：

```bash
bash scripts/probe_pdf.sh src.pdf
```

等价于手工执行：

```bash
pdfinfo  src.pdf | grep -E '^(Pages|Page size)'   # 页数 + 页面尺寸(pt)
pdftotext -layout src.pdf - | head -40            # 中文是否乱码？(ToUnicode 缺口)
pdfimages -list src.pdf | awk 'NR>2{c[$1]++} END{for(p in c) print p, c[p]}'  # 每页内嵌位图数
pdftocairo -svg -f N -l N src.pdf pg.svg          # 单页矢量导出，看 path/polyline 数
```

判定表：

| 现象 | 含义 | 对策 |
|---|---|---|
| `pdftotext` 出 `本本本本` 但拉丁字符/数字正常 | 中文字体缺 ToUnicode 映射 | 文字**只能靠渲染图人工判读或依原报告知识重建**；数字标定仍可用（见 Step 2） |
| `pdftocairo -svg` 里 `fill="rgb(...)"`，无 `<image>` | 图表是**矢量** | 可精确反解数据（Step 2） |
| 某页 `<image>` 数百个、`fill` 只有寥寥几色 | 该页图形是**着色蒙版位图** | **无法矢量还原**，必须如实声明「此处为位图，仅做意象重构」 |
| 页面出现整块纯色（抽样 `distinct≈1`） | 设计上的满高色带/黑面板 | 照做即可，且**落在其上的页脚文字必须换浅色** |

> 实测：某品牌 19 页 PDF 每页有 15–230 个 `<image>`（2×2 索引图 + smask 成对），
> 但数据图表页仍有完整矢量折线/矩形——**「有位图」不等于「不能反解」**，必须逐页看。

---

## Step 1 · 文字内容

中文乱码时不要硬凑：**拉丁标签 + 数字 + 对原报告主题的先验知识**是唯一可靠来源。
把重建出的文字结构化成一个 `content.py`（每页一个 dict），后续所有渲染都从它取数，
便于逐页替换与复核。

凡重建，必须在交付说明里写明「中文内容系依渲染图与主题重建」，**不得暗示逐字精确**。

---

## Step 2 · 数据反解（矢量路径 + 刻度标定）

`scripts/svgdump.py` 提供通用取数器：解析 `pdftocairo` 出的 SVG，复合所有 `<g>` 的
`matrix()` 变换（注意 y 轴翻转 `matrix(1,0,0,-1,0,594)`），输出每个元素的点集、子路径、
填充色/描边色与 bbox。

```bash
python3 scripts/svgdump.py pg6.svg        # 列出元素、点数、颜色、bbox
```

反解流程：

1. **曲线**：取带品牌色 `stroke` 的 path，采样点即数据点。
2. **柱形**：取填充 `rect`；**斜纹/图案填充的柱子数量不在填充里，在其 `clipPath` 矩形里**——必须解析 clipPath。
3. **标定**：用 `pdftotext -bbox` 拿刻度数字（拉丁字符，未乱码）的坐标，对「数值 ↔ 像素」做线性拟合。
4. **验收线：标定残差 ≤ 0.1pt**。个别斜纹柱可能到 0.3pt 量级，必须在报告里点名说明，
   **不能笼统写「全部 ≤0.07pt」**。
5. **三路交叉校验**：矢量路径 / clipPath 矩形 / PIL 像素扫描，结果一致才可交付。

三个必踩坑：

- **图例行也是同色 path**，会把 y 值拉飞 → 用绘图区矩形过滤（`in_plot()`）。
- **分组/堆叠柱不能用系列内部序号当类别** → 按 x 坐标的**最大间隙聚类**分配类别。
- **颜色到系列的映射会张冠李戴** → 用脚注语义 + 数值全为正/负反向验证。

真实案例（含残差与修正过程）见 `examples/blackrock_2026_case.md`。

---

## Step 3 · 版式 1:1 重建（纯 HTML+SVG，不用 PPT 模板）

- `@page{ size: <W>pt <H>pt; margin:0 }`，`.slide{ width:<W>pt; height:<H>pt; overflow:hidden }`。
- **页脚必须带原稿真实页码**：`<文件编号>-<页码>/<总页数>`。文件编号要**逐字节核对原 PDF**：

  ```bash
  pdftotext -f 4 -l 4 src.pdf - | grep -o 'MKTG[^ ]*' | od -c
  ```

  凭记忆手打极易多/漏字母（实战中曾把 `MKTG0726-5754384-EXP0727` 打成
  `MKTGT0726-5754384-EXIP0727`，多一个 T、多一个 I）。
- 页数与原稿不一致时（合并/拆分页），**页码仍标原稿真实页**（如合并页标 `2–3`），
  不要用 deck 序号充当页码。更稳妥：显式维护「deck 索引 → 原稿页码」映射函数。
- 深色面板上的任何文字（标题、页脚免责声明、页码）都要切浅色，否则黑底黑字。
  给 `page_footer()` 加 `dark_left/dark_right` 参数最省事。

---

## Step 4 · 出 PDF

用 `html-to-pdf-cdp` 技能的 `render_html_pdf.sh`（CDP `Page.printToPDF`，
绕开 headless `--print-to-pdf` 被沙箱 SIGKILL 的问题）：

```bash
SKIP_VERIFY=1 bash ~/.workbuddy/skills/html-to-pdf-cdp/scripts/render_html_pdf.sh in.html out.pdf 3200 css
```

**纯 SVG 版面必须加 `SKIP_VERIFY=1`**：该脚本自带的 `verify_charts.js` 只认 `<canvas>`，
会对着完全正确的 SVG 版面误报「12 个 canvas 未绘出」。

---

## Step 5 · 封 PPTX（满幅铺底 + 备注全文）

```bash
python3 scripts/mkpptx.py out.pdf out.pptx 200
```

实现要点（`scripts/mkpptx.py` 已封装）：

```python
prs.slide_width, prs.slide_height = W*12700, H*12700   # 1pt = 12700 EMU，与原稿同尺寸
# 每页：pdftoppm -r 200 出图 → add_picture(0,0,W,H) 满幅
# 备注：notes_text_frame.text = 该页 pdftotext 全文（压掉页脚声明/编号）
```

**为什么用图铺底而不是原生形状**：自绘 SVG 图表无法用 python-pptx 表达；位图保真 100%，
文字则靠**演讲者备注**保留可检索/可复制性。**交付时必须说明这一取舍**，并主动提供
「原生形状降级稿」作为备选。

---

## Step 6 · 交付硬门（全过才算完成）

体检脚本：

```bash
python3 scripts/layout_qa.py out.pdf
```

| # | 门 | 检查方式 |
|---|---|---|
| 1 | 页面尺寸与页数 | `pdfinfo`：Page size = 原稿；页数 = 内容页 + 附录 |
| 2 | 页码/文件编号逐页对齐 | 对每页 `pdftotext \| grep -o 'MKTG[^ ]*'`，与原稿逐页比对 |
| 3 | 无空白图 | 逐页 ink% / color% 覆盖率；纯文字页 color≈0 属正常 |
| 4 | 无出血溢出 | 逐页测**底部/右侧出血带**墨量；但**必须先排除设计上的满高色带**，只查文字栏区域 |
| 5 | 无黑底黑字 | 对深色区域抽样统计浅色像素数 > 0 |
| 6 | 计数自洽 | 附录里声明的「N 张图 / N 个系列 / N 个 CSV」必须等于实际文件数 |
| 7 | PPTX 结构 | `slides` 数、宽高（in）、每页 1 张图、备注字数 |

> 第 4 门最容易误判：满高黑面板本身就会把「出血带墨量」顶满，
> 必须把检测区域**收窄到文字栏**再判定（实测该页文字栏 545–558pt 墨量为 0 即安全）。

---

## 常见故障速查

| 症状 | 根因 | 修法 |
|---|---|---|
| `TypeError: not all arguments converted` | `'a' 'b' % args` 中 `%` 只作用于**最后一个**字面量，`+` 拼接的段不参与 | 每段单独 `%` 格式化后 `''.join()`，别指望一条链式格式 |
| 命令被系统策略拦截 | Python 里定义了名为 `reg` 的函数/变量，命中 Windows `reg` 命令黑名单 | 改名（如 `zone`/`band`） |
| 改完代码 PDF 仍是旧版面 | Chrome 复用了上一次的 user-data-dir | 用 `render_html_pdf.sh` 自起模式（每次全新 profile） |
| 图表全白 | HTML 里根本没写进图表 SVG | 先 grep 输出的 HTML 里目标元素数量，再看渲染 |
| 页码全错一位 | 合并了原稿的某两页，却仍用 deck 序号当页码 | 显式维护「deck 索引 → 原稿页码」映射 |
| CSV 比声明的系列多 | 同一系列被按两种命名/精度各写一份 | 交付前按内容哈希查重，删低精度副本 |

---

## 产出物清单

```
brand-deck/
  deck/content.py        # 结构化全文（每页一个 dict）
  deck/charts.py         # 纯 SVG 图表渲染器（无 JS）
  deck/gen_html.py       # 装配：页脚/色带/面板/各页 renderer + build()
  build/extract.py       # 矢量路径 → 数值（含标定与三路校验）
  out/*.html / *.pdf / *.pptx / csv/*.csv
```

---

## 本地许可

MIT-0 · Copyright (c) 2026 王东杰 (Wang Dong Jie) · yjkj999999
