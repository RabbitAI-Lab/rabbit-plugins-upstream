## Description:

Helps agents identify information gaps in Amazon product descriptions using product fields and review feedback, then suggest description-focused improvements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and ecommerce operators use this skill through an agent to review product details and customer-review feedback before improving an Amazon product description. It is scoped to the listing/description workflow and does not write bullet points, manage ads, or publish changes to Amazon pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags that paid operations may accept workflow overrides beyond the Amazon-description-only scope promised by the release.

Mitigation: Before confirming paid commands, verify that the request uses the listing/description workflow and the quoted requestId.

Risk: The skill uses ARI/Funewa API access and may process product, review, account, and billing data.

Mitigation: Install only if the user trusts ARI/Funewa with that data, protect ARI API keys, and avoid sharing setup logs.

Risk: Paid collection or analysis can consume account credits.

Mitigation: Review the quote and require explicit user confirmation before running paid actions.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/funewa/skills/description-writer)
- [README](README.md)
- [Operation workflow](references/operation-workflow.md)
- [API reference](references/reference.md)
- [Changelog](CHANGELOG.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown-style agent response with concise findings and optional bash command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a fixed listing/description workflow with ops_listing output; paid actions require a quote and explicit user confirmation.]

## Skill Version(s):

1.4.11 (source: evidence release, _meta.json, CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
