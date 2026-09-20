## Description:

Provides guidance for agents to operate Excel workbooks through the OOMOL excel connector and oo CLI, including reading, creating, updating, deleting, formatting, sorting, filtering, and workbook session workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill when an agent needs to inspect, create, update, format, sort, filter, or delete Excel workbook data through an OOMOL-connected Excel account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions may lead an agent to run an unverified remote installer script.

Mitigation: Review the oo CLI installation path first and prefer official installation documentation or a verified installer before allowing installation.

Risk: Write and destructive Excel actions can overwrite, delete, sort, clear, or restructure workbook data.

Mitigation: Require explicit user approval for the exact target, payload, and expected effect before running state-changing Excel operations.

## Reference(s):

- [ClawHub Excel skill page](https://clawhub.ai/oomol/skills/oo-excel)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Microsoft Excel](https://www.microsoft.com/microsoft-365/excel)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with shell command examples and JSON payload and response conventions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs agents to inspect live action schemas before constructing connector payloads.]

## Skill Version(s):

1.0.4 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
