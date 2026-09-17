# brand-pdf-deck-replica · 品牌 PDF 报告复刻

> 把一份「PowerPoint 导出的品牌 PDF 报告」复刻成**同尺寸**的 `pptx` + `pdf` + `html` 三件套，
> 并把每张图表的**数据从矢量图形反解成 CSV**。

**作者**：王东杰 (Wang Dong Jie) · [yjkj999999](https://github.com/yjkj999999)
**许可**：MIT-0（可自由使用、修改、再分发，无需署名）
**版本**：1.0.0

---

## 它解决什么问题

你拿到一份机构研报 PDF（贝莱德智库、麦肯锡、摩根士丹利……），想：

- 复刻它的**版式风格**，做成能在自家汇报里用的 pptx / pdf / html；
- 把里面图表的数据**扒出来**，而不是照着图重新估一个。

难点在于：这类 PDF 大多由 PowerPoint 导出，**中文字体没有 ToUnicode 映射**（`pdftotext` 出来全是 `本本本本`），
但好处是**图表往往是原生矢量**——意味着数据可以被精确反解，而不是靠肉眼读数。

本技能规定了两件事：**什么能还原**，以及**什么必须承认不能还原**。

---

## 安装

把本目录放进任意技能根目录即可：

```bash
# WorkBuddy
cp -r brand-pdf-deck-replica ~/.workbuddy/skills/
# OpenClaw / QClaw
cp -r brand-pdf-deck-replica ~/.openclaw/skills/
cp -r brand-pdf-deck-replica ~/.qclaw/skills/
```

依赖（都是常见命令行工具，Python 侧仅两个包）：

```bash
# macOS
brew install poppler        # 提供 pdfinfo / pdftotext / pdftocairo / pdftoppm / pdfimages
pip install python-pptx Pillow
```

---

## 快速开始

```bash
# 1) 探针：判定能不能反解
bash scripts/probe_pdf.sh 你的报告.pdf 6

# 2) 单页矢量结构化（看元素、点数、颜色、bbox）
pdftocairo -svg -f 6 -l 6 你的报告.pdf pg6.svg
python3 scripts/svgdump.py pg6.svg

# 3) ……按 SKILL.md 的 Step 2/3 重建版式与数据……

# 4) 出 PDF（纯 SVG 版面必须 SKIP_VERIFY=1）
SKIP_VERIFY=1 bash ~/.workbuddy/skills/html-to-pdf-cdp/scripts/render_html_pdf.sh in.html out.pdf 3200 css

# 5) 封 PPTX
python3 scripts/mkpptx.py out.pdf out.pptx 200

# 6) 体检
python3 scripts/layout_qa.py out.pdf
```

---

## 包含的脚本

| 脚本 | 作用 |
|---|---|
| `scripts/probe_pdf.sh` | 4 条探针命令一次跑完，输出「能否反解」的判定依据 |
| `scripts/svgdump.py` | 通用矢量取数器：解析 `pdftocairo` 的 SVG，复合 `<g>` 变换（含 y 翻转），输出点集/子路径/颜色/bbox |
| `scripts/mkpptx.py` | PDF → PPTX：与原稿同尺寸、逐页满幅铺底、页文写入演讲者备注 |
| `scripts/layout_qa.py` | 逐页体检：墨迹%/彩色%/右侧出血/底部出血，标出可疑页 |

全部只依赖标准库 + `python-pptx` + `Pillow`，不联网、不需要任何凭证。

---

## 六条硬门（摘要）

1. 页面尺寸与页数 = 原稿（内容页 + 附录）
2. 页脚文件编号与页码**逐页**与原稿对齐
3. 无空白图（逐页 ink% / color%）
4. 无出血溢出（**只查文字栏**，须先排除设计上的满高色带）
5. 无黑底黑字（深色区域浅色像素数 > 0）
6. 计数自洽（声明的图表数/系列数/CSV 数 = 实际文件数）

完整判定表、三个数据反解陷阱、六类故障速查见 `SKILL.md`。

---

## 实战案例

`examples/blackrock_2026_case.md` 记录了用本技能复刻贝莱德智库《2026年中全球投资展望》
（19 页 / 792×594pt / 10 张图 / 34 系列 / 5,553 数据点）的全过程，
包括**交付前抓出并修掉的 5 个真实缺陷**（文件编号错字、合并页导致页码错位、
文字溢出出血、黑底黑字隐形、附录计数不实）。

---

## 重要声明

- 本技能只做**版式与数据的还原**。复刻第三方机构报告时请自行确认版权与合规边界，
  对外分发前建议标注数据来源与还原方法。
- 中文文本在无 ToUnicode 映射时**只能依渲染图与主题重建**，不保证逐字精确——
  交付时必须如实标注，不得暗示精确复刻。
- 若原稿某页图形是着色蒙版位图，**无法矢量还原**，应如实声明并只做意象重构。

---

## License

MIT-0 · Copyright (c) 2026 王东杰 (Wang Dong Jie) · yjkj999999
