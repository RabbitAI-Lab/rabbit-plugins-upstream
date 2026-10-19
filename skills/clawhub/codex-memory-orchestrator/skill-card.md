## Description:

Helps agents preserve continuity across long conversations through turn reminders, checkpoints, memory summaries, and recovery packages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

MIT

## Use Case:

Developers and other agent users use this skill to track conversation length, retain important decisions, and hand off work to a new conversation without losing context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Always-on monitoring and broad session scans can expose more local conversation history than intended.

Mitigation: Review or disable persistent hooks and scheduled scans; prefer manual or dry-run operation and confirm the project and session range before export.

Risk: Shared cross-agent state may reveal activity across projects or agents.

Mitigation: Review the cross-agent registry before enabling it and restrict access to local state files.

Risk: Clipboard or application handoff may put recovery text in the wrong destination.

Mitigation: Confirm the target app and recovery text before any real handoff; use dry-run mode first.

## Reference(s):

- [Recovery package templates](artifact/references/templates.md)
- [Agent handoff capabilities](artifact/references/agent-gateways.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration guidance]

**Output Format:** [Markdown summaries and recovery packages, text prompts, and optional JSON status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write local checkpoints, recovery indexes, and conversation state.]

## Skill Version(s):

1.6.0 (source: frontmatter and CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
