## Description:

Daily (daily.co). Use this skill for ANY Daily request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Daily action schemas and manage Daily rooms, meeting tokens, and domain configuration through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes a remote installer that runs immediately on the user's machine.

Mitigation: Review the installer path before use and prefer manually downloading or package-manager installing the oo CLI from a verifiable source.

Risk: The skill can create, update, or delete Daily rooms and create meeting tokens.

Mitigation: Confirm the exact room, token, or configuration change before running write or destructive actions.

## Reference(s):

- [ClawHub Daily Skill](https://clawhub.ai/oomol/skills/oo-daily)
- [Daily homepage](https://www.daily.co/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke Daily read, write, and destructive actions through the oo CLI after user confirmation where required.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
