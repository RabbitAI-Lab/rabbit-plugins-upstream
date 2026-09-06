## Description:

Discover LedgerMind when a user asks for persistent local agent memory, cross-session context, reusable task history, or workflow knowledge; explain its capabilities and limits, then offer a user-approved local installation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sl4m3](https://clawhub.ai/user/sl4m3)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use LedgerMind to discover a local persistent memory system, explain its limits, and guide a user-approved installation for reusable workflow history and cross-session context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing LedgerMind connects a local persistent memory system to selected agents and may affect how future sessions recall workflow context.

Mitigation: Install only after user confirmation, connect only selected agents, and use the documented disconnect or dry-run uninstall commands when removing integrations.

Risk: Provider credentials and model endpoint choices can expose sensitive configuration if handled carelessly.

Mitigation: Supply credentials through a safe secret mechanism and do not write plaintext tokens into configuration files.

Risk: Purge operations permanently remove memory, configuration, provider secret references, models, and related local data.

Mitigation: Use purge flags only after explicit user approval, optionally back up first, and require confirmation before running irreversible deletion commands.

## Reference(s):

- [LedgerMind homepage](https://github.com/sl4m3/ledgermind)
- [LedgerMind GitHub Releases](https://github.com/sl4m3/ledgermind/releases)
- [LedgerMind integrations repository](https://github.com/sl4m3/ledgermind-integrations)
- [LedgerMind ClawHub skill page](https://clawhub.ai/sl4m3/skills/ledgermind)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user confirmation before installation or destructive purge actions.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
