## Description:

Helps agents use ARI to analyze Amazon product details and review evidence for bullet-point description gaps and suggested improvements; it does not support titles, ads, or automatic publishing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and their agents use this skill to review product details and review evidence, quote and run the ARI listing/bullets operation, and produce evidence-grounded recommendations for five bullet descriptions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI can run broader paid product-operations workflows than the fixed bullet-only description promises.

Mitigation: Install only if the ARI service is trusted, review quoted costs before confirmation, and keep the agent within the documented listing/bullets workflow and focus values.

Risk: The skill stores an ARI API key locally, contacts ari.funewa.com, reads account and credit information, and can spend credits after confirmation.

Mitigation: Use it only in environments where ARI account access is acceptable, protect the local key, and require explicit user confirmation before paid collection or analysis commands.

## Reference(s):

- [Amazon five-bullet operation workflow](references/operation-workflow.md)
- [Amazon five-bullet API reference](references/reference.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown text with optional inline shell commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an Amazon ASIN, site selection, and ARI API key; paid collection or analysis actions require a quote and explicit confirmation.]

## Skill Version(s):

1.4.13 (source: server release metadata, artifact _meta.json, CHANGELOG.md, and scripts/ari.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
