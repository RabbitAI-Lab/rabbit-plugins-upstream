## Description:

V2EX (v2ex.com). Use this skill for V2EX requests to read, create, update, and delete data through the V2EX connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate an authenticated V2EX account through OOMOL's connector, including reading member, node, topic, reply, notification, hot-topic, and latest-topic data. It also supports confirmed write actions such as boosting topics, creating tokens, setting sticky topics, and deleting notifications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes commands that run remote installer scripts directly in the user's shell.

Mitigation: Use a verified official install path or review the installer before execution.

Risk: The skill connects an authenticated V2EX account through OOMOL's connector.

Mitigation: Use the skill only when the user trusts OOMOL and has intentionally connected the V2EX account.

Risk: Write and destructive actions can change account state, including boosting topics, creating tokens, setting sticky topics, and deleting notifications.

Mitigation: Confirm the exact action, target, and payload with the user before running write or destructive commands.

## Reference(s):

- [ClawHub V2EX skill page](https://clawhub.ai/oomol/skills/oo-v2ex)
- [V2EX homepage](https://www.v2ex.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, PowerShell commands, text URLs, and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the oo CLI and may return JSON responses from V2EX connector actions.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
