## Description:

Komari lets agents operate Komari through an OOMOL-connected account using the `oo` CLI connector for reading, creating, updating, and deleting Komari data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to administer Komari through OOMOL-managed credentials, including client, node, metrics, ping, notification, session, settings, and audit-log operations. Write, destructive, secret-returning, and remote command actions require review and explicit approval before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can trigger high-impact Komari operations, including destructive deletes, settings changes, session revocation, metric migration, and remote command execution.

Mitigation: Require explicit user approval for write, destructive, provider/settings, and remote command actions, and confirm the target, payload, and expected effect before execution.

Risk: Some read actions can return sensitive material such as enrollment tokens, provider secrets, database DSNs, or command output.

Mitigation: Run secret-returning reads only when needed, avoid exposing or logging returned secrets, and summarize sensitive values instead of repeating them verbatim unless the user explicitly requests them.

Risk: The first-time setup instructions include one-line installer commands that execute downloaded shell or PowerShell scripts.

Mitigation: Prefer the official install guide with verification where possible and avoid automatic CLI installation from piped installer commands.

## Reference(s):

- [Komari homepage](https://github.com/komari-monitor/komari)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-komari)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce `oo connector schema` and `oo connector run` commands, JSON payload guidance, and interpretation of JSON connector responses.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
