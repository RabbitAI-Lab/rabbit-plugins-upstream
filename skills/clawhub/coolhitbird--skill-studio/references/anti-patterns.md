# Anti-Patterns（反模式 11 项实证清单）

> 诊断已有 skill 病灶时对照此表。每项对应 `audit.py` 一个检查项。
> **实证不写死本地路径**——具体 skill 名/KB 大小不写入可分发文档（安全考量）。

---

## 反模式速查表

| # | 反模式 | 严重度 | audit.py 检查项 |
|---|---|---|---|
| 1 | 巨型 prompt 反巨型 prompt | ERROR | skill_md.too_long |
| 2 | description 写成简介不是路由条件 | WARNING | description.not_route |
| 3 | SKILL.md 塞设计哲学 | WARNING | skill_md.philosophy |
| 4 | 强制力靠词汇不靠脚本 | INFO | skill_md.verbal_force |
| 5 | references/ 建了未引用 | WARNING | references.unused |
| 6 | .gitkeep 残留 | WARNING | dir.*.gitkeep_residual |
| 7 | __pycache__ 入包 | WARNING | scripts.pycache_residual |
| 8 | description 占位符未填 | ERROR | description.placeholder |
| 9 | 缺 agent_created 字段 | WARNING | frontmatter.agent_created.missing |
| 10 | name 与目录名不一致 | ERROR | name.mismatch |
| 11 | 寒暄词/第一人称 | INFO | skill_md.pleasantry |

---

## 详细反模式

### 1. 巨型 prompt 反巨型 prompt（ERROR）

**症状**：SKILL.md 超 600 行，把所有详节塞进正文。

**后果**：挤占对话历史预算，长对话模型"失忆"；元技能自身违反它教的"详节挪 references/"规范。

**实证**：某编排器类 skill 实测 21.6KB ≈ 600+ 行，是重灾区典型。某"反巨型 prompt"指南自身写成巨型 prompt——元技能违反自身规范是最讽刺的反模式。

**修复**：拆 `references/`，正文压到 ≤500 行，只留索引+编排。`audit.py` 检查项 `skill_md.too_long`。

---

### 2. description 写成简介不是路由条件（WARNING）

**症状**：description 缺"当用户提及[关键词]时使用"类触发公式，写成"这是一个 XX 工具"。

**后果**：description 是 metadata 常驻上下文，决定 skill 何时被激活。写成简介→模型不知道何时触发，触发率下降或撞车。

**实证**：marketplace 版 skill-creator 的 description 用 "This skill should be used when..." 公式，是正面教材。反面是写成"一个帮助创建技能的工具"——缺触发条件。

**修复**：用公式 `动词+做什么+何时用`，加"当用户提及[关键词]或[场景]时使用"。`audit.py` 检查项 `description.not_route`。

---

### 3. SKILL.md 塞设计哲学（WARNING）

**症状**：正文含"本质是""哲学""为什么这么设计""概念辨析"等词。

**后果**：SKILL.md 是工作指令不是论文。哲学层挤占执行预算，Agent 读哲学不读指令。

**实证**：早期 SOP 草稿把"Skill 与 Tool 辨析"哲学层塞进 SKILL.md，被铁律第 5 条纠正——挪 `references/architecture.md`。

**修复**：哲学层移到 `references/architecture.md`，SKILL.md 只留"何时用/标准流程/铁律/资源索引"。`audit.py` 检查项 `skill_md.philosophy`。

---

### 4. 强制力靠词汇不靠脚本（INFO）

**症状**：SKILL.md 写"MUST reject""必须拒绝""一定要"等措辞，指望模型听话。

**后果**：模型会善意推定，"MUST reject" 在 prompt 里靠不住。只有 `validate.py` 真跑校验才是硬钳。

**实证**：marketplace 版 skill-creator 用 prompt 措辞强制，本元技能用 `validate.py` 真校验——这是两者根本差异。

**修复**：措辞可保留（提示用），但强制力必须落到 `scripts/validate.py`。`audit.py` 检查项 `skill_md.verbal_force`（INFO 级，提示而非阻断）。

---

### 5. references/ 建了未引用（WARNING）

**症状**：建了 `references/foo.md` 但 SKILL.md 资源索引表没提。

**后果**：渐进式披露失效——Agent 不知道何时加载该文件，文件成孤儿。

**实证**：早期 init 生成的占位 references 未及时删/填，残留成孤儿。

**修复**：在 SKILL.md 资源索引表加引用，或删未用文件。`audit.py` 检查项 `references.unused`。

---

### 6. .gitkeep 残留（WARNING）

**症状**：`init_skill.py` 生成 `.gitkeep` 占位，填完内容后没删。

**后果**：`.gitkeep` 入包是噪音；空目录该删不该留。

**修复**：填内容后删 `.gitkeep`。`audit.py` 检查项 `dir.*.gitkeep_residual`。

---

### 7. __pycache__ 入包（WARNING）

**症状**：`scripts/__pycache__/` 残留，打包时入 zip。

**后果**：污染包体积，泄露本地 Python 版本信息。

**修复**：删 `__pycache__`，加 `.gitignore`。`audit.py` 检查项 `scripts.pycache_residual`。`package_skill.py` 已跳过 `.gitkeep`，建议也跳 `__pycache__`。

---

### 8. description 占位符未填（ERROR）

**症状**：description 含 `[TODO]`、`[动词]`、`[关键词]`、`placeholder` 等占位符。

**后果**：description 是路由条件不是简介，占位符=没写 description，触发完全失效。

**实证**：`init_skill.py` 生成的模板含 `[TODO: 动词开头...]`，曾发生填完 SKILL.md 正文但忘改 description 占位符，导致 `validate.py` 报 ALL PASS（已修补加占位符检测）。

**修复**：用公式填实际值。`audit.py` 检查项 `description.placeholder`（ERROR 级，拒出包）。

---

### 9. 缺 agent_created 字段（WARNING）

**症状**：frontmatter 没 `agent_created: true`。

**后果**：SkillManage 无法修改/删除此 skill（仅能管 `agent_created: true` 的）。

**修复**：加 `agent_created: true`。`audit.py` 检查项 `frontmatter.agent_created.missing`。

---

### 10. name 与目录名不一致（ERROR）

**症状**：frontmatter `name: foo-bar` 但目录名 `foo_bar` 或 `foobar`。

**后果**：加载机制按目录名索引，name 不一致导致找不到或重复加载。

**修复**：name 必须与目录名完全一致（小写+连字符）。`audit.py` 检查项 `name.mismatch`。

---

### 11. 寒暄词/第一人称（INFO）

**症状**：SKILL.md 含"好问题""很高兴帮你""我来为你"等寒暄，或用第一人称"我"。

**后果**：SKILL.md 面向 Claude 写作，祈使句+第三人称，不寒暄（铁律第 12 条）。寒暄挤占预算且不符角色。

**修复**：删寒暄，直接给指令。`audit.py` 检查项 `skill_md.pleasantry`（INFO 级，提示而非阻断）。

---

## 使用方法

```bash
# 诊断已有 skill
python scripts/audit.py <skill-folder>

# 只看 ERROR 级（发布前快速过）
python scripts/audit.py <skill-folder> --severity error

# JSON 输出（供脚本消费）
python scripts/audit.py <skill-folder> --json
```

**与 validate.py 的分工**：

| 工具 | 时机 | 检查项数 | 退出码语义 |
|---|---|---|---|
| validate.py | 发布前硬钳 | 7 项（少而精） | 1=拒出包 |
| audit.py | 诊断已有 skill | 11+ 项（多而广） | 1=有 ERROR 级病灶 |

**典型流程**：重构已有 skill → 跑 `audit.py` 拿病灶清单 → 按清单修复 → 跑 `validate.py` 硬钳确认 → `package_skill.py` 打包。

---

## 已知启发式误报（不阻断，仅提示）

audit.py 用关键词匹配，无法区分"规则描述里的词"和"内容本身"，以下为已知误报：

| 检查项 | 误报场景 | 为何不修 |
|---|---|---|
| `skill_md.philosophy` | 铁律描述含"哲学"二字（如"设计哲学不进 SKILL.md"） | 规则名无法回避，WARNING 级不阻断 |
| `skill_md.verbal_force` | 引用案例含 "MUST reject"（如描述 marketplace 版弱点） | 引用非自身使用，INFO 级不阻断 |
| `scripts.pycache_residual` | 跑 audit/validate 时 Python 自动生成 __pycache__ | 运行副作用，加 .gitignore + package 跳过即可 |

**误报处理原则**：audit.py 是诊断报告不是硬钳，WARNING/INFO 级误报可忽略；ERROR 级误报（理论上不会发生，因 ERROR 检查项是精确匹配）才需修工具。
