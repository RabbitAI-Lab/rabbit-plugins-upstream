## Description:

ExhibitDay helps agents read, create, update, and delete ExhibitDay events and tasks through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operations teams use this skill to manage ExhibitDay events and tasks from an agent through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installer setup can execute remote installation scripts if the oo CLI is missing.

Mitigation: Review installer commands before use and prefer a trusted package or official installation instructions.

Risk: Write and destructive actions can change or delete ExhibitDay events and tasks.

Mitigation: Confirm the exact target record and payload with the user before create, update, or delete actions.

Risk: Connector schemas can vary over time, so stale payload assumptions may fail or target the wrong fields.

Mitigation: Inspect the live action schema before building each payload and match the schema exactly.

## Reference(s):

- [ClawHub ExhibitDay Skill](https://clawhub.ai/oomol/skills/oo-exhibitday)
- [ExhibitDay Homepage](https://www.exhibitday.com)
- [oo CLI Repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.0 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
