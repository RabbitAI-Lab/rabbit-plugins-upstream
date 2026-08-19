# 📝 docx-trackdiff

![docx-trackdiff banner](docs/banner.png)

**对比两个 Word 文档（.docx），一键生成原生"修订模式"（Track Changes）对比文件——就像一位编辑打开"修订"后亲手把旧稿改成新稿。**

[English](README.md) | 简体中文

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Format](https://img.shields.io/badge/format-DOCX%20%2F%20OOXML-orange)
![Kimi](https://img.shields.io/badge/built%20with-Kimi%20K3%20Agent%20Swarm-blueviolet)
![PRs](https://img.shields.io/badge/PRs-welcome-brightgreen)

`修订模式` `track-changes` `docx对比` `word文档比较` `红线标注` `ooxml` `kimi技能` `agent-swarm`

---

## 🤔 为什么做这个工具

AI 辅助写作的时代，文档迭代极快：论文、报告、合同——每一轮对话都产出一个新版本。你想知道两版之间**到底改了什么**，而且要用所有人都看得懂的形式：**Word 原生修订视图**，每一条修改都可以逐条接受或拒绝。

现有方案都不够好：

- ☁️ 在线对比工具要上传未发表的手稿——对未发表研究来说隐私不可接受
- 📄 Word 自带的"比较"功能依赖手工 GUI 操作，无法脚本化进自动化流程
- 🐍 `difflib` 之类的工具只能给文本 diff，给不了带真正 `<w:ins>` / `<w:del>` 修订标记的 Word 文件

这个工具补上了缺口：**一条命令进，一份修订模式 .docx 出**——在 Microsoft Word、WPS 或 LibreOffice 里打开，就是你熟悉的"所有标记"视图。

## 📸 效果演示

用两份合成演示文档（含文字、图片、表格）对比，不涉及任何真实数据：

| 第 1 页 —— 标题、行内修改、被删说明段、被替换的图 | 第 2 页 —— 表格单元格修改、新增行、重写的结论、新增章节 |
|---|---|
| ![demo page 1](docs/demo-1.png) | ![demo page 2](docs/demo-2.png) |

注意这些细节：

- 🔤 **词级行内修订**——`12%` → ~~12~~`18%`、~~sharply~~`moderately`
- 🖼️ **图片替换可追踪**——旧图被标为删除且**原始字节完整保留**，"拒绝修订"能真正恢复旧图；新图标为插入
- 📊 **表格修改**——单元格数值变化（`4.5` → `4.3`）和整行插入（`Delta`）
- ➕➖ **整段增删**——被删的图表说明段、新增的"Next Steps"章节

[`examples/`](examples/) 目录里有现成的演示文件，可以自己跑一遍：

```bash
python3 scripts/compare_docx_tracked.py examples/demo_v1.docx examples/demo_v2.docx out.docx --author "你的名字"
```

## ✨ 特性

- ✅ **原生 Word 修订**——真正的 `<w:ins>` / `<w:del>`，带唯一 ID、作者、日期；自动开启 `w:trackChanges`
- ✅ **词级粒度**——修改段落做细粒度行内 diff，而不是粗暴的整段替换
- ✅ **结构感知**——完整保留新版的标题样式、表格、脚注、超链接、OMML 公式和节版式
- ✅ **图片双向保真**——被替换的旧图字节保留在删除标记内，拒绝修订可无损恢复
- ✅ **隐私优先**——100% 本地运行，零上传，零网络调用
- ✅ **自我验证**——内置验证器模拟"接受全部"（必须等于新版）和"拒绝全部"（必须等于旧版），外加 5 项结构检查
- ✅ **零配置**——一个 Python 脚本 + `lxml`，没了

## 🚀 快速上手

环境要求：Python 3.8+，`lxml`（`pip install lxml`）。LibreOffice 可选（仅用于渲染检查）。

```bash
git clone https://github.com/stephenlzc/docx-trackdiff.git
cd docx-trackdiff

# 1. 生成修订对比文件
python3 scripts/compare_docx_tracked.py 旧版.docx 新版.docx 输出.docx \
    --author "你的名字" --date "2026-08-15T00:00:00Z"

# 2. 验证（必做——7 项自动检查）
python3 scripts/verify_tracked.py 输出.docx 旧版.docx 新版.docx

# 3. 可选：渲染检查
soffice --headless --convert-to pdf 输出.docx
```

在 Word 中打开输出文件 → 审阅选项卡 → **所有标记**，逐条接受或拒绝。

### 参数

| 参数 | 默认值 | 含义 |
|---|---|---|
| `--author` | `Editor` | Word 修订面板中显示的修订人 |
| `--date` | 当天 | 修订时间戳 |
| `--threshold` | `0.45` | 段落相似度阈值：高于它 → 词级行内 diff；低于它 → 整段删除+插入 |

## 🤖 作为 Kimi Agent 技能使用

本仓库同时是一个 **Kimi agent skill**。克隆本仓库（或下载 ZIP）后，把文件夹放进 Kimi 技能目录（`~/.kimi-code/skills/` 或 `~/.agents/skills/`），然后直接说：

> "对比一下这两个版本的 docx，给我一份修订模式的文件"
> "Compare these two Word documents with track changes"

Agent 会读取 `SKILL.md`，调用内置脚本，自动验证，把红线对比文件交给你——全程零手工。

## 🧠 工作原理

1. **段落对齐**——`difflib.SequenceMatcher` 对归一化文本（弯引号、破折号、空白折叠）做全文段落对齐；replace 块内用动态规划二次配对"修改"段落（相似度 ≥ 阈值）
2. **词级 diff**——修改段落分词后做 diff，run 在 diff 边界拆分且保留原格式；diff 边界跨越原子元素（图片、公式、超链接）的段落按设计回退为整段删除+插入
3. **规范的 OOXML 操作**——被删段落带格式深拷贝、文本转 `w:delText`、段落标记打标、关系 ID 重映射、**旧图字节拷入包内**保证拒绝修订无损；`w:trackChanges` 插入 `settings.xml` 的 schema 正确位置
4. **七项验证**——修订 ID 唯一、`w:del` 内无残留 `w:t`、引用无悬空、接受/拒绝双向等价、删除内容覆盖、作者日期齐全、旧图字节保留

完整规则与已知失败模式见 [`references/ooxml-revision-rules.md`](references/ooxml-revision-rules.md)。

## ⚠️ 已知限制

- 对比范围为**文档正文**（含表格单元格）；批注和脚注**内容**不参与对比
- 少数含图片/公式的段落会以整段删除+插入呈现（设计内回退）
- 通过 LibreOffice + XML 级模拟验证；重要场景建议在桌面版 Word 的"所有标记"视图中过目一遍
- `.doc` 文件需先转换为 `.docx`

## 🌱 诞生故事

这个技能不是凭空设计的，而是从真实工作流里长出来的。Big Stephen 在一篇学术论文的多轮 AI 辅助修订中，需要精确看到每个版本之间的改动。整条流水线——diff 算法、OOXML 修订标记、验证框架、乃至技能打包本身——都是通过 **Kimi K3 的 Agent Swarm**（[Moonshot AI](https://www.moonshot.cn/) 出品）实现的：coder 子代理构建并加固脚本，随后一轮 swarm 式评估（with-skill 与 baseline 配对盲测 + 独立评分代理）在发布前抓出并修复了一个真实的图片保真 bug。

那次评估的关键结论：使用技能的运行**约 1 分钟**完成，而能力不差的从零实现基线用了**约 15 分钟**，且零判断失误。独立盲评也证明了自己的价值——它抓到了一个真实的图片保真缺陷（被替换图片的*旧图字节*被静默丢失，"拒绝修订"会恢复成错误的图），而技能自带的纯文本验证器对此完全不可见。修复方案和两项新增的验证检查（从 5 项加固到 7 项）正是来自这个闭环。完整报告见 [EVALUATION.md](EVALUATION.md)。

因为自己在实际场景里用得非常好，所以把它沉淀成可复用的技能并开源。**使用 Kimi K3 构建。** 🌒

## 🙌 致谢

- **作者**：Big Stephen——需求、真实场景测试
- **共同作者**：Kimi K3 Agent Swarm，由 [Moonshot AI](https://www.moonshot.cn/) 出品（[@MoonshotAI](https://github.com/MoonshotAI) · [Kimi-K3](https://github.com/MoonshotAI/Kimi-K3)）——实现、验证、打包

## 📄 许可证

[MIT](LICENSE)——随意使用，保留署名即可。

## 🔖 关键词

`docx` `修订模式` `track-changes` `word对比` `红线` `文档比较` `ooxml` `python` `kimi` `kimi-k3` `moonshot-ai` `agent-skill` `ai写作` `diff工具` `word文档` `修订追踪`
