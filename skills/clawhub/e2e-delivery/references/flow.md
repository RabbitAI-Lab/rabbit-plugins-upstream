# 五阶段执行手册

本文件承载每阶段每步的详细指令、命令示例、决策点。SKILL.md 里概述了阶段目标，本文件是执行细则。

**通用约定**：
- 🤖 = skill 自动执行
- 👤 = 人工阻塞（等用户完成后回复"继续"）
- 🔀 = 决策确认（询问用户参数或确认）
- 每步执行前写 `step_started`，执行后写 `step_completed` / `step_failed`

---

## 阶段 ① 准备

**入场前提**：环境预检通过（见 `env-precheck.md`）。
**出场判据**：`session.workItem` 已填充、`session.repo` 已识别到当前 git 仓库、`session.currentPhase == 'develop'`。

### Step 1.1 载入或初始化 session 🤖

```bash
mkdir -p ~/.claude/e2e-sessions
```

若 `~/.claude/e2e-sessions/<workitem-id>.json` 存在 → 读入内存，询问用户是否恢复；否则按 `session-schema.md` 初始化。

### Step 1.2 入口模式识别 🔀

- 输入匹配 `^\d+$` 或含 `pingcode2.devops.*/work-item-detail/(\d+)` → 模式 A，提取 ID
- 其他 → 模式 B，触发 `Skill(pingcode-assistant-pro)` 走创建流程，拿到 ID 后回到本 skill

### Step 1.3 获取工作项详情 🤖

```bash
ee-cli pingcode workitem get <id>
```

将响应写入 `session.workItem`（id、type、title、url、workSpaceInfo.id 等）。若返回 404 → 中断，报"未找到该工作项"。

### Step 1.4 识别当前仓库 🤖

```bash
cd <workspace> && git remote get-url origin
```

从 origin URL 解析 `pathWithNamespace`（如 `ee/codewiz-agent`），写入 `session.repo`。

---

## 阶段 ② 开发

**入场前提**：`session.workItem` 已就绪，当前在有效 git 仓库内。
**出场判据**：分支已创建、代码已提交、`git push` 成功、`session.repo.branch` 已填充。

### Step 2.1 决定开发分支 🔀

默认分支名：
- 需求（task/subtask）：`feature/<slug>-<workitem-id>`
- 缺陷（bug）：`fix/<slug>-<workitem-id>`

slug 从需求标题按下列规则生成：ASCII 化、小写、空格转 `-`、去特殊字符。

询问用户："默认分支名 `<分支名>`，回车确认或输入自定义名"。

### Step 2.2 切换/创建分支 🤖

```bash
git fetch origin master && git checkout -b <branch> origin/master
```

若分支已存在于本地 → 提示是否 checkout 现有分支。

### Step 2.3 编码 🔀

正常与用户交互，AI 完成代码修改。此步允许长时间；每一次显著修改（如完成一个子任务）追加 `code_change` 事件到 session。

### Step 2.4 本地检查（可选） 🤖

若项目根有 `pom.xml` / `build.gradle` / `package.json` → 尝试对应的 lint/build/test 命令。失败向用户报告，是否继续由用户决定。

### Step 2.5 提交 & 推送 🤖

```bash
git add <files>
git commit -m "<type>: <description>"
git push -u origin <branch>
```

commit message 遵循 conventional commits 惯例（`feat:`/`fix:`/`refactor:` 等）。

---

## 阶段 ③ 提交

**入场前提**：分支已推送。
**出场判据**：MR 已创建、工作项已关联（合规）、提测单已创建。

### Step 3.1 创建 MR 🤖

```bash
ee-cli cr create \
  --source-branch <branch> \
  --target-branch master \
  --title '<title>' \
  -d '<description>'
```

将返回的 `mrIid`、`yunxiaoUrl` 写入 `session.mr`。

### Step 3.2 关联工作项 🤖（含类型校验 + 自动建子任务）

**类型校验**：若 `session.workItem.type == 'task'`（需求），云效不允许 MR 直接关联，**自动补建服务端子任务**（不要阻塞用户）：

```bash
# 1. 拿子任务 create-form 的 subTypeId（服务端子任务）
ee-cli pingcode workitem create-form --sub-type-code SUBTASK_SUBTYPE_SERVER \
  -w <parentWorkspaceId> --parent-id <parentTaskId>
# 从返回值取 subTypeId

# 2. 建子任务（沿用父需求的 workspace / owner / business_line 默认值）
ee-cli pingcode workitem create \
  --name '<parentTitle> - <MR 标题的动词短语>（服务端）' \
  --work-item-type subtask \
  --sub-type-id <subTypeId> \
  --owner <当前用户 email> \
  --business-line <parentBusinessLineKey> \
  --parent-id <parentTaskId> \
  -w <parentWorkspaceId>
# 从返回值取新子任务 id
```

将新子任务 id 写入 `session.workItem.subtaskId`，追加 `step_completed(create_subtask)` 事件、`cap-add --ai create_subtask`。**不需要征求用户同意**——这是流程内部的确定性优化。

**若 workItem.type 已经是 `subtask` / `bug`**：跳过上面的建子任务步骤，直接进行下一步。

**执行关联**：

```bash
ee-cli cr workitem associate -m <mrIid> -w <workitem-id>
```

其中 `<workitem-id>` 取值优先级：`session.workItem.subtaskId`（如果自动建过） → `session.workItem.id`（否则）。

**关联失败** → 才阻塞报错让用户处理（比如子任务 workspace 与 MR 项目不一致等罕见情况）。

### Step 3.3 发起提测 🔀

询问用户：

- 测试人邮箱（必填，可多；默认询问是否自测）
- 提测单标题（给候选：`<workitem-name>-提测` / `<branch>-提测` / `提测-MMDD`）

```bash
ee-cli delivery ready-test-branches <workitem-id>  # 拿 branch-id
ee-cli delivery test-submission create <workitem-id> \
  --title '<title>' \
  --test-user <email> \
  --branch-id <branch-id> \
  [--self-test]
```

将返回的 `approveFormId` 写入 `session.testSubmission`。

---

## 阶段 ④ 验证

**入场前提**：MR 存在、提测单已创建。
**出场判据**：部署成功、功能验证通过、CR 评论已处理。

### Step 4.1 部署到测试环境 🤖

用 `ee-cli ci run` 直接触发部署（新版 CLI 支持 `--deploy-env` 参数，无需手动网页填部署参数）：

```bash
# 找到部署流水线 pipeline-id（一般是「【开发阶段】<module>构建部署」）
ee-cli ci list  # 查看项目下所有流水线，选与本次改动模块对应的那条

# 触发部署到 SIT
ee-cli ci run <pipeline-id> -b <branch> --deploy-env sit --yes
# 可选：--deploy-lane <name> 指定泳道；--image-tag <tag> 指定镜像
```

`ci run` 内部阻塞轮询到终态（默认 30 分钟超时）：
- `status == success` → 从返回值取 `pipelineHistoryId` 写入 `session.deploy.historyId`，继续 Step 4.3
- `status == failed` → 立即 `step_failed`，附上 `ci error` 的失败诊断，让用户决定重试/放弃

**Step 4.2 部署状态确认**（原步骤）已合并进 4.1，`ci run` 本身返回终态。

### Step 4.3 功能验证 🔀

询问用户：

> "部署成功。要我调用新接口/跑一遍功能验证吗？（推荐）"

用户确认后由 AI 调用相应接口（如新增的 API），把请求 URL、响应关键字段写入 `verification` 事件。**每一次验证调用都必须落一条 `verification` 事件**（含 scenario 名称、request、关键 response、pass/fail 判定、依据），后续测试报告直接从事件流生成。

### Step 4.3.1 生成测试报告 🤖

功能验证完成后（无论几个 scenario），基于本次 `verification` 事件生成独立测试报告：

**输出路径**：`docs/e2e-reports/<workitem-id>-<yyyymmdd>-test.md`（与交付报告同目录，`-test` 后缀区分）

**内容模板**：
```markdown
# 测试报告：<workItem.title>（#<id>）

## 测试环境
- 部署环境：<sit|beta|prod>
- 部署流水线：<pipeline_url>
- 镜像：<image tag，如可从 ci detail 拿到>
- 测试时间：<verification 首条事件 timestamp> → <末条 timestamp>

## 测试范围
- 目标接口/功能：<从需求 + 代码 diff 归纳>
- 关联 MR：#<mrIid>

## 测试用例明细
| # | 场景 | 请求 | 关键响应 | 结果 | 依据 |
|---|------|------|---------|------|------|
| 1 | <scenario> | <method + url + 关键参数> | <status code, 关键字段值> | ✅/❌ | <判定理由> |
...

## 汇总
- 用例数：X · 通过：Y · 失败：Z
- 结论：<通过 / 未通过（列失败项）>
```

**同步**：
- 本地 MD 写入后，同样通过 `Skill(hi-docs)` 同步到 REDoc（父目录复用 `~/.claude/e2e-delivery/config.json` 里的 `redocParentId`）
- 测试报告的 shortcutId 回写 `session.report.testReportShortcutId`
- 交付报告（Step 5.4）里的"功能验证"一节要引用测试报告链接

**若 4.3 用户选择跳过验证** → 也要生成一份"未执行验证"的说明报告（一句话），保证报告完整性。

### Step 4.4 触发智能 CR 🤖

```bash
ee-cli cr ai-review <mrIid>
```

- 触发成功 → 等 AI 出评论后进入 Step 4.5
- 返回"该MR未开启智能CR，无法触发扫描" → 用 `ee-cli cr config get` 检查项目 `defaultEnableAiCodeReview`，若为 `0` 说明**项目侧未启用**，写 `step_completed(trigger_ai_review, result=skipped, notes="项目未启用智能 CR")` 直接跳过（这不是 skill 层能解决的，不算 cliMissing）

### Step 4.5 拉取 & 处理评论 🤖

```bash
ee-cli cr note list <mrIid>
```

有评论 → 分类为 AI/人工，依次向用户呈现，询问 accept/reject/delay/resolve 决定并执行：

- AI 评论：`ee-cli cr note mark <mrIid> -n <note-id> --status <accept|reject|delay> [--resolve]`
- 人工评论：`ee-cli cr note resolve <mrIid> -n <note-id>`

---

## 阶段 ⑤ 交付

**入场前提**：验证通过、评论处理完毕、**提测单已通过**。
**出场判据**：MR 已合并、需求状态已流转、报告已生成。

### Step 5.0 提测单状态强校验 🤖（合并前的硬卡点）

**任何情况下都必须先查提测单状态**，未通过不得进入 Approve/合并：

```bash
ee-cli delivery test-submission get <approveFormId>
```

判定规则：
- `status` 为「测试通过」/「pass」→ 继续 Step 5.1
- `status` 为「自测待确认」/「待测试」 → 询问用户确认后用 CLI 流转：
  ```bash
  ee-cli delivery test-submission operate <approveFormId> test_accept
  ```
- `status` 为「测试中」 → 阻塞，写 `human_gate_waiting`：
  > "提测单 #<id> 正在测试中，请等测试人完成后回复'继续'（或告诉我强制通过 → 走 `test_accept_force`）。"
- `status` 为「测试不通过」 → 阻塞并展示原因，用户修复代码后重跑流程

`operate` 支持的动作：`start_test / revoke / test_accept / test_reject / qa_confirm / test_accept_force`。所有流转都要**先问用户确认**（合并前的最后一道人工闸门），不做无 gate 自动流转。

### Step 5.1 Approve MR 🔀

询问用户："即将 approve MR #<mrIid>，确认？"

```bash
ee-cli cr approve <mrIid>
```

### Step 5.2 合并前卡点复核 🤖（合并前最后一道硬闸门）

**在 `cr merge` 之前必须执行 checklist 复核**，把所有服务端合并卡点列出来，任一 blocking 项未通过则阻断：

```bash
ee-cli cr checklist <mrIid>
```

判定规则：
- 遍历返回的 `items` 数组，任一项 `blocking: true` 且 `result != success` → **阻塞**：
  > "MR #<mrIid> 尚有合并卡点未通过：
  > - [名称]：[msg]（[handleAction]）
  > 
  > 请先解决这些卡点，完成后回复'继续'。"
- 全部 blocking 项 `result == success` → 继续 Step 5.3

**为什么单独一步而不合到 Step 5.0**：Step 5.0 只是提测单业务规则的兜底；`cr checklist` 是服务端**所有维度**的卡点复核（含 reviewer 通过、AI 评论标记、安全检查、准出合规、双写 diff 等）——两者互补。

### Step 5.3 合并 MR 🔀

询问用户："即将合并 MR，确认？"

```bash
ee-cli cr merge <mrIid>
```

**注意**：由于 `cr merge` 失败时可能返回空字符串 + exit 0（已知问题），合并后必须验证：

```bash
ee-cli cr status <mrIid> --skip-checks
```

`state == merged` 才算成功；否则报错让用户处理。

### Step 5.4 流转需求状态 🔀

```bash
ee-cli pingcode workitem states <workitem-id> -w <workspace-id>
```

将可流转状态列出让用户选择，然后：

```bash
ee-cli pingcode workitem transition <workitem-id> --status-id <status-id> -w <workspace-id>
```

### Step 5.5 生成报告 🤖

见 `report-template.md`。产出后回写 `session.report.localPath` 和 `session.report.redocShortcutId`，`session.status = completed`。
