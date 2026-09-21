## Description:

Uses Amazon product detail and review evidence to summarize user value, applicable scenarios, and verifiable product positioning directions; it does not support market sizing, sales forecasting, or advertising execution and requires an ARI API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to request evidence-driven positioning analysis for a specific Amazon ASIN and site. The skill profiles the product, quotes paid ARI operations before execution, and runs only after explicit user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI stores an ARI API key locally and sends requests to the ARI service.

Mitigation: Install only if the publisher and ARI service are trusted; configure the key intentionally and avoid shared or unmanaged environments.

Risk: Paid remote workflows can spend ARI credits after explicit confirmation.

Mitigation: Review the quote and requestId before confirming, and confirm only the intended product-positioning operation for the intended ASIN and site.

Risk: The security review notes that the CLI can run paid remote operation workflows beyond the fixed product-positioning scope it advertises.

Mitigation: Keep usage to the documented workflow and do not pass custom --workflow or --focus values to operations quote or run.

Risk: Positioning conclusions can be misleading when product or review evidence is incomplete.

Mitigation: Treat outputs as evidence-based positioning discussion, not market size, sales, inventory, advertising, or real-time store data.

## Reference(s):

- [Amazon Product Positioning Operation Workflow](artifact/references/operation-workflow.md)
- [Amazon Product Positioning API Reference](artifact/references/reference.md)
- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/product-positioning)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown responses with inline shell commands and ARI quote, status, or analysis data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Paid collection or analysis requires quote review and explicit confirmation; conclusions are limited to available product-detail and review samples.]

## Skill Version(s):

1.4.13 (source: server release evidence, artifact _meta.json, CHANGELOG, and scripts/ari.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
