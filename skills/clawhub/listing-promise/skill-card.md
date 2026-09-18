## Description:

Checks whether an Amazon listing's feature, effect, and usage promises align with customer review feedback, identifies evidence gaps, and requires an ARI API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon operators and ecommerce teams use this skill to compare listing promises with review evidence for a specified ASIN and marketplace. It helps decide whether the available review sample supports, contradicts, or leaves gaps around the listing's claims.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI can run broader product-operations workflows than the listing-promise purpose describes.

Mitigation: Keep use to the documented listing/promise workflow and avoid custom --workflow or --focus values unless intentionally requesting broader ARI product-operations analysis.

Risk: The skill requires an ARI API key and sends ASIN, site, account, and review-analysis requests to ari.funewa.com.

Mitigation: Confirm this data sharing is acceptable before installation or use, and protect the API key.

Risk: Paid collection or analysis may consume ARI credits.

Mitigation: Use profile and quote commands first, then run paid commands only after explicit user confirmation with the quoted requestId.

## Reference(s):

- [ClawHub Skill Listing](https://clawhub.ai/funewa/skills/listing-promise)
- [Amazon Listing Promise Operation Workflow](references/operation-workflow.md)
- [Amazon Listing Promise API Reference](references/reference.md)
- [README](README.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown summaries with CLI command snippets and ARI analysis results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and explicit user confirmation before paid collection or analysis runs.]

## Skill Version(s):

1.4.13 (source: evidence release, artifact _meta.json, CHANGELOG.md, scripts/ari.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
