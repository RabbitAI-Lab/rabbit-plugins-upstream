## Description:

Use this skill for CompanyCam requests involving reading, creating, updating, and deleting CompanyCam data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external agents, and developers use this skill to operate CompanyCam projects, tags, company records, and user lookups through an OOMOL-connected CompanyCam account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup includes remote installer commands that run directly in a shell.

Mitigation: Install the oo CLI only through a verified, pinned, or inspectable method, and do not let an agent run remote installer commands blindly.

Risk: Write and destructive CompanyCam actions can change, archive, restore, or delete account data.

Mitigation: Confirm the exact action, target, and payload with the user before any write action, and require explicit approval before destructive actions.

## Reference(s):

- [CompanyCam Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-companycam)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [CompanyCam Homepage](https://companycam.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return JSON data from CompanyCam connector actions when commands are executed.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
