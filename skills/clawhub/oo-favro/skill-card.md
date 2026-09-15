## Description:

Favro skill for reading, creating, and updating Favro data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to inspect Favro schemas and retrieve, create, or update organizations, boards, widgets, collections, and cards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructions include running remote installer scripts directly in a shell.

Mitigation: Install the oo CLI through a version-pinned, inspectable, and integrity-verified method from the vendor before using the skill.

Risk: Favro write actions can change workspace data.

Mitigation: Confirm the exact payload and expected effect with the user before running create or update actions.

## Reference(s):

- [ClawHub Favro Skill](https://clawhub.ai/oomol/skills/oo-favro)
- [Favro Homepage](https://www.favro.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Favro connector command payloads and summarize returned Favro data.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
