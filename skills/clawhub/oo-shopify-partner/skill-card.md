## Description:

Shopify Partner connector skill for searching, reading, and executing Shopify Partner operations through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and Shopify Partner operators use this skill to inspect connector schemas, run Shopify Partner read actions, execute Partner GraphQL queries or mutations, and retrieve app, event, and earnings transaction data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill exposes a write-capable Shopify Partner GraphQL path while presenting common usage as searching and reading data.

Mitigation: Treat execute_graphql as write-capable, inspect the live schema, and require explicit user confirmation for any mutation or state-changing payload.

Risk: First-time setup includes remote installer commands that execute downloaded scripts.

Mitigation: Avoid pipe-to-shell installation unless the installer source and integrity have been independently verified; prefer reviewing the official install guide first.

Risk: Use requires Shopify Partner credentials and scopes through an OOMOL-connected account.

Mitigation: Use only credentials and scopes acceptable for exposure to OOMOL, apply least privilege, and reconnect or rotate credentials when access changes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-shopify-partner)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Shopify Partner Homepage](https://www.shopify.com/partners)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to inspect live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
