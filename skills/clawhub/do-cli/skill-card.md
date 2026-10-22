## Description:

Install and use the `do` CLI to manage personal tasks, habits, and related life-tracking records through the do app.

This skill is ready for commercial/non-commercial use.

## Publisher:

[robbeverhelst](https://clawhub.ai/user/robbeverhelst)

### License/Terms of Use:

MIT-0

## Use Case:

External users can use the skill to capture and review tasks, complete or snooze tasks, log habits, and read life-tracking records with the `do` CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security review recommends caution because the skill may save sensitive details from casual conversation without asking and understates its ability to change records.

Mitigation: Require explicit user permission before saving relationship notes or other sensitive details, and confirm before changing records.

Risk: An API key can provide access to tenant records, and downloaded installers require source verification.

Mitigation: Use a user-provided, least-privilege scoped API key; verify the package source and review any downloaded installer before running it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/robbeverhelst/skills/do-cli)
- [Project homepage listed by the skill](https://github.com/robbeverhelst/do)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Text, Configuration guidance]

**Output Format:** [Command-line instructions and JSON or human-readable CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI output is JSON when piped and formatted text in an interactive terminal.]

## Skill Version(s):

1.0.14 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
