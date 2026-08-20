---
name: "paper-reader"
description: "论文阅读入库全流程：DOI/PDF → JARVIS初稿 → Codex价值评估+精读 → Kimi Code review → commit/push"
---

# Paper Reader — 论文阅读入库流程

## 触发方式

用户发来以下任一格式：
```
读论文，DOI: 10.xxxx/xxxxx
读论文，arXiv: 2301.12345
读论文，PDF: /path/to/paper.pdf
```

**可选 flag：**
- `--精读`：跳过 Codex 价值评估，直接进入精读补充流程
- `--重排`：触发 CODEX_DEEP_READ.md 的 Tier 全面重排（默认只追加）

**启动知会：** 每次触发此 Skill 时，必须先回复用户：
```
📄 启动论文入库流程：[标题或入口标识]，模式：[精读/自动评估]，来源：[DOI/arXiv/PDF]
```

---

## 流程图

```
DOI / arXiv / PDF 入口
    ↓
[0] 查重 → 重复？→ 终止，提示文件路径
    ↓
[1] 获取论文元数据（标题、作者、期刊、摘要）
    ↓  ← 失败即终止
[2] JARVIS 生成初稿 .md → 存入仓库对应分类
    ↓
[3] Codex 价值评估 ← 若有 --精读 flag 则跳过
    ↓              ↓
  精读(≥3)    粗读(<3) → JARVIS 标记粗读 → 写文件 → commit/push → 结束
    ↓
[4] Codex 精读补充（公式/代码梳理）
    ↓
[5] JARVIS 更新 CODEX_DEEP_READ.md
    ↓  (默认追加；若 --重排 则全面重排 Tier)
[6] Kimi Code review（公式推导/代码流程/语法/逻辑/提问）
    ↓
[7] JARVIS git commit + push → 完成通知
```

**状态追踪：** 每个步骤完成后，JARVIS 更新 paper.md 中的状态标签：
```markdown
**流程状态：** ①元数据 ✓ | ②初稿 ✓ | ③评估 ✓(精读) | ④补充 ✓ | ⑤索引 ✓ | ⑥review ✓ | ⑦提交 ⏳
```

断点恢复：若流程中断，下次触发时 JARVIS 读取状态标签，从最后未完成的步骤继续。

---

## 详细步骤

### Step 0：查重

在 `<你的论文库路径>/` 中搜索：
- 同名文件（标题相近）
- 相同 DOI（全文搜索）
- 相同 arXiv ID

若重复 → 提示 Doctor"该论文已存在：[文件路径]"，**终止流程**。

### Step 1：获取论文元数据

**DOI 入口：**
- 使用 `web_fetch` 访问 `https://doi.org/10.xxxx/xxxxx`
- 提取：标题、作者、期刊名、出版日期、Abstract
- 若 DOI 链接失效 → **立即终止**，提示 Doctor"DOI 不可访问：<URL>"

**arXiv 入口：**
- 使用 `web_fetch` 访问 `http://export.arxiv.org/api/query?id_list=<arxiv_id>`
- 解析 XML 获取：标题、作者、Abstract、分类
- 若 arXiv API 无响应 → 提示 Doctor 后终止

**PDF 入口：**
- 使用任意 PDF 提取工具（`pdftotext` / `pdfplumber` / 其他）提取文本
- 从文本中识别：标题、作者、Abstract、Conclusion
- 若 PDF 无法提取文字 → **立即终止**，提示 Doctor"PDF 无法提取文字，可能需要 OCR 或人工处理"

### Step 2：JARVIS 生成初稿

**分类判断：**
- 根据论文主题判断所属分类（对应仓库现有目录）
- 若不属于任何现有分类 → 新建目录，命名规范：小写英文，连字符分隔
- 文件命名：英文小写 + 连字符，尽量与原论文标题一致

**初稿模板（写入 paper.md）：**

```markdown
# [论文标题（中英双语）]

**作者：** [Author Names]
**期刊：** [Journal Name, Year]
**DOI：** [https://doi.org/10.xxxx/xxxxx](https://doi.org/10.xxxx/xxxxx)
**arXiv：** [https://arxiv.org/abs/xxxx.xxxxx](https://arxiv.org/abs/xxxx.xxxxx) （如有）
**阅读状态：** ⏳ 待评估
**流程状态：** ①元数据 ✓ | ②初稿 ⏳ | ③评估 ⏳ | ④补充 ⏳ | ⑤索引 ⏳ | ⑥review ⏳ | ⑦提交 ⏳

---

## 摘要

### 中文翻译
[Abstract 的中文翻译]

### 原文
> [Original Abstract]

---

## 文章总结

### 1. 解决什么问题？
[一句话描述核心问题]

### 2. 用了什么方法论？
[核心方法/框架/技术路线]

### 3. 主要结论是什么？
[关键发现和结果]

---

## 价值评估
⏳ 待 Codex 评估

## 公式与代码梳理
⏳ 待精读补充

## Review Questions
⏳ 待 Kimi Code review
```

存入路径：`<你的论文库路径>/<分类>/<文件名>.md`
完成后更新状态标签：`②初稿 ✓`

### Step 3：Codex 价值评估

**调用 Codex** (`codex exec -s workspace-write`) 进行评估。

**Codex 任务：**
1. 读取 paper.md 初稿
2. 阅读仓库 `README.md` 了解 用户的研究方向
3. 浏览 `CODEX_DEEP_READ.md` 了解当前论文库结构和价值体系
4. **只输出评估文本**，不要直接写文件，不要操作 git

**价值判断标准（6 级）：**

| 级别 | 标准 | 判定 |
|------|------|------|
| 1 | 有清晰且令人信服的 idea | 精读门槛 |
| 2 | 有简单明了的计算结果 | — |
| 3 | 有强大的预言能力 | ≥3→**精读** |
| 4 | 达到 Editor's Pick 水平 | — |
| 5 | 方法新颖，填补领域空白 | — |
| 6 | 来自顶会/顶刊 + 高引用 | 加权加分 |

**JARVIS 根据 Codex 输出判断：**

**粗读（< 级别 3）：**
- 将"阅读状态"改为 `📖 粗读`
- 将 Codex 评价写入"价值评估"小节
- 删除"公式与代码梳理"和"Review Questions"占位符
- 更新状态标签
- **直接跳到 Step 7（commit/push）**

**精读（≥ 级别 3）：**
- 将"阅读状态"改为 `🔬 精读`
- 将 Codex 评价写入"价值评估"小节
- 更新状态标签：`③评估 ✓(精读)`
- 进入 Step 4

**若已传 `--精读` flag：**
- 跳过 Codex 评估
- 直接标记为 `🔬 精读`
- 在"价值评估"写入"用户指定精读"
- 进入 Step 4

### Step 4：Codex 精读补充

**调用 Codex** 进行精读补充。

**Codex 任务：**
1. 读取 paper.md
2. 详细梳理文章的公式推导（逐公式解释数学逻辑）
3. 梳理涉及的代码/算法流程
4. **只输出补充文本**，不要直接写文件，不要操作 git

**JARVIS 操作：**
- 将 Codex 输出的内容写入 paper.md 的"公式与代码梳理"小节
- 更新状态标签：`④补充 ✓`

### Step 5：JARVIS 更新 CODEX_DEEP_READ.md

**默认行为（无 `--重排` flag）：**
1. 将新精读论文追加到 Tier 3 末尾
2. 检查阅读路线图是否需要微调（新增小点）
3. 更新 token 统计（如有）

**若传了 `--重排` flag：**
1. 全面重新评估所有精读论文的 Tier 1/2/3 排名
2. 重写阅读路线图
3. 更新 token 统计

**链接格式：**
```markdown
N. **论文标题** — 分类
   - 文件：[`path/to/file.md`](path/to/file.md)
   - 数理基础：[简述]
   - 为什么精读：[简述与库内其他论文的关联]
```

更新状态标签：`⑤索引 ✓`

### Step 6：Kimi Code Review

**调用 Kimi Code** 参考下方『Kimi Code 调用方式』小节（具体 CLI 参数以你本地工具版本为准）。

**Prompt 要求 Kimi Code：**
1. 读取新精读文档 paper.md
2. 检查公式推导有无错误
3. 检查代码流程有无逻辑问题
4. 检查语法和 markdown 格式
5. 检查文档逻辑是否连贯
6. 结合现有科研内容，提出 3 个深入问题

**Kimi Code 调用方式（参考 TOOLS.md）：**
```bash
# 1. 写 prompt 到 temp 文件
# 2. 启动 kimi --yolo --add-dir <workspace> (pty:true, background:true)
# 3. paste "请读取 <prompt_file> 并执行"
# 4. send-keys Enter
# 5. poll 监控
```

**Kimi Code 完成后 JARVIS：**
- 确认 Review Questions 已追加到文档末尾
- 确认公式/语法问题已修复
- 更新状态标签：`⑥review ✓`

### Step 7：JARVIS 提交

```bash
cd ~/agent-workspace/Projects/Papers_matters
git add -A
git commit -m "paper: add <论文简称> (<精读|粗读>)"
git push
```

更新状态标签：`⑦提交 ✓`

**完成通知：**
```
✅ 论文入库完成：《标题》
   📂 分类：<分类>
   📖 状态：<精读/粗读>
   🔗 CODEX_DEEP_READ.md 已更新（精读时）
   📝 <文件路径>
```

---

## ⚠️ Codex 关键约束

Codex 在流程中**只负责生成文本内容**（评估意见、精读补充），**不**直接操作文件或 git。所有文件写入和 git 操作由 JARVIS 完成。这是因为 Codex sandbox 对 `.git` 目录有只读限制。

Codex 调用格式：
```bash
# 如网络需要代理，先 export HTTP_PROXY/HTTPS_PROXY 环境变量，再调用 && \
codex exec -s workspace-write - < "$PROMPT_FILE"
```

## 异常处理

| 异常 | 处理 |
|------|------|
| DOI 不可访问 | 终止 → 提示 Doctor |
| arXiv API 无响应 | 终止 → 提示 Doctor |
| PDF 无法提取文字 | 终止 → 提示 Doctor |
| 论文已存在 | 终止 → 提示文件路径 |
| Codex/Kimi Code 调用失败 | 最多重试 1 次 → 若仍失败，终止并提示 Doctor |
| 流程中断 | 下次启动读取状态标签，断点续跑 |

## 注意

- 所有公式使用 `\[...\]` display math 格式（GitHub 兼容）
- 每次触发 Skill 先发启动知会给 Doctor
- 精读文档自动进入 CODEX_DEEP_READ.md 索引
- 粗读文档仅存笔记，不进入索引
