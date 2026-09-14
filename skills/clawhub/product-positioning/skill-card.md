## Description:

This skill helps agents use Amazon product-detail and review evidence to summarize user value, fit scenarios, and product positioning directions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to request evidence-based Amazon product positioning guidance for a specified ASIN and marketplace. It checks product and review availability, quotes any billable ARI action, and runs analysis only after explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Billable collect and operations run actions can spend ARI credits and send Amazon product or review inputs to ari.funewa.com.

Mitigation: Require a quote and explicit user confirmation before running paid commands; install only when the user trusts ARI/Funewa and accepts local ARI API key storage.

Risk: Server security evidence reports that the CLI can override the advertised fixed positioning workflow and run paid remote product-operation workflows.

Mitigation: Keep use scoped to product/positioning and avoid workflow or focus overrides unless the package is updated to enforce the advertised workflow.

## Reference(s):

- [Amazon Product Positioning Operation Workflow](references/operation-workflow.md)
- [Amazon Product Positioning API Reference](references/reference.md)
- [ARI Service](https://ari.funewa.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and ARI CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and explicit user confirmation before billable collect or operations run actions.]

## Skill Version(s):

1.4.11 (source: server release metadata, artifact _meta.json, CHANGELOG, scripts/ari.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
