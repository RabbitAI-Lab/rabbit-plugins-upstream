---
name: mochi-work-reports
description: "Build daily and weekly work reports from dated work evidence, keeping completed, ongoing and blocked items separate and checking reporting periods and recorded durations. Use for 工作日报与周报."
metadata: {"openclaw":{"requires":{"bins":["node"]},"homepage":"https://mochilab.bz"}}
---

# 工作日报与周报 / Daily and Weekly Work Reports

Transform actual work notes into a report a teammate or manager can check. This Skill maintains a small, dated work ledger, retrieves the requested period and helps draft a readable account of progress. It is useful for 日报、周报、项目进展汇总 and preparing a handover from supplied work records.

## Gather a work item with its evidence

Ask for the reporting dates and intended reader when they affect the report. A phrase such as “this week” needs a calendar range in the user's timezone. Convert dates to `YYYY-MM-DD` before adding records. Keep the work date separate from when the note was entered.

Every ledger item has a title, a description, a completion state and one or more evidence references. Evidence may be a user-provided note path, a permitted commit reference, or a clearly labeled user-statement identifier. Retain supplied facts as supplied; do not describe a user statement as independently verified. Access external trackers or repositories only through tools and permissions already available for this task.

Use these states consistently:

| State | Record it when | How it appears in the draft |
|---|---|---|
| `done` | The stated work has been completed | Completed work and its evidenced result |
| `in-progress` | Work has started and remains unfinished | Current progress and the next concrete step |
| `blocked` | A dependency or problem prevents progress | The obstacle, its source and any recorded request for help |

Store only actual durations. `minutes` is optional and accepts an integer from 0 to 1440 per record. Missing time remains missing. Neither item count nor a partially recorded duration establishes an entire working day's hours.

## Add the record before drafting

Write an input file such as `work-add.json` in the active agent workspace:

```json
{
  "action":"add",
  "requestId":"work-20261023-login-01",
  "date":"2026-10-23",
  "title":"完成登录页错误提示调整",
  "detail":"依据用户提供的提交说明，完成错误提示文案和显示位置调整。",
  "status":"done",
  "evidence":["user-statement:login-update-01"],
  "minutes":90
}
```

Invoke the ledger helper and keep the returned `record.id`:

```text
node "{baseDir}/scripts/run.mjs" --workspace "CURRENT_WORKSPACE" --input "work-add.json"
```

Reuse the same request ID and identical JSON after a retry. A changed payload with the same ID is rejected. Check whether an item was already recorded before adding it again. The helper is an append-only ledger: it has `add` and `report`, not an edit or status-update operation. If the user supplies a correction, retain its relationship to the earlier record and reconcile the latest stated facts in the draft without double-counting the event.

## Select a daily or weekly interval

Prepare another request file with the inclusive range:

```json
{"action":"report","from":"2026-10-19","to":"2026-10-23"}
```

Run the same helper using that file. Review `records` and the three `sections` before writing prose. Items outside the interval stay out of the report. Inspect `recordedMinutes` alongside `recordsWithoutDuration`; show the former as recorded time rather than total time worked. An empty interval returns an empty report result, so ask for missing notes or state that no ledger items were recorded for those dates.

## Compose the report from the selected evidence

Open with the period and a concise overview of actual progress. Group the body into completed work, ongoing work and blockers. Under each item, retain a source reference and explain the recorded result in language suitable for the intended reader. Add next steps only when they were supplied or label them as proposals for confirmation. A request for a polished report does not establish new revenue, conversion, performance or productivity figures.

A practical Chinese format is：报告周期 → 已完成事项 → 进行中事项 → 阻碍与需协助事项 → 下一步安排 → 依据。没有对应记录的栏目可以省略，不把“尚未提供”改写成“全部完成”。

When a file is requested, save the final Markdown through the host's file-writing tool and read it back. The helper only returns ledger data; it does not send a message or automatically schedule the next report. Deliver a report to a named recipient only when the user requests that delivery. For recurring preparation, use the host's separate scheduling capability and keep the agent, workspace and recipient explicit.

## Ledger location and operational checks

The ledger is stored at `.mochilab/mochi-work-reports/state.json` inside the current workspace. Other agents' workspaces remain separate. Writes use a lock and atomic replacement; a busy response means another operation is active, so preserve its lock and retry later. A failed add leaves the prior ledger intact. Keep note text in JSON files, not executable command strings. Required runtime: Node.js 24.16+, active-workspace read/write access and the agent's configured model. No MochiLab account key, currency configuration or external service is needed by this local ledger. Field limits and response details are in [references/input.md](references/input.md).
