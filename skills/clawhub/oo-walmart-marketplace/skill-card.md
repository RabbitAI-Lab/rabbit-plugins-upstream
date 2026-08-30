## Description:

Walmart Marketplace (marketplace.walmart.com). Use this skill for ANY Walmart Marketplace request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and developers use this skill to read Walmart Marketplace catalog, inventory, and order data through an OOMOL-connected account. With user confirmation, it can also update inventory amounts for seller SKUs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Walmart Marketplace seller data and update inventory amounts, which may affect active marketplace listings.

Mitigation: Review action schemas and payloads before execution, and require explicit user confirmation before write or destructive actions.

## Reference(s):

- [Walmart Marketplace homepage](https://marketplace.walmart.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces oo CLI connector schema and run commands; connector responses are JSON when run with --json.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
