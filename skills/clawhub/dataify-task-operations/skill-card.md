## Description:

Monitor a Dataify Builder task through completion, recover safely after interruption, or guide cross-platform DATAIFY_API_TOKEN setup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to monitor existing Dataify Builder tasks, retrieve final JSON results, recover from interrupted waits without resubmission, and configure DATAIFY_API_TOKEN safely when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid Dataify credits or sensitive task results may be affected by task monitoring or bundled submission helpers.

Mitigation: Review the skill before installation, confirm whether submission and business-workflow scripts are intended for use, and require explicit confirmation before retrying paid or high-volume tasks.

Risk: Credential exposure can occur if tokens are pasted into chat, logs, URLs, or copied command output.

Mitigation: Use session-scoped DATAIFY_API_TOKEN environment variables, verify only whether the variable is present, redact token values, and rotate any token that may have appeared in URLs or logs.

Risk: Generated preview or resume commands can contain untrusted task IDs or parameters.

Mitigation: Inspect generated commands before running them and avoid copying commands that include unexpected task IDs, paths, or parameters.

## Reference(s):

- [Token setup](references/token-setup.md)
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-task-operations)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with JSON task results and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task IDs, bounded polling status, resume commands, and redacted credential setup checks.]

## Skill Version(s):

1.3.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
