## Description:

DeskTime lets agents operate DeskTime through an OOMOL-connected account to read company, employee, and project data and create projects via the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Teams and agents using DeskTime can inspect live action schemas, retrieve company settings, employee time-tracking data, employee lists, and active projects, and create DeskTime projects after confirming write payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may lead users to execute mutable remote installer scripts directly in a shell.

Mitigation: Review the OOMOL CLI installation source first and prefer a signed, version-pinned, checksum-verified installer or trusted package-manager method.

Risk: The skill can create DeskTime projects and optionally associated tasks.

Mitigation: Confirm the exact action payload and expected effect with the user before running write actions.

## Reference(s):

- [DeskTime homepage](https://desktime.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-desktime)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs agents to fetch live connector schemas before building action payloads and to confirm state-changing DeskTime operations before execution.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
