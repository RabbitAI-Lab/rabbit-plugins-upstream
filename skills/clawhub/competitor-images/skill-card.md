## Description:

Compares a primary Amazon ASIN with authorized competitor product pages to identify image-content gaps, visible product information differences, and review-backed shooting guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon marketplace operators and ecommerce analysts use this skill to review product-page imagery against authorized competitor listings and turn visible-page and review signals into concise image-gap findings and shoot notes. It is not intended for ad publishing, sales or profit forecasting, inventory or order analysis, or automatic product-page changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The paid operations command can spend ARI account credits after quote plus explicit confirmation.

Mitigation: Review the quote, preserve the returned requestId, and run paid operations only after the user explicitly confirms the charge.

Risk: The paid operations command can be steered beyond the advertised fixed image-gap workflow.

Mitigation: Keep the workflow and focus fixed to page_compare/images, and avoid --workflow or --focus overrides unless broader ARI product-operations behavior is intentional.

Risk: The skill uses an ARI API key, reads account and credit balance data, and contacts ari.funewa.com.

Mitigation: Review the security posture before installation, store the ARI key only in the user's environment or local ARI config, and do not share command output containing account context.

## Reference(s):

- [Operation Workflow](references/operation-workflow.md)
- [API Reference](references/reference.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown-style analysis with optional JSON command responses and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; paid operations require quote review and explicit user confirmation.]

## Skill Version(s):

1.4.11 (source: release evidence, _meta.json, CHANGELOG, scripts/ari.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
