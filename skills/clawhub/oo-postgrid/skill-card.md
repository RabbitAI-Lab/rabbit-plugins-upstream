## Description:

PostGrid helps agents read, create, update, and delete PostGrid Print & Mail contacts and templates through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate PostGrid contact and template workflows from an agent session, including read, write, update, and delete operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute downloaded scripts directly in a shell.

Mitigation: Review the CLI installation path first and prefer official, versioned, checksum-verified installation instructions.

Risk: Write and destructive PostGrid actions can change or delete contacts and templates.

Mitigation: Confirm the exact payload, expected effect, and target resource with the user before write or destructive actions.

## Reference(s):

- [ClawHub PostGrid skill page](https://clawhub.ai/oomol/skills/oo-postgrid)
- [PostGrid homepage](https://www.postgrid.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return connector JSON responses that include data and execution metadata.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
