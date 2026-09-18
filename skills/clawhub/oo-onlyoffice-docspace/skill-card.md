## Description:

ONLYOFFICE DocSpace helps agents search and read DocSpace account, room, folder, and user data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to search and read ONLYOFFICE DocSpace account, room, folder, and user data through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute downloaded code immediately.

Mitigation: Review the OOMOL CLI installation path and prefer a verified package, pinned release, checksum, or official installer that can be inspected before execution.

Risk: DocSpace data access depends on the OOMOL connector account configured by the user.

Mitigation: Confirm the connected OOMOL account and ONLYOFFICE DocSpace permissions before using the skill for sensitive data lookup.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-onlyoffice-docspace)
- [ONLYOFFICE DocSpace homepage](https://www.onlyoffice.com/docspace.aspx)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include live DocSpace connector results returned as JSON from the oo CLI.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
