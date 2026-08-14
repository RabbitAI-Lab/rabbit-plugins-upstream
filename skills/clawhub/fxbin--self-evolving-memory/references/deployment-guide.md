# 部署指南

## 初始化模式判定

先只读检查目标 Agent 工作目录，不先创建或覆盖文件：

- **fresh init**：5 个即时文件和 3 个核心自我指涉文件全部不存在
- **existing deployment**：任一目标文件或 `recent_memory/index.json` 已存在。只校验与补缺，不覆盖已有内容
- **legacy layout unsupported**：检测到旧布局文件 `self-reference/soul.md`。**不向后兼容**：不移动、不复制、不合并、不覆盖、不自动更名。立即停止并返回 `legacy_layout_unsupported`，旧文件字节保持不变；提示用户人工导出后重新初始化为当前布局（仅认 `self-reference/growth-journal.md`）

目标文件：

```text
USER.md
MEMORY.md
SOUL.md
TOOLS.md
SECRET.md
self-reference/growth-journal.md
self-reference/user-profile.md
self-reference/relationship.md
```

## Fresh init

1. 创建核心目录：`recent_memory/{project,decision,todo,episodic,tools}` 与 `self-reference/{diaries,snapshots,transaction-audit}`。
2. **仅在目标不存在时**，逐份读取并原样创建：
   - `assets/USER_template.md` → `USER.md`
   - `assets/MEMORY_template.md` → `MEMORY.md`
   - `assets/SOUL_template.md` → `SOUL.md`
   - `assets/TOOLS_template.md` → `TOOLS.md`
   - `assets/SECRET_template.md` → `SECRET.md`
   - `assets/GROWTH_JOURNAL_template.md` → `self-reference/growth-journal.md`
   - `assets/USER_PROFILE_template.md` → `self-reference/user-profile.md`
   - `assets/RELATIONSHIP_template.md` → `self-reference/relationship.md`
3. 创建 `SECRET.md` 后立即设置权限 `0600` 并 read-back 权限；失败则停止初始化，不写秘密值。
4. `recent_memory/index.json` 仅在不存在时由 `assets/recent_memory_index_template.json` 创建；若已存在，只做 JSON 解析和条目结构校验，绝不重置为 `{"entries":[]}`。
5. 可按需创建 `promotion-log.md`、`skill-suggestions.md`、`retrieval-playbook.md`、`consolidation-log.md`、`rollback_log.md` 和 `micro-consolidation-log.md`；不得用空文件覆盖现有日志。

任一步发现目标突然出现（并发初始化）即停止并重新诊断，不继续覆盖。

## Existing deployment：校验与补缺

- 对存在文件检查格式、权限与容量，只报告问题；修复前先获得用户对具体变更的确认
- 缺失文件可从对应模板创建，但必须使用“仅不存在时创建”语义
- `SECRET.md` 必须由模块一的非模型可信本地 scanner 检查；Agent 只接收 status/count/redacted locations。`plaintext_suspected` 时停止、轮换并迁移；scanner unavailable/error 时报告 `trusted_secret_scanner_required` 并阻塞，不得把文件内容送入模型
- `SOUL.md` 不因初始化、修复、巩固或 DPM 自动改变；只有用户明确授权的独立身份维护流程可改，且修改前展示精确 diff 并使用独立快照
- 检测到 `self-reference/soul.md`（legacy）时按上文 `legacy_layout_unsupported` 处理，**不提供任何可执行的迁移命令或脚本**

## Host 能力与降级

- **核心保证**：状态真相源是本地文件；上述初始化、容量、事务与身份/秘密边界不依赖外部数据库
- **定时触发是可选能力**：Host 有 Calendar/调度器时可设置每日低峰运行；没有时提供手动巩固清单，由用户显式触发
- **语义检索是可选能力**：Host 有 `memory_search` 时仅检索授权数据；没有时使用模块一的本地白名单关键词检索，排除 SECRET、snapshots、锁和 manifest
- Host 缺少安全的文件权限、排他创建、哈希或 read-back 能力时，不得运行巩固事务；应报告缺失能力和人工替代步骤

## 容量管理

当即时层文件接近容量上限时，在新事务中：

1. 优先精简过期或重复内容
2. 将详细内容下沉到 `recent_memory/`，在即时层保留指针
3. 写入后逐文件 read-back，并验证即时层总量和单文件上限

## 自检清单

- [ ] 模式判定正确，existing deployment 没有被模板覆盖
- [ ] 5 个即时文件和 3 个核心自我指涉文件存在
- [ ] SECRET.md 为 0600、只含 locator/脱敏元数据且未被自动加载或索引
- [ ] trusted SECRET scanner 返回 `clean_locator_only`；输出不含匹配文本，scanner 不可用时保持阻塞
- [ ] SOUL.md 保持用户授权的核心身份基线
- [ ] MEMORY.md 有“长期行为规则”和“核心状态锚点”两个分区
- [ ] `recent_memory/index.json` 可解析，已有条目未被清空
- [ ] 不存在 `self-reference/soul.md`（若存在则触发 `legacy_layout_unsupported`，停止初始化）
- [ ] 首次巩固前可获取共享锁、创建唯一 run-id、封存完整 business write-set 并逐文件哈希；`transaction-audit/` 位于 business write-set 外
