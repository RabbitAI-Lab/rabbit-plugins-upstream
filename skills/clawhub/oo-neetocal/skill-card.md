## Description:

NeetoCal enables agents to search and read bookings, scheduling links, and availability through an OOMOL-connected NeetoCal account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve NeetoCal bookings, scheduling links, and available slots from an OOMOL-connected account. The skill is intended for read-only calendar scheduling workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Use an official, verifiable installer path where possible, inspect installer contents before execution, and avoid running pasted curl-to-shell or PowerShell invoke-expression commands blindly.

Risk: The skill requires connecting an OOMOL account to NeetoCal.

Mitigation: Install and use the skill only when the user is comfortable with OOMOL's oo CLI and the connected NeetoCal account permissions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-neetocal)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [NeetoCal homepage](https://www.neeto.com/neetocal)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return JSON data from oo CLI connector actions.]

## Skill Version(s):

1.0.2 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
