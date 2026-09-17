## Description:

IT Glue (itglue.com). Use this skill for ANY IT Glue request - searching and reading data. Whenever a task involves IT Glue, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external operators, and developers use this skill to search and read IT Glue configurations, contacts, organizations, and users through an OOMOL-connected IT Glue account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup instructions include remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Install the oo CLI only through a verified method the user trusts, with inspection or signature/checksum verification where possible.

Risk: IT Glue data requests are routed through OOMOL-connected infrastructure.

Mitigation: Confirm the user accepts the OOMOL connection path and account permissions before using the skill with sensitive IT Glue data.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-it-glue)
- [IT Glue Homepage](https://www.itglue.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs read-oriented IT Glue connector actions and returns JSON responses from the oo CLI.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
