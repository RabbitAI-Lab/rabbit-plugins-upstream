## Description:

IT Glue (itglue.com) connector guidance for searching and reading account data through OOMOL's oo CLI instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, support staff, and MSP operators use this skill to retrieve IT Glue configurations, contacts, organizations, and users through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute scripts from OOMOL-controlled URLs.

Mitigation: Review installer source before running it, prefer verified packages or checksum/signature validation, and avoid elevated shells unless strictly necessary.

Risk: Read actions can expose IT Glue account data through the connected OOMOL account.

Mitigation: Use an authorized account, scope requests to the needed organization or record, and avoid retrieving unnecessary sensitive records.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-it-glue)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [IT Glue homepage](https://www.itglue.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo connector schemas before execution; actions described by the artifact are read-only get and list operations.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
