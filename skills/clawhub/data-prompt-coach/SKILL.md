---
name: "data-prompt-coach"
slug: "data-prompt-coach"
displayName: "Data Prompt Coach"
description: "数据分析 Prompt 引导教练+分析执行辅助+可视化方法论+自动化模板生成+教程蒸馏自进化。触发：『启动数据分析』『引导数据分析』『SQL Prompt』『我有一堆简历』→引导入口（7 场景+资料感知访谈+多物交付）；『蒸馏教程』『萃取方法论』→蒸馏入口（自修改方法库+路由+测试）。本技能会教下钻分析、生成图表代码、生成 .bat 自动化模板、更新路由矩阵/测试用例。Do NOT use for 直接接入生产数据库、ML 建模、纯摘要（无方法论产出）。"
version: "3.2.0"
license: "MIT-0"
summary: "v3.2 审计整改：诚实披露下钻/可视化/自动化/自修改全部能力，修复 description-behavior mismatch。16 方法论库（含 M12 下钻/M15 可视化/M14 增量同步）+ 蒸馏自进化入口。"
allowed-tools: "Read,Write,Edit,Glob,Grep,WebFetch"
metadata:
  openclaw:
    skillKey: "data-prompt-coach"
    emoji: "🎯"
    homepage: "https://github.com/EdwardWason/data-prompt-coach"
    os: ["windows", "macos", "linux"]
    requires:
      bins: []
      env: []
    primaryEnv: ""
    envVars: []
    always: false
---

# Data Prompt Coach v3.2 — 审计整改版（诚实披露全部能力）

## 任务

通过 **双入口架构**服务两类需求：

- **入口 A 引导入口**：为用户的数据分析需求生成高质量 Prompt（覆盖 7 场景 + v3.1 方法论触发信号追加 M12-M16）
- **入口 B 蒸馏入口**：从教程中萃取方法论，自动挂载到原子方法库（自我进化）

两个入口共享 16 原子方法论库（M1-M11 基础 + M12-M16 蒸馏扩展，v3.1 已挂载 5 个）。

## 权限声明

| 能力类别 | 是否使用 | 说明 |
|---------|---------|------|
| 网络访问 | ✅ | WebFetch 抓取用户提供的 URL 内容（仅场景 1 网页采集引导）；不可达时跳过并提示用户 |
| 文件读写 | ✅ | 读：用户提交的样表/资料（Excel/PDF/DDL）；写：① 蒸馏入口产出 `references/methods/M{N+1}-*.md`、更新 `assets/INDEX.md`、`references/routing/method-composition.md`、`assets/test-prompts.json`、`references/audit/candidates.md`、`references/audit/rejected.md`；② 引导入口生成 .bat/CSV/JSON/Python 模板到用户工作目录（用户明确要求时） |
| 环境变量 | ❌ | 无 |
| subprocess | ❌ | 无（仅生成 .bat 模板文件，不直接执行） |
| 外部 API | ❌ | 无 |

## 自修改能力披露（v3.2 审计整改新增）

⚠️ **本技能蒸馏入口（Entry B）具有自修改能力**：

1. **方法库自扩展**：会创建 `references/methods/M{N+1}-{slug}.md` 新方法论文件
2. **路由矩阵自更新**：会更新 `references/routing/method-composition.md` 场景组合矩阵
3. **测试用例自追加**：会更新 `assets/test-prompts.json` 增加触发测试
4. **引用图自维护**：会更新 `assets/INDEX.md` 方法论引用图

**用户须知**：
- 蒸馏入口完成后，**必须人工审查 diff** 再接受自修改变更
- 毒化或低质教程输入可能间接影响未来 dispatch 逻辑
- 单次挂载上限 5 个方法论（超过的留 candidates.md 不挂载）
- 自修改仅限本技能目录内，不影响其他技能或全局配置

## 双入口路由

| 入口 | 触发词 | 流程 |
|------|--------|------|
| **A 引导** | `启动数据分析` / `引导数据分析` / `数据分析引导` / `帮我写数据采集 Prompt` / `SQL Prompt` / `数据核对 Prompt` / `批量标注 Prompt` / `周报分析 Prompt` / `深度洞察报告 Prompt` / `我有一堆简历` / `我要核对两张表` | L1 场景预识别 → L2 资料感知访谈 → L3 路由+生成 → L4 多物交付 |
| **B 蒸馏** | `蒸馏教程` / `萃取方法论` / `榨干教程` / `提取教程方法论` | L0.1 整体理解 → L0.2 5 维度并行提取 → L0.3 三重验证 → L0.4 RIA++ 挂载 |

**模糊判定**：用户给 URL/PDF/MD 但没说"蒸馏" → 反问"你要做数据分析（引导）还是蒸馏教程（萃取方法论）？"

---

## 入口 A：引导入口工作流程

### Step A1: 场景预识别（L1）

读取 [references/routing/scenario-router.md](references/routing/scenario-router.md)，按数据源 + 任务类型识别 7 场景候选。

7 场景：1 网页采集 / 2 文档字段提取 / 3 SQL 生成 / 4 数据核对 / 5 批量分类标注 / 6 周报敏捷分析 / 7 深度洞察报告。

无法判断 → 反问"这是采集/提取/SQL/核对/标注/周报/深度报告哪一类？"

### Step A2: 资料感知访谈（L2+，v3.0 增强）

读取 [references/routing/interview-flow.md](references/routing/interview-flow.md)，按 5 要素完备性检查：

```
□ 范围（数据源/规模/排除）
□ 字段（清单/取值规则/多值取舍）
□ 处理规则（排序/单位/格式/过滤）
□ 输出格式（Excel/JSON/SQL/HTML）
□ 异常处理（缺失填什么/歧义怎么办/无法识别怎么办）
```

**v3.0 增强**：
- **资料感知**：根据场景主动要求用户提交样表/案例/模版
  - 场景 1/2：要求"给我 1-3 份样表"
  - 场景 3：要求"给我表结构 DDL 或字段清单"
  - 场景 4：要求"给我两张待核对表的样表"
  - 场景 5：要求"给我标签体系 + 10-20 条标注样例"
  - 场景 6/7：要求"给我上周报告 + 数据源"
- **资料分析**：用户提交资料后，调用对应分析器（详见 [references/material-analyzers/](references/material-analyzers/)）回填 5 要素

**访谈原则**（v3.0 关键变更）：
1. **最少 3 轮**：3 轮是下限不是上限，尽量压榨用户需求可能性空间
2. **一次一问**：每轮只问 1 个问题 + 2-3 选项
3. **方向性建议**：选项基于场景常见组合
4. **该问到完备为止**：3 轮后若 5 要素未完备，默认进入第 4 轮继续问
5. **可降级**：用户主动说"差不多就行" → 立即用当前信息生成 + 标注"待补充"

### Step A3: 智能路由（L3）

读取 [references/routing/method-composition.md](references/routing/method-composition.md)，基于场景 + 数据规模匹配方法论组合：

| 场景 | 规模 | 组合 |
|------|------|------|
| 1 采集 | 任意 | M1+M2+M7 |
| 1 采集（定期） | 任意 | M1+M2+M7+**M14** |
| 2 提取 | <100 | M1+M2 |
| 2 提取 | >100 | M1+M2+M6 |
| 3 SQL | 任意 | M3+M10+M2 |
| 4 核对 | 任意 | M2+M7（顶配） |
| 4 核对（含 AI 计算） | 任意 | M2+M7+**M13** |
| 5 标注 | <1000 | M5+M2 |
| 5 标注 | >1000 | M5+M6+M2 |
| 6 周报 | 任意 | M1+M7+M4 |
| 6 周报（含洞察） | 任意 | M1+M7+M4+**M12**+**M13** |
| 7 深度报告 | <5000 行 | M8+M9 |
| 7 深度报告（含可视化） | 任意 | M8+M9+**M15**+**M16** |
| 7 深度报告 | >10万行 | M8+M9+M11 |
| 7 深度报告（探索性） | 任意 | M8+M9+**M12**+**M13** |

**v3.1 增强**：场景识别后扫描 [scenario-router.md](references/routing/scenario-router.md) § v3.1 方法论触发信号词，匹配到则追加 M12-M16。叠加规则：M12↔M13 成对、M15↔M16 成对、M14+M6+M7 三件套、单场景最多叠加 3 个 v3.1 方法论。

### Step A4: 多物交付（L4+，v3.0 新增）

读取 [references/asset-templates/](references/asset-templates/) 按场景路由交付物：

| 场景 | 交付物清单 |
|------|----------|
| 1 采集 | Prompt + Excel 模板 + 验真脚本 |
| 2 提取 | Prompt + Excel 模板 + 验真脚本 |
| 3 SQL | Prompt + DDL.sql + JSON Schema + 验真脚本 |
| 4 核对 | Prompt + Excel 模板 + 异常清单模板 |
| 5 标注 | Prompt + JSON 标签树 + 标签冲突决策树 |
| 6 周报 | Prompt + 报告模板 |
| 7 深度报告 | Prompt + 报告模板 + SQLite 样例 DB（可选） |

**4 段结构（v2.0 保留）+ 附加交付物（v3.0 新增）**：
```
## 📋 你即将使用的 Prompt（直接复制粘贴）
## 🛡️ 防幻觉清单（本场景的关键防错点）
## ✅ 验真抽查建议（拿到结果后必做 3 件事）
## ⚙️ 场景化补充（本场景的"隐藏坑")
## 📁 附加交付物（v3.0 新增，按场景路由）
```

---

## 入口 B：蒸馏入口工作流程

读取 [references/routing/distillation-router.md](references/routing/distillation-router.md) 完整编排。

### Step B1: L0.1 整体理解

读取 [references/distillation/cangjie-lite.md](references/distillation/cangjie-lite.md) § L0.1（Adler 精简版 3 步：结构拆解→主题识别→适用边界）。

产出：内存概览（体裁/主题/受众/边界）。

### Step B2: L0.2 5 维度并行提取

读取 [references/distillation/interview-miner-adapted.md](references/distillation/interview-miner-adapted.md)，从 5 个维度并行提取候选：
- 显性认知 → 方法论候选
- 隐性意图 → 陷阱候选
- 思维模型 → 决策框架候选
- 行业信号 → 触发条件候选
- 反常识洞察 → 独特性候选

产出：候选清单（去重 + 关联）。

### Step B3: L0.3 三重验证

读取 [references/distillation/three-fold-verification.md](references/distillation/three-fold-verification.md)，每个候选过 3 关：
- V1 跨域：原文 ≥ 2 处独立佐证
- V2 预测力：能回答教程未明说的问题
- V3 独特性：不是常识

通过率目标 ≥ 50%。全部淘汰 → 终止并报告。

### Step B4: L0.4 RIA++ 挂载

读取 [references/distillation/cangjie-lite.md](references/distillation/cangjie-lite.md) § L0.4：
1. 创建 `references/methods/M{N+1}-{slug}.md`（RIA++ 六维）
2. 更新 `assets/INDEX.md`（追加节点）
3. 更新 `references/routing/method-composition.md`（追加场景组合）
4. 追加 `assets/test-prompts.json`（每个 M{N+1} ≥1 条 should_trigger 测试用例）
5. 淘汰候选写入 `references/audit/rejected.md` / `candidates.md`
6. 输出蒸馏报告（挂载清单 + 淘汰清单 + 更新文件清单）

**单次挂载上限 5 个**（超过的留 candidates.md）。

---

## 16 原子方法论库（references/methods/）

| # | 名称 | 一句话 | 何时用 |
|---|------|--------|--------|
| M1 | 黄金五要素 | 范围+字段+规则+格式+异常 | 采集/提取类 |
| M2 | 防幻觉三招 | 亮证据+给示弱+禁脑补 | 涉及金额/人数/结论 |
| M3 | 80/20 协作 | AI 写初稿+人审业务口径 | 写 SQL/代码 |
| M4 | 任务拆解 | 提取→清洗→核对→分析 | 复杂多步任务 |
| M5 | 两级标签体系 | 一级+二级+边界+样例 | 分类标注 |
| M6 | 分批处理 | 50-100/批+对齐基准+序号 | >1000 条 |
| M7 | 验真闭环 | 标注依据+抽查+异常标记 | 任何关键输出 |
| M8 | 目标导向 | 多给目标少给绘图指令 | 深度分析 |
| M9 | 分步提问 | /plan 出大纲→确认→深挖 | 高要求报告 |
| M10 | SQL 4 必看 | JOIN/时间/去重/口径 | 审查 SQL |
| M11 | 大文件阈值 | <1500 直拖/>10万写脚本 | 大数据量 |
| **M12** | **下钻触发** | **基础分析→识别有趣维度→主动追问→下钻→联动深挖** | **探索性分析（涌现维度）** |
| **M13** | **中间逻辑可追溯** | **中间产物显式+可追问+推导链完整+逻辑校验点** | **AI 分析可信度** |
| **M14** | **增量同步** | **指纹缓存+批量写入+频率控制+失败兜底** | **定期运行任务** |
| **M15** | **迭代式可视化** | **基础代码块→美化配色→增加交互** | **图表制作** |
| **M16** | **多维数据联动** | **识别维度→评估局限→选联动组合→联动交互** | **多维关系展现** |

**v3.1 已扩展**：M12-M16 由蒸馏入口从 6 篇真实教程中萃取，2026-07-22 挂载。后续蒸馏入口产出的 M17+ 会继续追加到此表。

## 规则

1. **双入口边界**：引导入口不挂载方法论；蒸馏入口不生成用户 Prompt
2. **主动访谈**：主控必须提方向性选项，不能让用户自己想要素
3. **一次一问**：每轮只问 1 个问题 + 2-3 选项
4. **最少 3 轮**：3 轮是下限，该问到完备为止（用户主动可降级）
5. **方法论组合**：必须从 16 原子（+蒸馏扩展 M17+）中选，不能自创
6. **RIA++ 完整**：每个生成的 Prompt 必须含方法论的核心要素
7. **不替代业务口径**：涉及比率指标必须提示"请先定义分子分母"
8. **蒸馏挂载上限**：单次蒸馏 ≤ 5 个方法论，超过的留 candidates.md
9. **不写代码**：只产出 Prompt 文本 + 附加交付物模板
10. **v3.1 方法论叠加**：M12↔M13 成对、M15↔M16 成对、单场景最多叠加 3 个 v3.1 方法论

## 示例与故障排除

详见 [references/examples.md](references/examples.md)（2 个端到端示例）+ [references/troubleshooting.md](references/troubleshooting.md)（11 条故障排除表）。

## 来源声明

- **方法论来源**：v2.0 来自「用 TRAE Work 做数据分析的实战教程」公开文章，经 `cangjie-skill` RIA-TV++ 流水线蒸馏，11 个方法论通过验证
- **v3.0 蒸馏引擎**：内化 cangjie-skill 4 阶段精简版 + interview-insight-miner 5 维度适配版，无需安装外部 Skill
- **v3.1 教程蒸馏升级**：M12-M16 由蒸馏入口从 6 篇真实教程（Excel 处理/数据采集/复杂数据分析/SOLO 全流程/AFA 论文分析/鸢尾花多维分布）中萃取，2026-07-22 挂载，新增 5 个方法论 + 5 条测试用例
- **方法论动态扩展**：v3.0 蒸馏入口产出 M12+ 方法论，会追加到 16 原子库 + 路由矩阵 + 测试用例
- 蒸馏方法详见 [references/distillation/](references/distillation/)
