## Description:

Read and write Microsoft To Do via shared Outlook Graph auth: enumerate task lists, read/filter tasks, and create, update, complete, or delete tasks (writes require --apply plus a typed-YES prompt or an explicit --yes flag).

This skill is ready for commercial/non-commercial use.

## Publisher:

[guoxh](https://clawhub.ai/user/guoxh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to inspect Microsoft To Do task lists and manage tasks for the signed-in Outlook or Microsoft 365 account through Microsoft Graph.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The shared Microsoft Graph OAuth setup grants persistent write access to tasks and also includes calendar and contact write scopes.

Mitigation: Prefer a dedicated To Do-only OAuth setup when broader Outlook-family access is not acceptable, or install only after reviewing and accepting the shared-scope consent model.

Risk: Task creation, update, completion, and deletion can modify the signed-in user's Microsoft To Do data.

Mitigation: Keep the default dry-run behavior for review, and execute writes only with --apply plus typed YES or an explicit --yes flag in non-interactive runs.

## Reference(s):

- [ClawHub outlook-todo skill page](https://clawhub.ai/guoxh/skills/outlook-todo)
- [Microsoft Graph To Do Notes](references/graph-todo.md)
- [Allowed network endpoint: Microsoft Graph](https://graph.microsoft.com)
- [Allowed network endpoint: Microsoft login](https://login.microsoftonline.com)

## Skill Output:

**Output Type(s):** [text, json, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands; script output can be summary text, JSON, IDs, or raw Microsoft Graph responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write operations default to dry-run and require --apply plus typed YES or --yes; use requires bash, jq, curl, python3, and shared Outlook Graph auth.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
