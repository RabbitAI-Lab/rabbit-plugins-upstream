## Description:

Checks Amazon ASIN listings for page completeness, misunderstanding risk, and issues supported by review evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, operators, and listing teams use this skill to assess a single ASIN's listing health, find completeness and misunderstanding risks, and ground conclusions in product-detail and review evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary says the CLI still exposes workflow override parameters that can bypass the documented fixed listing-health scope.

Mitigation: Use the documented listing-health flow only, and avoid custom workflow or focus parameters unless broader product-operations behavior is intentional.

Risk: The security guidance says the skill stores an ARI API key locally and contacts ari.funewa.com.

Mitigation: Review before installing, configure the key only in a trusted environment, and stop if endpoint or redirect blocking errors appear.

Risk: The security guidance says the skill can spend ARI credits after confirmation.

Mitigation: Run the quote step first and proceed only after explicit user confirmation using the returned requestId.

## Reference(s):

- [Amazon Listing Health Operation Workflow](references/operation-workflow.md)
- [Amazon Listing Health API Reference](references/reference.md)
- [ClawHub listing-health page](https://clawhub.ai/funewa/skills/listing-health)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with concise findings, evidence notes, and inline shell commands when setup or status checks are needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key, contacts ari.funewa.com, quotes paid operations before confirmation, and does not promise real-time price, sales, inventory, order, profit, or advertising data.]

## Skill Version(s):

1.4.13 (source: server evidence release.version, artifact _meta.json, CHANGELOG, and scripts/ari.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
