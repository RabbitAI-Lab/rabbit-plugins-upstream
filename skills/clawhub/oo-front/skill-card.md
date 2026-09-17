## Description:

Front enables agents to read, create, and update Front contacts and teammates through the OOMOL-connected oo CLI instead of calling the Front API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and business operations users can use this skill to let an agent inspect Front connector schemas, run read operations, and perform confirmed contact create or update actions in an OOMOL-connected Front workspace.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can include direct execution of remote oo CLI installer scripts.

Mitigation: Review the installer source and prefer a pinned, signed, or checksum-verified oo CLI installer before running installation commands.

Risk: Front create and update actions can change workspace contact data.

Mitigation: Confirm the exact JSON payload and expected effect with the user before allowing the agent to run write actions.

## Reference(s):

- [Front homepage](https://front.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Front ClawHub skill page](https://clawhub.ai/oomol/skills/oo-front)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON action payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read actions can run directly; write actions require confirmation of the exact payload and effect before execution.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
