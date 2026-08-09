# 模块一：分层存储

### 即时层（≤20KB 总量，单文件上限之和等于总量上限）

即时层中 `USER.md`、`MEMORY.md`、`SOUL.md`、`TOOLS.md` 可在每次对话开始时加载为 Agent 的工作记忆。`SECRET.md` **不自动加载**，只允许在用户授权且确有需要时按 locator 读取对应秘密；文件本身也不得含明文秘密。

**容量上限一致性约束**：下方单文件上限之和精确等于 20KB(20480B)，不存在"单文件都满但总量超限"的歧义。若需调整任一文件上限，必须同步调整其他文件使求和仍为 20480B，或修订本节总量约束。

| 文件 | 职责 | 容量上限 | 写入工具 |
|------|------|----------|----------|
| USER.md | 用户画像：换项目仍成立的信息 | 2048B | edit_file |
| MEMORY.md | 规则 + 状态锚点 + 指针 | 5120B | edit_file |
| SOUL.md | 身份定义：性格、风格、关系 | 4096B | edit_file |
| TOOLS.md | 工具经验："用XX要注意YY" | 5120B | edit_file |
| SECRET.md | secret handle/locator + 脱敏元数据；不含秘密值 | 4096B | edit_file（按需，0600） |

（求和验证：2048 + 5120 + 4096 + 5120 + 4096 = 20480B = 20KB ✓）

**写入规则**：
- 即时层文件**只能用 edit_file 修改**，严禁 write_file 覆盖
- 更新已有内容用 `replace_one` / `replace_all`
- 新增内容用 `append` / `append_newline`
- 严格控制篇幅，超过上限时必须精简已有内容再追加

### SECRET 安全边界

以下均为硬规则：
- 禁止写入 API Key、密码、Token、私钥、cookie 或其他可直接使用的凭证值
- 只记录 `secret://provider/item` 一类 handle/locator，以及 owner、轮换日期、用途、last4 等脱敏元数据
- 创建后立即设置权限 `0600`；权限无法收紧时停止写入并报告阻塞
- 不自动加载到模型上下文，不加入 `recent_memory/index.json`，不进入 `memory_search`/RAG，不进入普通巩固或微巩固快照
- 需要凭证时由用户授权的 Host secret capability 解析 locator；本 skill 不读取或回显秘密值

#### 非模型可信本地 scanner 与迁移 helper

SECRET 内容检查属于 Host 控制面，不属于模型可见的普通 read-set。可信 scanner 必须在本地进程内按确定性规则读取 `SECRET.md` 字节，识别疑似明文凭证，同时把合法的 `secret://...` locator 与明确脱敏字段列入 allowlist；原始字节、匹配文本、上下文片段和可逆编码永不进入模型 payload、RAG、快照、日志或命令输出。

scanner 唯一允许返回的结构为：

```json
{
  "status": "clean_locator_only",
  "match_count": 0,
  "redacted_locations": []
}
```

- `status` 只允许 `clean_locator_only`、`plaintext_suspected`、`scanner_unavailable`、`scan_error`
- `match_count` 只返回非负整数；`redacted_locations` 只含 `rule_id`、行号和不可逆 column bucket，不含正文、捕获组、locator 或秘密 hash
- `plaintext_suspected` 必须阻塞普通操作并进入下方迁移；`scanner_unavailable`/`scan_error` 必须报告 capability gap `trusted_secret_scanner_required` 并阻塞，不能退化为模型读取
- `clean_locator_only` 仍需独立验证文件权限为 `0600`；权限失败同样阻塞
- scanner 运行完成后，Agent 只消费上述三字段；任何额外字段或非零匹配时的文本输出都视为 scanner 不可信

本技能提供的 `scripts/scan_secret.py` 和 `scripts/migrate_secret.py` 是**必须由 Host 作为可信本地控制面安装和执行**的参考 helper；模型不得读取 `SECRET.md`、不得代替 helper 拼接或输出秘密值。helper 不可用、权限不足、plan 与最新扫描不完全匹配，均按 `trusted_secret_scanner_required` 阻塞。

**旧部署明文迁移（五步，任一步失败即停止）**：
1. Host 运行 `python scripts/scan_secret.py --secret-file /absolute/path/SECRET.md`；Agent 只接收 status/count/redacted locations。scanner 不可用或输出越界时阻塞，绝不改由模型读取。
2. 提醒用户在对应提供方撤销/轮换旧凭证，并将新值存入其选择的 secret store。
3. 基于脱敏位置生成**不含秘密值**的 migration plan；每一项只含 `rule_id`、`line`、`locator` 与可选 `owner`、`purpose`、`last4`。每个 locator 必须以 `secret://` 开头。
4. 取得用户确认后，Host 运行 `python scripts/migrate_secret.py --secret-file /absolute/path/SECRET.md --plan /absolute/path/safe-plan.json --confirmed-by-user`。helper 在本地重新扫描、要求 plan 精确覆盖全部命中行、原子地把整行替换为 locator 元数据，并强制 `0600`；模型始终不可见旧值或新值。
5. helper 内部用同一 scanner 复查；只有返回 `migration_status: applied`、嵌套扫描结果为 `clean_locator_only` 且权限为 `0600` 才解除阻塞。仍命中、plan 失配、scanner 不可用或原子替换失败时不宣称迁移完成。

安全 migration plan 示例（可传给模型；其中没有秘密值）：

```json
{
  "replacements": [
    {
      "rule_id": "assignment_value",
      "line": 12,
      "locator": "secret://vault/production-api",
      "owner": "platform",
      "purpose": "production API",
      "last4": "1234"
    }
  ]
}
```

**唯一例外：巩固校验失败后的快照回滚**（见模块三/模块九）允许使用 `write_file` 整体覆盖即时层文件，前提是：
1. 必须从已校验的快照目录读取内容，不能凭空写
2. 必须按模块三写入 business write-set 外的 canonical 脱敏 audit projection，只记录 run-id、结果、路径不可逆标识与前后哈希
3. 回滚完成后立即恢复"严禁 write_file"约束

回滚是 write_file 禁令的**文档化例外**，不是日常写入路径。除此之外的任何 write_file 调用都违反硬规则。

**MEMORY.md 格式规范**：
```markdown
# 记忆记录

## 长期行为规则
- **粗体短标题**：规则内容
- **粗体短标题**：规则内容

## 核心状态锚点
- **粗体短标题**：状态描述（YYYY-MM-DD）
> 指针用代码块包裹，只放路径不重复内容
```

### 近中期层（按需加载）

即时层放不下的详细内容存放在 `recent_memory/` 目录。

**目录结构（模块一为近中期层与自我指涉目录的唯一权威定义源，其他模块只引用不新增）**：
```
recent_memory/
├── index.json          ← 所有记忆单元的目录（摘要 + 标签）
├── project/*.md        ← 项目进度快照
├── decision/*.md       ← 重要决策记录
├── todo/*.md           ← 待办事项
├── episodic/*.md       ← 情境记忆（具体事件/对话/操作的散点记录，巩固阶段的主要扫描对象）
├── tools/*.md          ← 工具使用经验详情（TOOLS.md 索引行指向这里）
├── contacts/*.md       ← 联系人/群成员信息（可选，按需创建）
├── graph/              ← 事件因果图谱（见模块六）
├── topics/             ← 主题实体索引（见模块七）
├── exploration/        ← 主动探索问题池（见模块十，按需创建）
└── forest/             ← DPM Trace Forest（见模块十一，按需创建）
    ├── leaves/         ← 散点事件
    ├── branches/       ← 主题线索
    └── trunks/         ← 认知跃迁

self-reference/         ← 自我指涉子系统（见模块二）
├── growth-journal.md   ← 认知生长日志（与即时层 SOUL.md 职责分离，见模块二）
├── user-profile.md     ← 对用户的理解
├── relationship.md     ← 关系理解
├── diaries/*.md        ← 反思日记
├── snapshots/          ← 事务 preimage 与 manifest（见模块三，唯一规范源；不含 SECRET 明文）
├── transaction-audit/  ← create-only 脱敏 canonical audit projection（控制面，不在 business write-set）
├── role-slices/        ← 角色化记忆切片（见模块十一，按需创建）
├── promotion-log.md    ← 晋升日志（见模块四）
├── skill-suggestions.md ← 技能建议冷却记录（见模块五）
├── retrieval-playbook.md ← 检索技巧手册（见模块八）
├── consolidation-log.md ← 从 canonical audit 派生的人类可读视图（非权威）
├── rollback_log.md     ← 从 canonical audit 派生的人类可读视图（非权威）
└── micro-consolidation-log.md ← 从 canonical audit 派生的人类可读视图（非权威）
```

> **按需创建原则**：`graph/` `topics/` `exploration/` `forest/` `role-slices/` 以及带 log 后缀的文件，在对应模块启用时才创建。fresh init 仍必须用 assets 模板创建 5 个即时层文件和 3 个核心自我指涉文件，以保证首次巩固前检可通过；其余增强目录按需创建。详见部署指南。

**index.json 格式**：
```json
{
  "entries": [
    {
      "file": "project/xxx.md",
      "summary": "一句话摘要",
      "tags": ["标签1", "标签2"],
      "updated": "2026-07-02"
    }
  ]
}
```

**USER.md 格式规范**（对应 `assets/USER_template.md`）：
```markdown
# 用户画像

## 稳定特征
- **偏好**：描述（YYYY-MM-DD 验证）

## 工作方式
- **习惯**：描述
```

**SOUL.md 格式规范**（对应 `assets/SOUL_template.md`，只含核心身份，**不含认知生长**——认知生长写入 `self-reference/growth-journal.md`）：
```markdown
# 身份定义

## 核心身份
- **性格特质**：描述
- **行为风格**：描述
```

**写入规则**：
- 新建文件可用 write_file
- 修改已有文件用 edit_file
- 写入后**必须同步更新 index.json**

### 长期层（Host 语义检索或本地降级）

Host 提供 `memory_search` 时，可对 Host 明确授权的数据源做 RAG 语义搜索。该能力不是本 skill 自带依赖，也不得索引 `SECRET.md`、`self-reference/snapshots/`、事务锁或其他非白名单路径。

Host 不提供语义检索时，降级为本地白名单检索：只遍历 `USER.md`、`MEMORY.md`、`SOUL.md`、`TOOLS.md`、`recent_memory/` 与 `self-reference/` 的业务记忆文件，并排除 `SECRET.md`、`self-reference/snapshots/`、锁、事务 manifest 和隐藏文件。优先使用 Host 本地搜索能力；若可用 `rg`，使用转义后的字面关键词和显式 glob。无本地搜索能力时按 `recent_memory/index.json` 指针人工遍历，不假装具备语义召回。

**搜索层级（由浅入深）**：
1. 即时层（已加载上下文）→ 先确认是否已有
2. 近中期层（index.json 定位）→ 结构化记忆
3. 长期层（可选 `memory_search`；否则白名单本地检索）→ 深层历史记忆

**何时搜索**：
- 用户说"好好想想""怎么不记得了"→ 至少推到第2层
- 当前任务需要历史决策/文件/结论 → 必须先验证

### 记录触发规则

**必须立即记录**：
- 用户明确说"记住""记一下"
- 消息中出现长期稳定、后续可能复用的信息

**判断归属**：
| 信息类型 | 归入文件 |
|----------|----------|
| 身份/性格/行为风格设定 | SOUL.md |
| secret handle/locator、轮换日期、last4 | SECRET.md（0600，按需读取） |
| API Key/密码/Token/私钥实际值 | **禁止写入记忆系统**；存入用户选择的 secret store |
| 换项目仍成立的用户信息 | USER.md |
| "用XX要注意YY"的经验 | TOOLS.md |
| 长期规则/状态锚点+指针 | MEMORY.md |
| 说不清的详细记录 | recent_memory/ |

> 注：联系人/群成员信息无专属即时层文件。稳定联系人归入 `USER.md`，一次性或详细联系人记录归入 `recent_memory/contacts/`（按需创建）。
