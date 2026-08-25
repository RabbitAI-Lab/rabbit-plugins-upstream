## Description:

Turn a written holiday homework list into one holiday homework voice clip per labeled cue.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers and education-support users use this skill to convert an existing holiday homework assignment list into a labeled pack of short spoken instruction clips. It plans the clip list first, then guides optional voice cloning and paid speech synthesis with consent, billing, and recovery checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill links a Beatra account and stores a shared local token for broad Beatra access.

Mitigation: Install only where that account access is acceptable, keep the token out of chat, logs, and command arguments, and revoke the device authorization when the skill is no longer needed.

Risk: Voice cloning can upload chosen voice samples and speech generation can spend credits.

Mitigation: Require explicit voice-rights confirmation and separate approval for cloning and speech synthesis before any paid call, then use stable request IDs to avoid duplicate charges during recovery.

Risk: Silent automatic updates are enabled by default.

Mitigation: Disable automatic updates for environments that require explicit change approval, and review the package before re-enabling updates.

## Reference(s):

- [Holiday homework voice workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [MCP connection](references/mcp-connection.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Tasks and results](references/tasks-and-results.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/holiday-homework-voice)
- [Beatra skill homepage](https://beatra.ai/skills/holiday-homework-voice)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance, Files]

**Output Format:** [Markdown guidance with JSON payload examples and shell commands; successful speech tasks produce MP3 audio files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Plans 8 to 20 labeled clips by default and keeps one spoken homework instruction per clip.]

## Skill Version(s):

0.1.1 (source: server release metadata and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
