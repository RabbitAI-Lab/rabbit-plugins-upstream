## Description:

Ninox helps an agent read, create, update, delete, and search Ninox data through the OOMOL-connected oo CLI instead of calling the Ninox API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Ninox workspaces, databases, tables, records, and search results through an OOMOL-connected account without handling raw Ninox credentials. It supports read workflows directly and requires explicit confirmation before create, update, or delete actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup includes pipe-to-shell installer commands for the oo CLI.

Mitigation: Use a trusted, verifiable oo CLI installation method where possible, such as reviewing the install guide and installer source before execution.

Risk: The skill can create, update, or delete Ninox records.

Mitigation: Inspect the live action schema, confirm the exact payload and expected effect with the user, and require explicit approval before write or destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-ninox)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Ninox homepage](https://ninox.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions return JSON responses through the oo CLI; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
