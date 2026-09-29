## Description:

Builds and runs cross-platform automation workflows with scheduled, file-watch, webhook, manual trigger, conditional, and multi-step operation support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[careytian-ai](https://clawhub.ai/user/careytian-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Operations, content, data, support, and project teams can use this skill to design repeatable workflows for data sync, content publishing, report generation, monitoring alerts, and similar recurring business tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad command, file, and network authority for automation workflows.

Mitigation: Review each workflow before running it, restrict working directories and network destinations, and require explicit approval for command execution, uploads, publishing, file moves or deletes, scheduled runs, and file-watching workflows.

Risk: Scheduled or file-watching workflows can repeat unintended actions without direct supervision.

Mitigation: Use auditable logs, narrow triggers, clear stop controls, and conservative timeouts before enabling unattended workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/careytian-ai/skills/automation-workflow-builder)
- [Publisher profile](https://clawhub.ai/user/careytian-ai)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or structured workflow examples with code and command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May describe workflows that use command execution, file operations, network requests, scheduling, webhooks, notifications, and publishing actions.]

## Skill Version(s):

1.0.0 (source: release evidence, config.json, metadata.json, CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
