## Description:

Adyntel helps agents search and read Adyntel advertising intelligence data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agent operators use this skill to retrieve Adyntel ad-library and keyword intelligence for competitive advertising research across Google, LinkedIn, Meta, and TikTok.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute downloaded scripts directly.

Mitigation: Review and verify the oo CLI installer through an official, versioned OOMOL channel before running installation commands.

Risk: The connector scope may be broader than the listed read and search actions.

Mitigation: Use the skill for the listed read/search actions, inspect the live action schema before each connector run, and require explicit confirmation before any action that writes, deletes, posts, or changes account data.

## Reference(s):

- [ClawHub Adyntel Skill](https://clawhub.ai/oomol/skills/oo-adyntel)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Adyntel Homepage](https://www.adyntel.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce oo CLI schema-inspection and connector-run commands that return JSON responses from Adyntel.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
