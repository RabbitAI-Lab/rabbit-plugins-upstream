# Session 文件 Schema

**路径**：`~/.claude/e2e-sessions/<workitem-id>.json`

## 顶层结构

```json
{
  "sessionId": "e2e-<workitem-id>-<yyyymmdd>-<hhmm>",
  "workItem": { ... },
  "repo": { ... },
  "status": "in_progress | completed | aborted",
  "currentPhase": "prepare | develop | submit | verify | deliver | done",
  "currentStep": "<step-name>",
  "startedAt": "<ISO 8601 with timezone>",
  "updatedAt": "<ISO 8601>",
  "completedAt": "<ISO 8601> | null",
  "phases": [ ... ],
  "events": [ ... ],
  "capabilities": { ... },
  "mr": { ... },
  "testSubmission": { ... },
  "report": { ... }
}
```

## 子字段

### workItem

```json
{
  "id": 951526,
  "type": "task | bug | subtask",
  "title": "skillhubopenapi 需求",
  "url": "https://pingcode2.devops.xiaohongshu.com/work-item-detail/951526",
  "workspaceId": 60,
  "createdBySkill": false
}
```

`createdBySkill: true` 表示本次 skill 通过模式 B 新建了该工作项。

### repo

```json
{
  "path": "ee/codewiz-agent",
  "workspace": "/Users/cp/developer/java/codewiz-agent",
  "branch": "feature/skill-openapi-951526"
}
```

### phases

```json
[
  {
    "name": "prepare | develop | submit | verify | deliver",
    "status": "pending | in_progress | completed | failed",
    "startedAt": "<ISO 8601> | null",
    "completedAt": "<ISO 8601> | null",
    "durationMs": 12000
  }
]
```

初始化时预填 5 项，`status: pending`。

### events

事件是 append-only 的时间序列。类型：

| type | 含义 | 必需字段 |
|------|------|---------|
| `phase_started` | 阶段开始 | `phase` |
| `phase_completed` | 阶段完成 | `phase`, `durationMs` |
| `step_started` | 步骤开始 | `phase`, `step` |
| `step_completed` | 步骤完成 | `phase`, `step`, `durationMs`, `action`, `result` |
| `step_failed` | 步骤失败 | `phase`, `step`, `action`, `errorMessage` |
| `human_gate_waiting` | 等待人工介入 | `phase`, `step`, `reason` |
| `human_gate_resumed` | 人工介入结束 | `phase`, `step`, `resumedAt`, `waitDurationMs` |
| `verification` | 功能验证记录 | `phase: 'verify'`, `request`, `response` |

每条 event 都包含：

```json
{
  "timestamp": "<ISO 8601>",
  "type": "<one of above>",
  "phase": "<phase name>",
  "step": "<step name>",
  "action": "<原始命令或动作描述>",
  "result": "success | failure | null",
  "durationMs": <number> | null,
  "errorMessage": "<string> | null",
  "notes": "<any extra info> | null"
}
```

### capabilities

运行时汇总：

```json
{
  "aiCompleted": ["get_workitem", "create_branch", "create_mr"],
  "humanRequired": ["deploy_to_test", "trigger_smart_cr"],
  "cliMissing": ["ci run 部署参数透传", "cr revert"]
}
```

`cliMissing` 由 skill 在遇到人工阻塞时归纳（例如"部署失败因为 ci run 不支持部署参数" → 追加"ci run 部署参数透传"）。

### mr / testSubmission / report

```json
"mr": {
  "iid": 384,
  "url": "https://yunxiao.devops.xiaohongshu.com/cr/details?mrId=384",
  "state": "opened | merged | closed"
},
"testSubmission": {
  "id": 72812,
  "testUsers": ["chenpeng2@xiaohongshu.com"]
},
"report": {
  "localPath": "docs/e2e-reports/951526-20260708.md",
  "redocShortcutId": "76c439a85a5a480d3f82cb0f0c0000ef",
  "testReportLocalPath": "docs/e2e-reports/951526-20260708-test.md",
  "testReportShortcutId": "abc123..."
}
```

## 初始化模板

新建 session 时写入：

```json
{
  "sessionId": "...",
  "workItem": {},
  "repo": {},
  "status": "in_progress",
  "currentPhase": "prepare",
  "currentStep": null,
  "startedAt": "<now>",
  "updatedAt": "<now>",
  "completedAt": null,
  "phases": [
    {"name": "prepare", "status": "pending", "startedAt": null, "completedAt": null, "durationMs": null},
    {"name": "develop", "status": "pending", "startedAt": null, "completedAt": null, "durationMs": null},
    {"name": "submit", "status": "pending", "startedAt": null, "completedAt": null, "durationMs": null},
    {"name": "verify", "status": "pending", "startedAt": null, "completedAt": null, "durationMs": null},
    {"name": "deliver", "status": "pending", "startedAt": null, "completedAt": null, "durationMs": null}
  ],
  "events": [],
  "capabilities": {"aiCompleted": [], "humanRequired": [], "cliMissing": []},
  "mr": null,
  "testSubmission": null,
  "report": {"localPath": null, "redocShortcutId": null, "testReportLocalPath": null, "testReportShortcutId": null}
}
```

## 写入操作 — 必须走 helper 脚本

**禁止**用 inline python 手拼 event JSON。**必须**走 `scripts/session.py`，理由：

- helper 自动填 `timestamp`、`durationMs`（比对上一条 `step_started`）、`waitDurationMs`（比对上一条 `human_gate_waiting`）、更新 `updatedAt`
- helper 维护 `phases[].startedAt/completedAt/durationMs` 一致性
- 手写 inline python 曾出现过 `durationMs` 全 null、`step_started` 漏写的问题，直接影响报告质量

**Helper 路径**（skill 装载后固定）：`~/.cc-mirror/codewiz-cc/config/skills/e2e-delivery/scripts/session.py`

**常用命令**（`$SF` = session 文件路径）：

```bash
# 初始化（新建 session）
python3 $HELPER init $SF --workitem-id 951526 --workitem-type task \
  --workitem-title "xxx" --workitem-url "https://..." --workspace-id 60

# 阶段
python3 $HELPER phase-start $SF prepare
python3 $HELPER phase-end   $SF prepare

# 步骤（durationMs 自动计算）
python3 $HELPER step-start $SF prepare get_workitem --action "ee-cli pingcode workitem get 951526"
python3 $HELPER step-end   $SF prepare get_workitem --result success

# 步骤失败
python3 $HELPER step-end $SF verify deploy_to_test --result failure --error "image_tag 不能为空"

# 人工阻塞（waitDurationMs 自动计算）
python3 $HELPER gate-wait   $SF verify deploy_to_test --reason "手动网页部署"
python3 $HELPER gate-resume $SF verify deploy_to_test

# 功能验证（记 request/response 供测试报告使用）
python3 $HELPER verification $SF "keyword=skill 过滤" \
  --request "GET /openapi/.../team/5/skills?keyword=skill" \
  --response "code=200, total=6" --result success

# 能力标记
python3 $HELPER cap-add $SF --ai get_workitem
python3 $HELPER cap-add $SF --human deploy_to_test --cli-missing "ci run 部署参数透传"
python3 $HELPER cap-remove $SF --cli-missing "ci run 部署参数透传"  # 修复后移除

# 结构化字段（mr / testSubmission / report / repo 等）
python3 $HELPER set $SF --path repo.branch --value feature/xxx
python3 $HELPER set $SF --path mr --value '{"iid":388,"url":"...","state":"opened"}' --json

# 收尾
python3 $HELPER done $SF

# 查看当前进度（人类可读）
python3 $HELPER show $SF
```

**执行铁律**：
- 任何 step 开始前 → `step-start`（不能省，否则 durationMs 算不出）
- 任何 step 结束时 → `step-end`（`--result` 必填）
- 任何人工阻塞 → 先 `gate-wait`，用户回复后 `gate-resume`
- 阶段切换 → `phase-start` / `phase-end`
- 完成流程 → `done`

违反以上任一 → 报告字段会缺失，属于 skill 执行 bug。
