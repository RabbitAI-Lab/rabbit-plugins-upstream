## Description:

团队任务管家 helps agents manage a local JSON-backed team task ledger with creation, updates, comments, archiving, backups, restricted restore, and export-oriented summaries while leaving reminders, notifications, identity, and authorization to external integrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[djoldwang](https://clawhub.ai/user/djoldwang)

### License/Terms of Use:

MIT-0

## Use Case:

Teams and their integration developers use this skill to maintain a shared local task ledger, record task changes and comments, archive completed work, and produce JSON, CSV, Markdown, or text summaries. Deployments must provide identity, permissions, calendar rules, notification routing, and reminder scheduling outside the skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The storage script records an actor label but does not authenticate users or enforce business permissions.

Mitigation: Require the integration layer to authenticate the current actor and enforce team permissions before any create, update, status, comment, export, archive, reopen, restore, or notification workflow.

Risk: The skill records reminder receipts but does not schedule reminders or send notifications.

Mitigation: Use an external scheduler and notification service with authorization checks and a task ID plus reminder-slot idempotency key before reporting that a message was sent.

Risk: Local ledger integrity depends on all writers using the provided storage entry point and on a private local data directory.

Mitigation: Keep the ledger on a local macOS or Linux filesystem owned by the runtime user, prevent other users from writing to the data and backup directories, and route all writes through scripts/task_store.py.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/djoldwang/skills/team-tasks)
- [Safe Storage Interface](references/storage.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, JSON, CSV]

**Output Format:** [Markdown guidance, shell command examples, JSON operation objects, and JSON/CSV/text task exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local files only; write operations must go through the bundled Python storage script and external integrations handle identity, permissions, reminders, and notifications.]

## Skill Version(s):

1.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
