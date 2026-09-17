## Description:

Altiria (altiria.com). Use this skill for Altiria requests such as reading, creating, updating, and deleting data through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Altiria contacts, groups, and SMS workflows from an OOMOL-connected account. It supports schema inspection before actions, read operations, contact create/update/delete actions, and SMS sending with confirmation safeguards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may execute a remote installer directly.

Mitigation: Review the installer source and prefer a verified package or checksum before running setup commands.

Risk: Contact writes, contact deletion, and SMS sending can change account state or send messages.

Mitigation: Approve these actions only after the exact target, payload, and expected effect are clear.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-altiria)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Altiria homepage](https://www.altiria.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo connector schemas before constructing action payloads; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
