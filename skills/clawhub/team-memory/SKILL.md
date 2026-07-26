---
name: team-memory
description: 私人团队记忆管理系统 v2.6.0，面向管理者的本地 Markdown 长期记忆副驾。用于记录团队成员观察、1:1 沟通、OKR/绩效证据、相关方需求/投诉/反馈、上级期望和公司战略；维护成员档案、时间轴、蒸馏摘要、相关方画像和智能待办台账；生成团队情况一图流/A4 团队看板、同构概要文字版、1:1 准备、周报/月报、绩效材料、晋升评估、项目复盘、相关方沟通准备和向上汇报；支持旧 Markdown 导入、v1 数据兼容、主库锁定、JSONL/SQLite 机器索引、完整导出和本地隐私保护。
metadata:
  short-description: 本地团队长期记忆、绩效证据、相关方反馈和管理复盘工具
  tags:
    - team-management
    - manager-memory
    - performance-review
    - stakeholder-feedback
    - markdown
license: MIT
compatibility: opencode
version: "2.6.0"
---

# Team Memory v2.6.0

本 skill 帮助管理者维护本地 Markdown 团队记忆。原则：先保护历史数据，再更新结构；新写入使用 v2 结构，旧 v1 文件可继续读取。

Markdown 文件树是唯一可信源。JSONL/SQLite 只由 Markdown 重建，用于机器读取和导出，不反向覆盖 Markdown。

## 功能概览

- 成员长期档案：维护成员基本信息、角色职级、OKR、成长方向、管理策略和历史画像。
- 事件时间轴：记录成员日常表现、项目交付、协作沟通、1:1 对话、承诺事项和绩效证据。
- 蒸馏摘要：按成员沉淀近期状态、关键事件、风险点、追踪项和我的承诺，便于快速准备沟通。
- 相关方反馈：记录需求方、协作部门、投诉/反馈来源和项目接口人的需求、投诉、认可、风险和沟通记录。
- 证据等级管理：允许断续信息先进入系统，并用“线索 / 反馈 / 事实 / 结论”和核实状态控制使用边界。
- 智能待办台账：从时间轴中的追踪项和承诺生成 `tasks.md`，支持每周/月度复盘、等待反馈和沉默任务检查。
- 团队一图流：把成员近况、相关方反馈、待办控制、向上期望、公司战略和证据盲区压缩为 A4 SVG 看板，并生成同构 Markdown/JSON 兜底。
- 管理场景输出：生成 1:1 准备、周报/月报、绩效材料、晋升评估、项目复盘、相关方沟通准备和向上汇报素材。
- 数据迁移与导入：支持按成员整理的旧 Markdown 导入，兼容 v1 的 `姓名-档案.md`、`姓名-时间轴.md`、`姓名-蒸馏.md`。
- 本地索引和导出：从 Markdown 重建 JSONL/SQLite 机器索引，支持完整数据包导出和校验。
- 主库保护：通过 `.team-memory-root.json` 锁定唯一主库，避免写错目录或覆盖历史数据。

## 适用场景

使用本 skill 处理以下请求：记录团队成员表现、补充历史观察、准备 1:1、整理绩效证据、生成团队情况一图流/A4 团队看板/团队概况概要文字版、生成周报/月报、做晋升评估、复盘投诉和项目协作、沉淀需求方反馈、管理追踪事项、导入旧 Markdown 记录、检查或导出本地团队记忆数据。

## 主库锁定规则

默认主数据目录是当前 skill 根目录下的 `data/`，但所有写入必须先通过 `.team-memory-root.json` 锁定文件确认真实主库。

强制规则：

1. 写入前先确认 `.team-memory-root.json` 存在，并且 `skill-config.yaml` 的 `settings.data-path` 与锁定文件一致。
2. 没有锁定文件时停止，不要猜路径，不要创建 `~/.config/opencode/...` 或其他新目录。
3. 如果发布包自带 `data/`，首次使用运行 `scripts/adopt-data.py` 接管当前 `data/`。
4. 如果没有数据，首次使用运行 `scripts/init.sh` 创建空主库并写入锁定文件。
5. 如果检测到多套数据，运行 `scripts/doctor.py` 生成报告；不要自动合并、删除或覆盖。

## 数据结构

默认主数据目录：`data/`（由 `.team-memory-root.json` 锁定）

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
`.index/` 是可重建机器索引，不是源数据；事件索引用 `event_key = source_file:event_id` 作为机器唯一键。
`tasks/tasks.md` 是待办状态源；成员 `timeline.md` 是事实证据源。
`stakeholders/` 用于记录需求方、协作部门、投诉/反馈来源和项目接口人的长期互动；低证据等级记录只作为线索和追踪提醒。

成员真实姓名、别名、角色、职级和入职日期保存在 `skill-config.yaml`。文件路径优先使用 `member-XXX`，降低隐私和跨平台风险。

## v1 兼容

读取历史数据时同时支持：

- v2：`data/members/member-001/profile.md`
- v1：`data/members/张三-档案.md`
- v2：`data/members/member-001/timeline.md`
- v1：`data/members/张三-时间轴.md`
- v2：`data/members/member-001/distill.md`
- v1：`data/members/张三-蒸馏.md`

如果 v2 和 v1 同时存在：优先读取 v2，把 v1 视为只读历史来源。不要删除、覆盖或重命名 v1 文件，除非用户明确要求。

## 成员匹配

1. 读取 `skill-config.yaml` 的 `members` 和 `shortcuts`。
2. 用输入中的姓名、别名、成员 ID 匹配成员。
3. 如果多个成员命中同一别名，停止并请用户确认，不要猜。
4. 如果没有命中，询问是否创建新成员；创建时使用 `scripts/new-member.sh`。

## 记录观察

当用户说“记录……”“补一条……”“今天张三……”等记录请求：

1. 先确认主库锁定文件；路径不确定时停止并运行 `scripts/doctor.py`。
2. 匹配成员。
3. 写入锁定主库的 `data/members/{member-id}/timeline.md` 的“时间轴（从新到旧）”标题后方。
4. 新记录格式：

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

5. 如果输入里有承诺、提醒、下次跟进、1:1，要生成追踪项。
6. 记录后更新同成员 `distill.md`：近期状态、关键事件、追踪项。
7. 对负面记录只写事实和行为，不写人格判断。

## 相关方反馈记忆

当用户说“需求方反馈……”“运营投诉……”“设计认可……”“某项目接口人提到……”等公司内相关方信息：

1. 先确认主库锁定文件；路径不确定时停止并运行 `scripts/doctor.py`。
2. 相关方可以是个人、部门或项目接口，不强制是真人；路径使用 `data/stakeholders/stakeholder-XXX/`。
3. 相关方 `timeline.md` 保存完整关系脉络，事件 ID 使用 `FBK-YYYYMMDD-001`。
4. 必须标注 `证据等级` 和 `核实状态`：
   - 证据等级：线索 / 反馈 / 事实 / 结论
   - 核实状态：未核实 / 待补充 / 部分确认 / 已确认 / 已闭环 / 已撤销
5. 如果涉及明确成员表现，在成员 `timeline.md` 增加一条关联记录，引用 `FBK` 事件 ID。
6. `线索级` 和 `未核实`记录只用于提醒、追问和观察，不写入成员长期画像，不作为绩效结论。
7. `事实级` 或 `结论级`记录可以用于复盘、绩效和向上沟通，但输出时必须保留来源、日期和事件 ID。

相关方记录格式：

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
- [ ] 中 - 需要跟进的事项 (来源: FBK-YYYYMMDD-001)

**关联事件**:
- 
```

## 查询和报告

默认检索顺序：

1. 先读 `distill.md` 快速理解成员状态。
2. 涉及待办时先读 `data/tasks/tasks.md`，需要证据时追溯 `timeline.md`。
3. 需要证据时读 `timeline.md`，并追溯关联的 `FBK` 相关方反馈。
4. 需要 OKR、职级、发展计划时读 `profile.md`。
5. 准备需求方沟通、项目复盘或跨部门问题时，读 `data/stakeholders/{stakeholder-id}/distill.md` 和 `timeline.md`。
6. 团队级问题再读本地存在的 `data/team-memory-overview.md`、`upward/expectations.md`、`company/strategy.md`。
7. 用户要“团队情况一图流”“团队看板”“A4 概览”时，先读 `references/team-dashboard.md`，再运行 `python3 scripts/team-dashboard.py --format all` 生成统一数据包和图文输出。

常见输出：

- 1:1 准备：近期亮点、需关注、上次承诺、本次谈话要点、建议提问。
- 周报/月报：团队亮点、风险、外部认可、高频投诉、追踪项、下周期建议。
- 团队一图流：A4 SVG 看板 + 同构 Markdown/JSON，顺序固定为管理结论、关键数据、人员雷达、风险注意、7/30 天动作、背景摘录和证据索引。
- 绩效材料：按维度给评价，并引用具体日期和事件 ID。
- 晋升评估：只使用有记录证据的事件，区分事实、推断和建议。
- 相关方沟通准备：合作偏好、历史反馈、未闭环事项、敏感点和建议话术。

## 团队一图流

当用户要求快速了解团队整体情况时，不要只汇总普通记录。按管理看板处理：

1. 先确认主库锁定文件，路径不确定时运行 `scripts/doctor.py`。
2. 阅读 `references/team-dashboard.md`。
3. 运行 `python3 scripts/team-dashboard.py --format all`，默认输出到 `data/insights/`。
4. 优先返回 A4 SVG 图版路径；如果环境不能展示图片，返回同名 Markdown 文字版。
5. 保持图版和文字版同构：管理结论、关键数据、人员雷达、风险注意、7/30 天动作、背景摘录、证据索引。
6. 对线索级、未核实反馈、记录覆盖不足的成员明确标注“待核实/证据盲区”，不要写成绩效结论。
7. 如需进一步解释，再追溯成员 `timeline.md`、相关方 `timeline.md`、`tasks.md` 和证据 ID。

## 智能待办

- 日常记录后运行 `python3 scripts/sync-tasks.py`，把追踪项和我的承诺同步到 `data/tasks/tasks.md`。
- 同步范围包括成员“追踪项/我的承诺”和相关方“后续动作”，支持 `**追踪项**:` 和 `## 追踪项` 两类写法；新待办用 `对象类型` 和 `对象` 表示归属。
- 每周运行 `python3 scripts/review-tasks.py --weekly`，检查逾期、高优先、等待反馈和沉默超过 14 天的待办。
- 每月运行 `python3 scripts/review-tasks.py --monthly`，生成新增、关闭、延期、沉默和下月重点建议。
- 处理结果先运行 `python3 scripts/resolve-task.py TASK-ID --status done|waiting|dropped|deferred --note "..."` 生成草案。
- 用户确认后再加 `--apply` 写入台账；成员待办需要写回成员时间轴时再加 `--append-timeline`，相关方待办不自动写回成员时间轴。
- 不要手工合并重复待办；`sync-tasks.py` 只自动合并同来源行或正文完全一致的事项，相似但不一致的事项只在报告里提示。

## 更新和迁移

- 升级前阅读 `references/upgrade.md`。
- 已有 `data/` 的发布包首次使用 `scripts/adopt-data.py` 接管主库。
- 路径不确定或发现多套数据时运行 `scripts/doctor.py`。
- v1 到 v2 使用 `scripts/migrate-v1-to-v2.sh`。
- 迁移脚本默认 dry-run；只有 `--apply` 才复制文件。
- 迁移只复制，不删除旧文件。
- 按成员整理的旧 Markdown 使用 `scripts/import-member-markdown.sh`。
- Markdown 导入脚本默认 dry-run，并在 `data/import/reports/` 生成报告；只有 `--apply` 才写入 `timeline.md`。
- Markdown 导入只沉淀历史证据，不自动修改 `profile.md` 或 `distill.md`；导入后的当前人物卡更新应先生成建议稿并等待用户确认。
- 机器索引使用 `scripts/rebuild-index.py` 重建。
- 一致性检查使用 `scripts/doctor.py`，会报告事件总数/唯一 ID 数、同文件重复事件 ID、跨文件重复事件 ID、缺失相关方字段、断开的关联事件和失效待办来源。
- 数据导出使用 `scripts/export-data.py`。
- 使用说明见 `references/usage.md`。

## 参考文档

- 使用指南：`references/usage.md`
- 记录模板：`references/record-templates.md`
- 场景示例：`references/scenario-examples.md`
- 团队一图流数据架构：`references/team-dashboard.md`
- 故障排除：`references/troubleshooting.md`
- Markdown 历史记录导入：`references/import-markdown.md`
- 升级、迁移、兼容和变更摘要：`references/upgrade.md`
