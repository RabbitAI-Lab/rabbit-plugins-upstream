## Description:

Guides agents in using the do CLI to manage personal tasks and habits and review life-tracking information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[robbeverhelst](https://clawhub.ai/user/robbeverhelst)

### License/Terms of Use:

MIT-0

## Use Case:

People and their agents use this skill to capture and review tasks, track habits, and plan work through the do CLI. Some commands change account data or communicate with other members.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI can modify tasks, habits, plans, and standards, despite the skill's limited-write description.

Mitigation: Review intended changes and require explicit user confirmation before cancellation, plan acceptance, or standards changes.

Risk: Agent commands can post messages or take actions affecting another member.

Mitigation: Require explicit user confirmation before agent posts or actions affecting another member.

Risk: Account API keys and external installers or packages may expose account access or introduce unreviewed code.

Mitigation: Use narrowly scoped keys, keep them out of shell history and transcripts, and verify external installers and packages before use.

## Reference(s):

- [do skill release on ClawHub](https://clawhub.ai/robbeverhelst/skills/do-cli)
- [do CLI documentation linked in the skill](https://github.com/robbeverhelst/do)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Text or Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI responses are JSON when piped and formatted text in an interactive terminal.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
