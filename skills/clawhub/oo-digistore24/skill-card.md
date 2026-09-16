## Description:

Use Digistore24 through an OOMOL-connected account to retrieve and list buyers, products, purchases, and account user information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents assisting external Digistore24 users can inspect live connector schemas and run read-only account queries for buyers, products, purchases, and user information through the OOMOL oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes remote installer commands that could run unverified code if executed blindly.

Mitigation: Install the oo CLI only after downloading from the official source, reviewing what will run, and approving installation deliberately.

Risk: The connector reads Digistore24 account data through an OOMOL-managed connection.

Mitigation: Use it only when the user accepts OOMOL handling the Digistore24 connection and reading connected account data.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-digistore24)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Digistore24](https://www.digistore24.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use live connector schemas and return JSON responses from the OOMOL Digistore24 connector.]

## Skill Version(s):

1.0.2 (source: evidence release and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
