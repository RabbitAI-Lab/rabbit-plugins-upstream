## Description:

Shopify REST Admin (Legacy) helps agents inspect and read Shopify shop, blog, article, page, author, and tag data through the OOMOL Shopify connector and oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and store operations teams use this skill to safely search and read Shopify REST Admin (Legacy) content through an existing OOMOL-connected Shopify account. It is intended for read-only operational queries without calling the Shopify API directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer commands for the oo CLI.

Mitigation: Prefer an already-installed or package-manager-installed oo CLI, review or verify any installer before running it, and avoid administrative shells.

Risk: The connected Shopify account may expose data according to the scopes granted through OOMOL.

Mitigation: Confirm the Shopify scopes connected to OOMOL match the data intended for use before running actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-shopify)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Shopify](https://www.shopify.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before action execution; expected action results are JSON from the oo CLI.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
