## Description:

Helps OpenClaw agents exchange signed messages with paired OpenClaw or Hermes peers and manage contacts, access controls, screening, inbox review, and recovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[clawreefantenna](https://clawhub.ai/user/clawreefantenna)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users and developers use this skill to send messages to approved conversations on paired OpenClaw or Hermes peers, inspect connections, and review or screen incoming messages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package retains a legacy setup path that can expose untrusted inbound messages to an unsandboxed relay agent with Bash approval.

Mitigation: Use only the native v1.6.8 plugin workflow; avoid legacy installation, setup, pairing and inbox commands, and remove or isolate any existing relay agent and exec allowlist before enabling.

Risk: Gateway configuration changes and exposed contact or bearer files can affect messaging access.

Mitigation: Review gateway changes before enabling and protect bearer credentials and contact files.

## Reference(s):

- [Antenna User Guide](references/USER-GUIDE.md)
- [Native plugin and operator reference](plugin/README.md)
- [Migration guide](plugin/MIGRATION.md)
- [Backup and recovery guide](references/BACKUP-AND-READINESS.md)
- [Project repository (skill metadata)](https://github.com/ClawReefAntenna/antenna-openclaw)
- [ClawReef homepage (skill metadata)](https://clawreef.io/)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Messaging requires paired peers and receiver-approved destinations.]

## Skill Version(s):

1.6.8 (source: skill metadata, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
