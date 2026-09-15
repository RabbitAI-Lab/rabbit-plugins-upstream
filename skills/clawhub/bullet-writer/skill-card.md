## Description:

Bullet Writer helps Amazon listing operators turn product-detail and review evidence into five bullet-point diagnosis and improvement guidance through the ARI service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketplace operators, and listing specialists use this skill to analyze Amazon product details and review evidence, then identify selling-point gaps, customer questions, and wording improvements for the five bullet points. It is not intended for title rewriting, ad keyword bidding, or automatic Amazon page publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an ARI API key and sends product identifiers and task metadata to ari.funewa.com.

Mitigation: Use it only when that data sharing is acceptable, provide the minimum ASIN and site data needed, and store the API key through the documented setup or configure flow.

Risk: Paid ARI credits can be consumed after the user confirms a quote.

Mitigation: Review the quote and requestId before confirming, and use the status command to resume interrupted runs instead of starting a duplicate paid run.

Risk: The authoritative security summary says the exposed operations CLI can be steered beyond the advertised fixed bullet-point workflow.

Mitigation: Before installation or execution, review proposed commands and restrict use to the documented listing/bullets workflow unless the publisher further tightens workflow and focus enforcement.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/bullet-writer)
- [Operation workflow reference](references/operation-workflow.md)
- [API reference](references/reference.md)
- [ARI service](https://ari.funewa.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown prose with optional inline shell commands and structured findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and explicit user confirmation before paid analysis or collection runs.]

## Skill Version(s):

1.4.11 (source: evidence.release.version, artifact/_meta.json, scripts/ari.py, CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
