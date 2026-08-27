# 公文 Word 生成工作流（最终版）

把 Markdown 转成符合 党政机关公文格式（GB/T 9704-2012）及通用公文排版规范的 Word，
分两步：**生成（Node + docx 库）** → **后处理（Python 补字体/缩进）**。

## 1. 环境
- Node 托管环境：`/Users/weidong/.workbuddy/binaries/node/versions/22.22.2/bin/node`
- 安装 docx（隔离在托管 workspace）：
  `cd /Users/weidong/.workbuddy/binaries/node/workspace && /Users/weidong/.workbuddy/binaries/node/versions/22.22.2/bin/npm install docx`
- 运行生成脚本时指定模块路径：
  `NODE_PATH=/Users/weidong/.workbuddy/binaries/node/workspace/node_modules node generate_gongwen_docx.js input.md output.docx`

## 2. 生成脚本（scripts/generate_gongwen_docx.js）
已固化全部规则，核心要点：

- 字体：标题=方正小标宋简体（二号、居中）；一、黑体 / （一）楷体 / 1、仿宋 / （1）仿宋（三号）；正文仿宋GB2312。
- 缩进**双单位**：非正文段落 `indent:{firstLine:0, firstLineChars:0}`；正文及（1）分点
  `indent:{firstLine:640, firstLineChars:200}`。只写一种单位会让某些 Word/预览回退本地模板缩进。
- 对齐：正文段落和（1）分点 `AlignmentType.JUSTIFIED`（两端对齐），不是只左对齐。
- 层级标题（一~四级）一律顶格、**段前段后间距 0**（`spacing:{before:0,after:0}`）。
- 第四层（1）属内容性分点：同正文缩进2字、两端对齐，**不要顶格**。
- 分点标点：同组（1）…（n），末项 `。`、其余 `；`。
- 页码：页脚居中、无缩进、阿拉伯数字 Times New Roman（四号），用 `PageNumber.CURRENT`。
- 表格：首行三列水平+垂直居中（`VerticalAlign.CENTER` + 段落 `CENTER`），表头黑体；数据单元格左对齐。
- 版面：A4；页边距 上37 下35 左28 右26 mm（twips：2097/1984/1587/1474）；行距固定值28磅（560 twips）。
- 落款：说明性材料（修改/编制/起草说明等）默认不加；正式发文才补署名+成文日期。

输入兼容两种写法：
- 标准 markdown 标题（`#`~`######`），按深度自动编号（##→一、 ###→（一） ####→1、 #####→（1））。
- 已带公文编号的文字（含 `**加粗**` 伪装成标题的，如 IMA 导出的 md），按 `一、/（一）/1、/（1）` 直接定级。
- `1）2）3）` 自动归一为 `（1）（2）（3）` 并补 `；/。`。

## 3. 后处理（关键，scripts/fix_fonts.py）
docx 库只写 `ascii/hAnsi` 不写 `eastAsia`，且不会创建 Normal 样式。后处理：
- 遍历 `word/document.xml` 与 `word/footer*.xml` 的 `w:rFonts`，把 `ascii` 值抄到 `eastAsia`，并把
  `ascii/hAnsi` 改为 `Times New Roman`（中文用对应中文字体，数字用新罗马体）。
- 给每个 `w:pPr` 显式补齐 `firstLine/firstLineChars/left/leftChars`（无缩进段落双单位均为 0，正文为 2 字）。
- 在 `styles.xml` **显式创建 Normal 样式**，并在 Normal 与 `docDefaults/pPrDefault` 上同时声明
  首行缩进=0、左缩进=0。否则打开文件时 Word 会套用本地 Normal 模板，出现"XML 写了无缩进、打开却有缩进"。
- 用法：`python fix_fonts.py output.docx`（缺省路径回退到固定文件名）。

## 4. 校验清单
- 解压 docx，抽取 `word/document.xml` 文本，统计层级标记：一、/（一）/1、/（1）应各出现且符合预期；第四层必须是 `（1）` 不是 `1）`。
- 校验"残留独立 1）"**必须用中文全角否定后顾** `(?<!（)\d+）`，不能基于 ASCII `(`；否则会把
  `（1）` / `（图1）` / `（表1.1）` 误判为残留（这是经典的误报坑）。
- 检查 `w:rFonts` 是否都带 `w:eastAsia`；数字 `ascii` 是否为 `Times New Roman`。
- 检查表格首行三列 `w:jc="center"` 且单元格 `w:vAlign="center"`。
- 检查 1~4 级标题 `w:spacing` 的 `before/after` 均为 0。
- 检查页脚 `w:jc="center"`、`firstLineChars=0`、含 PAGE 字段。

## 5. 红头文件（如需）
公文处理办法定义了 发文机关标志/发文字号/签发人/红色反线 等要素。若用户要正式红头，需补充：
发文机关标志（红色宋体）、发文字号（三号仿宋）、签发人、红色反线、份号/密级等。无文号/签发人信息时，
默认生成"公文样式材料"（标题+正文+落款），不伪造红头。
