## Description:

Operate Amilia through an OOMOL-connected account to search and read program and activity data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to retrieve Amilia activities and programs through the OOMOL oo CLI after the account is connected.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup directs users to run remote installer scripts in a shell.

Mitigation: Review setup commands before installing, and prefer a pinned, signed, or checksum-verified oo CLI release.

Risk: Connector actions can access data from the connected Amilia account.

Mitigation: Connect only an Amilia account whose program and activity data may be exposed to OOMOL connector actions.

Risk: Future or schema-discovered write and destructive actions could change or remove Amilia data.

Mitigation: Inspect the live action schema and confirm the exact payload, effect, and target with the user before running any action tagged write or destructive.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-amilia)
- [Amilia homepage](https://www.amilia.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing payloads; listed routine actions are read-only.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
