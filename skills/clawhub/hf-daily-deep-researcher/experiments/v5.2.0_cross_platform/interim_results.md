# v5.2.0 跨平台兼容性对比实验 — 初步测试结果

**实验时间**: 2026-07-29 16:15 ~ 进行中
**测试平台**: Kimi / OpenClaw

---

## 一、工具可用性实测结果

### 1.1 当前环境（Kimi / OpenClaw）

| 工具 | 搜索功能 | 获取论文全文 | 备注 |
|------|---------|-------------|------|
| **kimi_search** | ✅ 可用（语义搜索强） | N/A | 返回大量结果，含 GitHub 资源库等非 arXiv 来源 |
| **kimi_fetch** | N/A | ❌ 失败（ar5iv.org 返回 fetch failed） | 无法访问 ar5iv HTML 实验版 |
| **web_fetch** | ⚠️ arXiv API 报 500，HF 报 failed | ✅ 成功（arxiv.org/html/ 返回 9229 字正文） | arXiv 原生 HTML 版本可完整获取 |
| **browser** | 未测试 | 未测试 | — |

### 关键发现

**发现 1：kimi_fetch 在当前 Kimi 平台上无法访问 ar5iv.org**
- 测试 URL: `https://ar5iv.org/html/2607.04713`
- 结果: "Failed to fetch URL due to network error: fetch failed"
- 影响: 之前 Skill 中"优先使用 kimi_fetch 获取 arXiv HTML"的设计在当前平台不成立

**发现 2：web_fetch 可以获取 arXiv 原生 HTML 完整内容**
- 测试 URL: `https://arxiv.org/html/2607.04713`
- 结果: 成功返回 9229 字，包含摘要 + 正文前 3 节
- 优势: 内容完整，格式为 HTML，可被解析
- 局限: 有 10000 字符截断（maxChars 参数限制）

**发现 3：arXiv API（export.arxiv.org/api/query）报 500 错误**
- 可能原因: URL 编码问题、服务器负载、或网络策略限制
- 影响: web_fetch 方案不能依赖 arXiv API，需要改用 arxiv.org/html/ 直接获取

### 1.2 工具链修正建议

基于实测结果，工具优先级需要调整：

| 优先级 | 原设计 | 修正后 |
|--------|--------|--------|
| 1 | kimi_fetch → ar5iv | **web_fetch → arxiv.org/html/** |
| 2 | web_fetch → arXiv API | web_fetch → arxiv.org/abs/（摘要） |
| 3 | browser 兜底 | browser 兜底 |

---

## 二、方案 A 搜索结果（kimi_search）

### 2.1 搜索查询执行
- 查询 1: `site:arxiv.org credit assignment OR agentic RL 2026-07-22..2026-07-29` → 返回 8-10 篇论文（日期过滤未生效）
- 查询 2: `arxiv 2607 credit assignment OR agentic reinforcement learning OR GRPO OR process reward` → 返回 GitHub 资源库 + 综述
- 查询 3: `arxiv 2607.04 OR 2607.05 OR 2607.06 OR 2607.07 agent OR RL OR credit` → 返回综述详细内容

### 2.2 找到的论文

**2026 年 7 月论文（仅 1 篇）**：
- arXiv:2607.04713 — "Reward-Swap Policy Optimization for Multi-Turn LLM Agents" (2026-07-06)

**非 7 月但高度相关论文（10 篇+）**：
- arXiv:2604.09459 — Credit Assignment 综述（2026-04）
- arXiv:2605.00425 — Agentic RL Credit Assignment（2026-05）
- arXiv:2603.21563 — CCPO/SEPO Multi-Agent（2026-03）
- arXiv:2605.30928 — HiMAQ Hierarchical（2026-05）
- arXiv:2602.03719 — Credit Assignment 方法分类（2026-02）
- arXiv:2601.21754 — SCOUT（2026-01）
- arXiv:2601.06794 — ECHO Co-Evolving Critics（2026-01）
- 等

**GitHub 资源库发现**：
- xxzcc/Awesome-Credit-Assignment-in-LLM-RL（2026.07 Refresh）
- 列出 9 篇 2026 年新论文（无明确 arXiv ID）

### 2.3 问题记录
- kimi_search 日期范围过滤语法未生效（`YYYY-MM-DD..YYYY-MM-DD` 不工作）
- 需要手动筛选日期

---

## 三、方案 B 搜索（进行中）

子 Agent `HF-Exp-PlanB-Search` 已启动，使用纯 web_fetch 搜索。
- 状态: running (已运行约 3 分钟)
- 超时: 600 秒

---

## 四、精读能力对比

### 4.1 论文全文获取

| 方案 | 工具 | 目标 URL | 结果 | 获取字数 |
|------|------|---------|------|---------|
| A | kimi_fetch | ar5iv.org/html/2607.04713 | ❌ 失败 | 0 |
| B | web_fetch | arxiv.org/html/2607.04713 | ✅ 成功 | 9229 字 |

**结论：在当前平台，web_fetch 是唯一可用的论文全文获取工具。**

### 4.2 内容质量

web_fetch 返回的 arxiv.org/html/ 内容包含：
- ✅ 完整摘要
- ✅ 正文各章节（Introduction、Related Work、Method 等）
- ✅ 图表引用（Figure 1, Figure 2）
- ✅ 公式（部分，LaTeX 源码格式）
- ⚠️ 被 maxChars 参数截断（10000 字符限制）
- ⚠️ 包含安全提示前缀（约 800 字外部内容声明）

---

## 五、待完成事项

1. [ ] 等待方案 B 子 Agent 完成搜索
2. [ ] 对比两方案搜索覆盖率
3. [ ] 用 web_fetch 精读 arXiv:2607.04713，对比 kimi_fetch（如果可用）
4. [ ] 生成最终对比报告
5. [ ] 修正 Skill 文档（deep_reader_prompt.md 等）

---

## 六、初步结论

### 6.1 跨平台兼容性状态

**绿色（可用）**：
- web_fetch 获取 arxiv.org/html/ ✅
- kimi_search 语义搜索 ✅

**黄色（有限）**：
- web_fetch arXiv API（500 错误）⚠️
- web_fetch HuggingFace Daily Papers（fetch failed）⚠️

**红色（不可用）**：
- kimi_fetch 访问 ar5iv ❌

### 6.2 对 Skill 设计的影响

1. **deep_reader_prompt.md** 需要修正：不应优先 kimi_fetch，应优先 web_fetch + arxiv.org/html/
2. **searcher_prompt.md** 需要修正：arXiv API 方案不稳定，应改用 arxiv.org 搜索 + 日期筛选
3. **SKILL.md** 需要更新工具链矩阵
