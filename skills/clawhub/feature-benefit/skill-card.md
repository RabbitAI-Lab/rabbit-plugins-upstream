## Description:

Connects Amazon product features to user benefits supported by review evidence and suggests listing copy without ad bidding, exaggerated claims, or automatic publishing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and listing operators use this skill to convert product features for a specified ASIN and marketplace into review-evidence-backed benefit statements. It checks product data and pricing before paid ARI analysis, then helps draft listing-oriented recommendations from the available review sample.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid ARI credits may be consumed if collection or analysis actions are run without reviewing the quote.

Mitigation: Review the quote and requestId first, then run paid actions only after explicit user confirmation.

Risk: The packaged CLI can perform broader paid operation modes than the published fixed listing-benefits workflow.

Mitigation: Use the documented listing/benefits workflow and avoid supplying workflow, focus, or competitor parameters unless broader product-operations behavior is intended.

Risk: The skill stores an ARI API key locally and the security summary notes a local file-safety weakness.

Mitigation: Ensure ~/.ari is a private directory controlled by the user before saving an API key.

## Reference(s):

- [Amazon Feature Benefit Operation Workflow](artifact/references/operation-workflow.md)
- [Amazon Feature Benefit API Reference](artifact/references/reference.md)
- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/feature-benefit)
- [Publisher Profile](https://clawhub.ai/user/funewa)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with ARI command examples and evidence-backed listing recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; paid collection or analysis actions should follow a quote and explicit user confirmation.]

## Skill Version(s):

1.4.11 (source: server release evidence, CHANGELOG, _meta.json, script VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
