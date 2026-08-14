## Description:

Komari (github.com). Use this skill for ANY Komari request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to administer Komari through an OOMOL-connected account, including client, node, metrics, notification, clipboard, session, and settings workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform write and destructive Komari administration actions.

Mitigation: Confirm the exact target, payload, and intended effect before approving state-changing or destructive actions.

Risk: Some actions can expose secrets, database settings, enrollment tokens, or command output.

Mitigation: Review returned data before sharing it and avoid copying sensitive values into public logs or messages.

Risk: Remote command execution on clients is a powerful administrative capability.

Mitigation: Run remote commands only after explicit approval of the command, target clients, and expected operational impact.

## Reference(s):

- [Komari homepage](https://github.com/komari-monitor/komari)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-komari)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
