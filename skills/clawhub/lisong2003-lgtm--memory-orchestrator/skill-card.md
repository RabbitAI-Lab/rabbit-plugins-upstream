## Description:

Helps Codex users carry context across long conversations by tracking turns, retrieving project memory, and preparing checkpoints and handoff summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

MIT-0

## Use Case:

Developers using Codex can monitor long conversations, save project decisions and next steps, and prepare concise handoffs for a new session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to local Codex session history and persistent memory may expose sensitive conversations or mix projects.

Mitigation: Limit access to known project and session paths, confirm the scope before exporting or compressing history, and review stored memory files.

Risk: Scheduled monitoring can continue reading session history after an individual handoff is complete.

Mitigation: Enable scheduling only when needed, and provide a clear way to disable the scheduled task and remove memory files.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/lisong2003-lgtm/skills/memory-orchestrator)
- [Recovery package templates](references/templates.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Text reminders and Markdown checkpoints or handoff packages; optional JSON session state]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-scoped summaries; local memory persistence and optional scheduled monitoring.]

## Skill Version(s):

1.2.0 (source: ClawHub release metadata, frontmatter, changelog, manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
