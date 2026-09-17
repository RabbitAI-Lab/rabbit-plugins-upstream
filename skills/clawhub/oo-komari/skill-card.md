## Description:

Komari lets an agent operate Komari through an OOMOL-connected account for reading, creating, updating, and deleting Komari data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Komari monitoring resources through the OOMOL oo CLI connector, including clients, nodes, metrics, notifications, sessions, settings, audit logs, and remote execution tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform high-impact Komari administration, including writes, deletions, settings changes, secret-revealing reads, and remote command tasks.

Mitigation: Require explicit user confirmation for write, destructive, secret-revealing, and remote command actions, and verify the exact payload against the live schema before running the command.

Risk: First-time setup includes installer commands that execute remote scripts directly.

Mitigation: Use a verified installation path, avoid running one-line installers blindly, and run setup only after a command failure indicates that the CLI, authentication, or connection is missing.

Risk: Remote command execution through Komari can run shell commands on selected clients.

Mitigation: Treat remote command execution as a sensitive action; confirm the target clients and command text before use.

## Reference(s):

- [ClawHub Komari skill page](https://clawhub.ai/oomol/skills/oo-komari)
- [Komari homepage](https://github.com/komari-monitor/komari)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [OOMOL Komari app connection](https://console.oomol.com/app-connections?provider=komari)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline bash commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses schema-first oo connector commands and returns single-stream guidance for executing Komari actions.]

## Skill Version(s):

1.0.2 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
