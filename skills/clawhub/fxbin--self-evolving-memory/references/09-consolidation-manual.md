# 模块九：记忆巩固执行手册

本模块提供记忆巩固的**标准化执行流程**，任何加载本技能的 Agent 都可以按照此手册执行每日巩固。

### 触发时机

- **建议时间**：每日凌晨 00:20 ~ 00:30（对话低峰期）
- **触发方式**：手动触发；Host 提供 Calendar/调度器时可选定时触发
- **执行时长**：预计 5 ~ 15 分钟（视近期记忆量而定）
- **执行主体**：优先使用 Host 隔离 session；Host 不支持时在当前 session 手动执行并明确占用上下文

### 前置检查

执行前确认：
1. [ ] 能正常访问 4 个自动加载的即时文件（USER.md、MEMORY.md、SOUL.md、TOOLS.md）；SECRET.md 由模块一的非模型可信本地 scanner 检查，Agent 只接收 status/count/redacted locations
2. [ ] 能正常访问 self-reference/ 目录
3. [ ] 能正常访问 recent_memory/ 目录
4. [ ] Host 有可等价完成“仅不存在时创建、读取、修改、逐文件 SHA-256、原子获取锁”的本地文件能力
5. [ ] 当前不是对话高峰期
6. [ ] 模块三恢复扫描完成，不存在未恢复事务或活动共享锁
7. [ ] `growth-journal.md`、`user-profile.md`、`relationship.md` 已按模板存在
8. [ ] trusted SECRET scanner 返回 `clean_locator_only` 且权限检查为 `0600`；`plaintext_suspected`、`scanner_unavailable`、`scan_error` 或输出越界均阻塞

任何一项不满足 → 跳过本次巩固并返回脱敏阻塞报告；事务尚未开始时不原地追加 business/audit 日志。scanner 缺失时报告 capability gap `trusted_secret_scanner_required`，绝不改由模型读取 SECRET.md。

### 阶段0：事务守卫（必须最先执行）

**事务规则来源**：[模块三：记忆巩固守卫](03-consolidation-guard.md) 是共享锁、唯一 run-id、完整 business write-set、preimage/tombstone manifest、逐文件哈希、`.complete`、canonical audit 和恢复状态机的唯一真相源。本手册不得缩小或重定义该协议。

**本阶段动作**：先完成恢复扫描，获取大/微巩固共享排他锁，声明本轮完整 write-set，封存所有 preimage/tombstone 并逐文件 read-back/hash；只有模块三定义的 `.complete` 已创建后才能进入阶段 1。禁止随机抽查，禁止把 `SECRET.md` 放入普通快照。

**产出**：已封存且可整组恢复的事务 manifest；尚无任何业务写入。

### 阶段1：事实巩固

**目标**：将近期情境记忆中的稳定事实提炼升级到语义层。

**步骤**：

1. **扫描近中期层**
   - 读取 `recent_memory/index.json`，了解所有记忆单元
   - 读取 `recent_memory/episodic/` 下近期（7天内）的情境记忆文件
   - 整体记忆结构以 `recent_memory/index.json` 为准（无需独立的 INDEX.md）

2. **先执行证据门控（DPM 启用时）**
   - 启用模块十一：累计证据权重 ≥3.0 才能进入评分；不足者标记“待验证+高价值”并停止该条目的晋升
   - 未启用模块十一：直接进入模块四评分

3. **逐份评估升级价值**
   对通过前置条件的情境记忆单元，按晋升评估标准打分：
   - 复用频率（0-2分）
   - 稳定性（0-2分）
   - 决策权重（0-2分）
   - 不可替代性（0-2分）
   - 情感显著性（0-2分）

4. **执行升级**
   - **≥7分**：升级到即时层对应文件
     - 用户信息 → USER.md
     - 规则/状态 → MEMORY.md
     - 工具经验 → TOOLS.md
     - 身份/性格观察 → `self-reference/growth-journal.md`（`SOUL.md` 在巩固中永不写入）
   - **5-6.9分**：标记为"下次巩固重点审视"，保留在近中期层
   - **<5分**：维持现状

5. **更新索引**
   - 更新 `recent_memory/index.json` 中对应条目的状态与最后验证时间
   - 已升级的条目标注"已晋升"并保留指针

6. **压缩过期记忆**
   - 超过 7 天且已巩固的情境记忆，压缩为单行摘要
   - 保留核心信息：时间、事件、结论
   - 删除冗余细节描述

**产出**：更新后的语义记忆文件 + 更新的索引 + 晋升日志

### 阶段1.5：深度提炼（可选，仅在启用模块十一 DPM 时执行）

**触发条件**：Agent 已启用模块十一的 DPM 动态分层增强。未启用则跳过本阶段，直接进入阶段2。

**执行内容**：三角色并行提炼（因果侦探 / 模式猎手 / 边界测绘员），具体角色职责、产出标准、与阶段1/2 的衔接见 [模块十一 §核心机制二](11-dpm-enhancement.md#核心机制二三角色提炼因果侦探--模式猎手--边界测绘员)。

**产出**：新增因果边 + 模式清单 + 问题池更新（具体由模块十一定义）。

### 阶段2：自我改写

**目标**：基于近期经历，更新自我认知、关系理解，沉淀成长。

**核心原则**：
- 不是每件事都要改（宁缺毋滥）
- 改写是生长不是覆盖（只追加，不删除已有章节）
- 允许矛盾（认知本身就是多面的）
- 不要空话（必须有具体事件支撑）
- `SOUL.md` 是只读基线；任何身份观察都写 `growth-journal.md`

**步骤**：

1. **回顾近期经历**
   - 扫描近 3 天的对话、事件、决策
   - 提取对自己有冲击/有启发的 2-3 件事

2. **审视自我认知**（growth-journal.md）
   - 问自己：这件事让我对"我是谁"有了什么新理解？
   - 如果有新的认知生长点，追加到 growth-journal.md 的"认知生长"章节
   - 格式：`**标题（日期）**：具体理解`
   - 没有新认知就不写，不要硬凑

3. **审视关系理解**（relationship.md）
   - 问自己：近期互动让我对我们的关系有了什么新理解？
   - 有新发现就追加，没有就跳过

4. **审视用户画像**（user-profile.md）
   - 问自己：有没有发现用户新的偏好、习惯、做事方式？
   - 确认是稳定特征（出现 ≥3 次验证；注意：本流程按"次数"，与模块十一证据门控按"累计权重≥3.0"是不同 metric，两者精神相似但不等价）再追加

5. **写反思日记**
   - 路径：`self-reference/diaries/YYYY-MM-DD.md`
   - 内容：当天最有感触的 1-2 件事 + 思考
   - 不需要长，真诚就好
   - 没有特别值得写的可以跳过

**产出**：可能更新的 growth-journal.md / relationship.md / user-profile.md + 当日反思日记

### 阶段3：校验与回滚

**目标**：确保巩固没有引入错误或越界。

**硬规则校验清单**（任何一项不通过都按模块三回滚完整 write-set，不在失败事务中原地修补）：

| 校验项 | 标准 | 不通过的处理 |
|--------|------|-------------|
| 关键信息完整性 | 用户ID、偏好、核心项目状态不可丢失 | 回滚对应文件 |
| growth-journal.md 连续性 | 不允许删除已有章节，只能追加 | 回滚 growth-journal.md |
| 关系理解不倒退 | relationship.md 不应出现比之前更浅的理解 | 人工复核，必要时回滚 |
| 文件容量 | 即时层总量 ≤20KB 且单文件不超上限（USER 2048B / MEMORY 5120B / SOUL 4096B / TOOLS 5120B / SECRET 4096B） | 整组回滚；在新 run 中先压缩或下沉 |
| SOUL.md 字节不变 | 运行前后 SHA-256 必须一致 | 整组回滚并记录身份边界违规 |
| SECRET.md 边界 | trusted scanner=`clean_locator_only`、0600，且 SECRET 未进入模型 read/write-set、RAG 或快照 | scanner 命中或不可用时阻塞；若事务已开始则整组回滚后持久化脱敏 audit |
| 格式规范 | MEMORY.md 必须有"长期行为规则"和"核心状态锚点"两个分区，遵循粗体标题+代码块指针格式 | 整组回滚；在新 run 中修正 |
| write-set 完整性 | 所有业务写入都在 manifest 中，且逐文件 read-back/hash 成功 | 整组回滚 |

**回滚操作**：只执行模块三恢复状态机：现存业务目标按 preimage 恢复，新建业务目标按 tombstone 删除，逐文件验证原哈希；随后先封存 rolled_back outcome manifest，再写入并 read-back/hash 脱敏 canonical audit projection。audit durable 前不释放锁；audit 失败进入 `recovery_failed` 并保留锁。

**全部通过后**：
- 记录本次巩固总结到 `recent_memory/episodic/consolidation_YYYYMMDD.md`
- Host 有 Calendar 时可更新状态；否则以 canonical audit projection 为状态源。人类可读巩固/回滚日志只能在锁释放后由 projection 派生，不是权威记录

**产出**：校验报告 + 可能的回滚 + 巩固总结日志

### 异常处理

| 异常情况 | 处理方式 |
|----------|----------|
| 快照创建失败 | 立即中止，不执行后续步骤 |
| 某个文件读取失败 | 中止业务写入；若已进入 mutating 则回滚完整 write-set |
| 写文件或 read-back/hash 出错 | 回滚完整 write-set，不继续其他目标 |
| 校验发现多处问题 | 全部回滚，本次巩固标记为失败 |
| 执行超时（>30分钟） | 回滚完整 write-set，不保留部分结果 |

### 巩固效果评估

每月做一次巩固效果回顾：
- 回顾过去一个月的巩固记录
- 统计：晋升了多少条记忆、回滚了多少次、新增了多少认知生长
- 评估：即时层信息的准确率、近中期层的利用率
- 调整：优化晋升评分标准、调整巩固频率
