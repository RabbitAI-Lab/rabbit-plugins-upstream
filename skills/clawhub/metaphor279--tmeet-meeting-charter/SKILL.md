---
name: tmeet-meeting-charter
description: "Turn user-uploaded files and conversation into a durable, versioned meeting charter that can be retrieved or updated later, and create a one-time pre-meeting reminder that reloads the latest charter. Use when a user asks to prepare, save, review, revise, or be reminded of a Tencent Meeting charter, agenda, scope, decision rules, parking-lot topics, or meeting progress."
---

# 腾讯会议章程沉淀与定时提醒

将用户上传的文件和对话沉淀为一份可持续更新、随时查阅的会议章程，并在用户指定的时间触发 Agent 提醒。调用 `tmeet` 时同时遵守官方 `tmeet-skill` 的认证、隐私、分页和多结果确认规则。

## 命令子树

```text
tmeet
├── auth
│   ├── login
│   └── status
└── meeting
    ├── get
    ├── list
    └── search
```

这些命令只补充会议主题、会议号和时间等元数据。章程的事实主体来自用户上传的文件与对话，不依赖知识库。

## 工作流

### 1. 收集并核对上下文

1. 读取用户本轮上传的文件、粘贴内容和对话中已确认的信息。
2. 若用户提供会议号，使用 `meeting get` 补齐元数据；仅给关键词时用 `meeting search`；仅给时间范围时用 `meeting list`。
3. 搜索出现多场候选会议时，展示主题、会议号和时间并等待用户选择，不自行猜测。
4. 检查来源之间的冲突。优先级为：用户最新明确确认 > 较新版本文件 > 较旧文件；不能消解时并列记录为“待确认”。
5. 不虚构业务背景、会议进度、拍板人、责任人、截止时间或制度要求。缺失字段写“待确认”。

macOS/Linux 使用 `tmeet`，Windows x64 使用 `tmeet.cmd`。例如：

```powershell
tmeet.cmd meeting get --meeting-code "<MEETING_CODE>" --compact
```

### 2. 整理会议章程

章程必须包含：

1. 基本信息：主题、会议号、时间、参会角色、预计时长。
2. 背景与当前进展：已完成事项、正在推进事项、阻塞点及其来源。
3. 可验收的会议目标：避免只写“同步信息”。
4. 必须产出：结论/交付物、责任人、截止时间；未知项标记待确认。
5. 讨论范围与不讨论事项。
6. 议程时间盒：背景、讨论、决策、待办确认和余量。
7. 决策规则：拍板人、异议记录和升级路径。
8. 停车场：离题但有价值、需会后处理的事项。
9. 风险、未决问题与会前检查项。
10. 结束标准：必须产出均有结论，待办均有责任人和时间或明确待确认。

默认返回完整章程。用户要求“会前快速看”时，另附一段不超过 10 条的注意事项，但不得取代完整版本。

### 3. 持久化和版本更新

用户要求保存、以后查阅或创建提醒时，将章程写入当前工作区的 `meeting-charters/`，不要写入 Skill 安装目录：

```text
meeting-charters/
└── <meeting-code>-<topic>.md
```

没有会议号时使用 `<YYYY-MM-DD>-<topic>.md`。文件使用以下 YAML front matter：

```yaml
---
title: "<会议主题>"
meeting_code: "<会议号或待确认>"
start_time: "<ISO 8601 或待确认>"
version: 1
updated_at: "<ISO 8601>"
remind_at: "<ISO 8601 或未设置>"
source_files:
  - "<来源文件>"
---
```

- 同一会议后续更新原文件并递增 `version`，保留已确认决策；新来源与旧结论冲突时不静默覆盖。
- 返回保存路径、版本和待确认项。
- 用户说“查一下这个会议章程”时，先按会议号精确匹配；没有会议号再按主题/日期查找。多结果必须请用户选择。

### 4. 创建会前提醒触发器

只在用户明确要求提醒时创建。用户只说“会前提醒”但未给提前量或准确时间时，先询问；不要自行采用默认提前量。

1. 章程必须先保存，并确定会议开始时间和 `remind_at`。
2. 使用当前 Agent 宿主提供的一次性自动化/定时任务能力创建触发器，不使用模型常驻轮询。
3. 触发器载荷只保存章程绝对路径、会议号和提醒意图，不保存章程正文快照。
4. 触发时重新读取该路径中的最新版本，向用户发送：会议目标、必须产出、议程时间盒、风险/未决问题、结束标准和文件路径。
5. 修改会议时间或提醒时间时，更新原触发器，避免重复提醒；取消提醒时删除对应触发器。
6. 若宿主没有定时能力，只返回待创建的触发器规格，并明确说“尚未创建主动提醒”，不得声称会按时提醒。

创建成功后的响应必须说明提醒时间、时区、关联会议、读取的章程路径，以及“提醒时会读取最新版本”。

## 输出骨架

```markdown
# 会议章程｜<会议主题>

## 基本信息
## 背景与当前进展
## 会议目标
## 必须产出
## 议程时间盒
## 讨论范围与不讨论事项
## 决策规则
## 停车场
## 风险与未决问题
## 会前检查
## 结束标准
```

## 边界

- 不创建知识库、外部任务或会议本身，不修改/取消会议。
- 不声称能依据实时 ASR 自动判断跑题，也不在会议公屏主动打断。
- 上传材料包含敏感信息时，只在用户授权的工作区保存；面向用户不展示 `meeting_id`、Token 或其他内部标识。
- 本模块可独立安装；主 Skill 只按 `$tmeet-meeting-charter` 名称调用，不依赖兄弟模块目录。
