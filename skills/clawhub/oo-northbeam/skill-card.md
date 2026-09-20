## Description:

Helps agents operate Northbeam through an OOMOL-connected account by inspecting connector schemas and running read-only Northbeam data actions with the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and operators use this skill to query Northbeam attribution, breakdown, metrics, daily spend, and hourly spend data through a connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup instructs users to pipe downloaded installer scripts directly into a shell.

Mitigation: Review the installer path first and prefer a pinned package, signed release, checksum verification, or manual installer inspection before installation.

Risk: Read-only Northbeam actions may expose business spend and attribution data through the connected OOMOL account.

Mitigation: Use an account with appropriate access scope and share returned data only with authorized recipients.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-northbeam)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Northbeam Homepage](https://www.northbeam.io)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses from the connector are expected as JSON with data and meta.executionId fields.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
