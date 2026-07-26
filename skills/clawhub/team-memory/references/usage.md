# Team Memory 使用指南

Team Memory v2.6.0 是一个本地 Markdown 团队记忆系统，用于记录成员观察、相关方反馈、维护档案、管理智能待办、生成团队情况一图流、准备 1:1、生成周报/月报和绩效材料。

Markdown 文件树是唯一可信源。JSONL/SQLite 只由 Markdown 重建，用于机器读取和导出。

首次使用分两种情况：

- 发布包自带已有 `data/`：运行 `scripts/adopt-data.py`，接管当前 `data/` 为唯一主库。
- 没有数据：运行 `scripts/init.sh`，创建空主库并写入 `.team-memory-root.json`。

任何写入都必须先确认 `.team-memory-root.json` 存在。不要让智能体自行创建 `~/.config/opencode/...` 或其他新目录。

## 推荐结构

```text
data/
├── members/
│   └── member-001/
│       ├── profile.md
│       ├── timeline.md
│       └── distill.md
├── stakeholders/
│   └── stakeholder-001/
│       ├── profile.md
│       ├── timeline.md
│       └── distill.md
├── upward/
│   └── expectations.md
├── company/
│   └── strategy.md
├── insights/
├── templates/
├── import/
│   ├── incoming/
│   └── reports/
├── tasks/
│   ├── tasks.md
│   └── reviews/
├── .index/
│   ├── events.jsonl
│   ├── tasks.jsonl
│   └── team-memory.sqlite
├── .backup/
└── archive/
```

`.backup/` 是内部备份目录，通常不需要直接查看或手动编辑。
`.index/` 是可重建机器索引，不是源数据。
`tasks/tasks.md` 是待办状态源，成员时间轴是事实证据源。
`stakeholders/` 保存需求方、协作部门、投诉/反馈来源和项目接口人的长期互动。

## 快速开始

1. 接管或初始化主库：

```bash
# 已有 data 时
python3 scripts/adopt-data.py

# 没有 data 时
bash scripts/init.sh
```

2. 编辑 `skill-config.yaml`：

- 每个成员必须有唯一 `id`，例如 `member-001`
- `name` 可以是真名
- `alias` 和 `shortcuts` 必须唯一
- `schema-version: "2.2"` 表示数据结构版本，不等同于产品版本

3. 创建新成员：

```bash
bash scripts/new-member.sh member-010 "张三" "后端开发工程师" "2026-05-21"
```

脚本会创建 `profile.md`、`timeline.md`、`distill.md`，并提示你手动更新 `skill-config.yaml`。

4. 检查路径：

```bash
python3 scripts/doctor.py
```

如果报告显示多套数据，先人工确认主库，不要写入。

## 日常记录

对 Codex/OpenCode 说：

```text
记录：张三今天主动修复了生产问题，并写了复盘文档
```

写入规则：

- 写入前确认主库锁定文件存在，路径不确定时先运行 `scripts/doctor.py`
- 匹配 `skill-config.yaml` 中的姓名、别名或成员 ID
- 新记录写入 `data/members/{member-id}/timeline.md`
- 新记录添加在“时间轴（从新到旧）”标题下方
- 如果包含承诺、提醒、下次跟进、1:1，要生成追踪项
- 记录后更新 `distill.md` 的近期状态、关键事件和追踪项

## 相关方反馈

对 Codex/OpenCode 说：

```text
记录相关方反馈：运营反馈张三这次素材交接响应慢，具体项目还要再确认
```

写入规则：

- 写入前确认主库锁定文件存在，路径不确定时先运行 `scripts/doctor.py`
- 相关方可以是个人、部门或项目接口，路径使用 `data/stakeholders/stakeholder-XXX/`
- 相关方 `timeline.md` 保存完整关系脉络，事件 ID 使用 `FBK-YYYYMMDD-001`
- 如果涉及明确成员表现，在成员 `timeline.md` 增加一条关联记录，引用对应 `FBK` 事件
- 信息断续、不完整时允许先记录，但必须标注 `证据等级` 和 `核实状态`

证据等级：

- 线索：信息不完整，只用于提醒后续观察
- 反馈：来源明确，但上下文未完全核实
- 事实：时间、对象、行为、影响基本清楚
- 结论：已复盘并确认原因、责任边界、改进动作和结果

核实状态：

- 未核实 / 待补充 / 部分确认 / 已确认 / 已闭环 / 已撤销

使用边界：

- `线索级` 或 `未核实`记录不能直接进入成员长期画像、绩效结论或晋升判断
- `反馈级`记录可用于沟通准备、追问和风险观察
- `事实级` 和 `结论级`记录可用于复盘、绩效和向上沟通，但必须引用来源、日期和事件 ID
- 投诉、负面反馈只写事实、行为和影响，不写人格判断

相关方记录模板：

```markdown
### YYYY-MM-DD（周X）
#### HH:MM - 一句话标题 [FBK-YYYYMMDD-001]
**反馈类型**: 需求 / 投诉 / 认可 / 风险 / 建议 / 沟通记录  
**证据等级**: 线索 / 反馈 / 事实 / 结论  
**核实状态**: 未核实 / 待补充 / 部分确认 / 已确认 / 已闭环 / 已撤销  
**来源方**:   
**涉及成员**:   
**涉及项目**:   
**标签**: #相关方反馈

**事实描述**:
- 

**当前判断**:
- 

**后续动作**:
- [ ] 中 - 需要核实或跟进的事项 (来源: FBK-YYYYMMDD-001)

**关联事件**:
- 
```

## 导入旧 Markdown 记录

把按成员整理好的旧 Markdown 放到：

```text
data/import/incoming/member-001/
```

先预览：

```bash
bash scripts/import-member-markdown.sh
```

确认 `data/import/reports/` 下的报告后再写入：

```bash
bash scripts/import-member-markdown.sh --apply
```

导入规则：

- 新事件 ID 形如 `OBS-YYYYMMDD-IMPORT-001`
- 记录写入对应成员 `timeline.md` 的“时间轴（从新到旧）”
- 不覆盖、不删除、不重写已有事件
- 每条记录保留来源文件、行号、导入时间和原始记录
- 重复执行会跳过已导入记录
- 不自动修改 `profile.md` 或 `distill.md`

MBTI、年度期待、管理判断、发现的问题、对组员说的话，都作为带日期来源的历史证据进入时间轴。需要刷新当前人物卡时，先让智能体基于 `profile.md`、`timeline.md` 和 `distill.md` 生成更新建议，确认后再写入。

## 智能待办

同步追踪项到待办台账：

```bash
python3 scripts/sync-tasks.py
```

同步范围包括成员 `timeline.md` / `distill.md` 的“追踪项、我的承诺”，以及相关方 `timeline.md` / `distill.md` 的“后续动作”。脚本同时支持 `**追踪项**:` 和 `## 追踪项` 这类写法。新待办会写入 `对象类型` 和 `对象`，例如 `member member-001` 或 `stakeholder stakeholder-001`；旧的 `成员` 字段仍可读取。

每周扫描：

```bash
python3 scripts/review-tasks.py --weekly
```

月度复盘：

```bash
python3 scripts/review-tasks.py --monthly
```

处理结果先生成草案：

```bash
python3 scripts/resolve-task.py TASK-20260701-001 --status waiting --note "已追问，等待反馈"
```

确认后再写入：

```bash
python3 scripts/resolve-task.py TASK-20260701-001 --status done --note "已完成复盘" --apply
```

需要把处理结果写回成员时间轴时再加 `--append-timeline`。只有成员待办支持自动写回成员时间轴；相关方待办请在相关方 `timeline.md` 记录处理结果。脚本会保留所有来源事件，不删除原始时间轴记录。待办只在同一来源行或正文完全一致时自动合并，相似但不一致的事项会进入同步报告提醒。

## 重建索引和导出

重建机器索引：

```bash
python3 scripts/rebuild-index.py
```

导出完整数据包：

```bash
python3 scripts/export-data.py
```

导出包包含 Markdown 主库、`tasks.md`、`events.jsonl`、`tasks.jsonl`、`team-memory.sqlite`、`manifest.json` 和 `checksums.sha256`。Markdown 仍是唯一可信源，SQLite/JSONL 可以随时重建。事件索引中 `event_id` 是人类可读 ID，允许不同文件中重复；机器唯一键使用 `event_key = source_file:event_id`。

## 记录模板

```markdown
### YYYY-MM-DD（周X）
#### HH:MM - 一句话标题 [OBS-YYYYMMDD-001]
**事件**: 事实描述  
**类别**: 技术能力 / 协作沟通 / 项目交付 / 团队影响 / 成长潜力  
**评价**: ⭐⭐⭐⭐⭐ 优秀 / ⭐⭐⭐⭐ 良好 / ⭐⭐⭐ 一般 / ⚠️ 需关注  
**标签**: #标签

**观察笔记**:
- 基于事实的观察

**追踪项**:
- [ ] 中 - 需要跟进的事项 (来源: OBS-YYYYMMDD-001)
```

成员侧关联相关方反馈：

```markdown
### YYYY-MM-DD（周X）
#### HH:MM - 相关方反馈关联 [OBS-YYYYMMDD-001]
**事件**: 成员相关行为或影响的事实摘要  
**类别**: 协作沟通 / 项目交付 / 团队影响  
**评价**: ⭐⭐⭐ 一般 / ⚠️ 需关注 / ⭐⭐⭐⭐ 良好  
**证据等级**: 线索 / 反馈 / 事实 / 结论  
**核实状态**: 未核实 / 待补充 / 部分确认 / 已确认 / 已闭环 / 已撤销  
**关联事件**: FBK-YYYYMMDD-001  
**标签**: #相关方反馈

**观察笔记**:
- 区分对方反馈和自己的判断

**追踪项**:
- [ ] 中 - 需要和成员或相关方跟进的动作 (来源: FBK-YYYYMMDD-001)
```

## 1:1 模板

```markdown
### YYYY-MM-DD（周X）
#### HH:MM - 1:1沟通 [DLG-YYYYMMDD-001]
**事件**: 和{姓名}1:1  
**类别**: 协作沟通 / 成长潜力  
**评价**: ⭐⭐⭐⭐ 良好  
**标签**: #对话 #1on1

**对方反馈**:
- 

**我说了**:
- 

**我的承诺**:
- [ ] {待办} (来源: DLG-YYYYMMDD-001)

**事后反思**:
- 有效：
- 下次改进：
```

## 查询和报告

默认检索顺序：

1. 先读 `distill.md` 快速理解成员状态
2. 涉及待办时读 `data/tasks/tasks.md`
3. 需要证据时读 `timeline.md`，并追溯关联的 `FBK` 相关方反馈
4. 需要 OKR、职级、发展计划时读 `profile.md`
5. 准备需求方沟通、项目复盘或跨部门问题时，读 `data/stakeholders/{stakeholder-id}/distill.md` 和 `timeline.md`
6. 团队级问题再读 `team-memory-overview.md`、`upward/expectations.md`、`company/strategy.md`

常见请求：

```text
准备明天和张三的 1:1
生成本周团队观察报告
生成团队情况一图流
生成张三本季度绩效材料，需要引用具体证据
对比张三和李四的晋升资格
准备和运营需求方的沟通
复盘本月设计投诉和反馈
```

输出要求：

- 团队一图流：A4 SVG 看板 + 同构 Markdown/JSON，包含管理结论、关键数据、人员雷达、风险注意、7/30 天动作、背景摘录和证据索引
- 1:1 准备：近期亮点、需关注、上次承诺、本次谈话要点、建议提问
- 周报/月报：团队亮点、风险、追踪项、下周期建议
- 相关方沟通准备：合作偏好、历史反馈、未闭环事项、敏感点和建议话术
- 项目复盘：高频投诉、重复需求、外部认可、跨部门风险和闭环动作
- 待办复盘：逾期、高优先、等待反馈、沉默超过 14 天、下月重点
- 绩效材料：按维度评价，并引用日期和事件 ID
- 晋升评估：只使用有记录证据的事件，区分事实、推断和建议

## 团队一图流

当用户说“团队情况一图流”“团队看板”“一张图了解团队”“A4 概览”时，先生成统一数据包：

```bash
python3 scripts/team-dashboard.py --format all
```

默认输出：

```text
data/insights/team-dashboard-YYYYMMDD.svg
data/insights/team-dashboard-YYYYMMDD.md
data/insights/team-dashboard-YYYYMMDD.json
```

SVG 是 A4 图版，Markdown 是概要文字兜底，JSON 是同构数据包。三者结构一致，不要让图版和文字版各自重新组织数据。

一图流固定顺序：

1. 管理结论
2. 关键数据
3. 人员雷达
4. 7 天动作
5. 30 天动作
6. 背景摘录
7. 证据索引

一图流必须同时参考成员事件、相关方反馈、`tasks.md`、成员 `distill.md`、`team-memory-overview.md`、`upward/expectations.md` 和 `company/strategy.md`。缺少团队概况、向上期望或公司战略时，在“背景与证据盲区”里提示补齐。

健康分、控制压力和势能差只是管理启发指标，不是绩效评分。涉及绩效、晋升或处罚时，必须回到具体日期、事件 ID、证据等级和原文。

## 多层架构

- 蒸馏层：`distill.md`，用于快速理解成员状态
- 原始层：`timeline.md`，用于追溯完整事实和证据
- 档案层：`profile.md`，用于 OKR、角色、职级和发展计划
- 相关方层：`stakeholders/`，用于追溯需求方、协作部门和反馈来源的长期互动

准备 1:1 时，先读蒸馏层，再按需追溯原始层。生成绩效材料时，必须从时间轴引用具体日期和事件 ID。
涉及投诉、需求方反馈和外部认可时，必须保留证据等级、核实状态和 `FBK` 事件 ID。

## 隐私建议

- 文件路径优先使用 `member-XXX`
- 相关方路径优先使用 `stakeholder-XXX`
- 真实姓名放在 `skill-config.yaml` 和正文必要位置
- 不要把 `data/` 上传到公共仓库
- 网盘同步前检查加密和共享权限
- 离职成员优先归档到 `data/archive/`

## 故障排除

### 记录无法匹配成员

检查 `skill-config.yaml`：

- `members[].name` 是否与输入姓名一致
- `members[].alias` 是否唯一
- `shortcuts` 是否指向真实存在的 `member-XXX`

### 生成报告缺少数据

常见原因：

- `distill.md` 没有及时更新
- `timeline.md` 记录太少或事件描述过短
- 旧 v1 文件还没有迁移，且查询时没有读取 v1 兼容路径

### 文件名或压缩包乱码

v2 的默认路径使用英文和 `member-XXX`。发布包内部路径必须使用 `/`，不要使用 Windows 反斜杠。

### 写入到了错误目录

运行：

```bash
python3 scripts/doctor.py
```

检查 `.team-memory-root.json`、`skill-config.yaml` 的 `settings.data-path` 和候选数据目录。不要手动合并；先看报告确认主库。

`doctor.py` 还会显示事件总数和唯一事件 ID 数，并检查同文件重复事件 ID、跨文件重复事件 ID、缺失相关方反馈必填字段、断开的关联事件、失效待办来源和成员蒸馏里的低证据等级内容。同文件重复事件 ID 必须先修复，否则 `rebuild-index.py` 会停止重建，避免 SQLite 静默覆盖。

### 搜索历史记录

```bash
rg "张三|member-001|OBS-2024" data/members
```

如果没有安装 `rg`：

```bash
grep -R "张三" data/members
```
