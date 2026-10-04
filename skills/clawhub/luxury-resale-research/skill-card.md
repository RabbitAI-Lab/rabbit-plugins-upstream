## Description:

Research luxury-fashion and watch resale listings, sold evidence, condition, and seller signals across specialist marketplaces for sourcing and evidence comparison, not buying or appraisal.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Shoppers, resale researchers, and sourcing teams compare public luxury resale listings and available sold evidence, while keeping asking prices, condition labels, and seller signals distinct from verified transactions or authentication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the optional Crawlora helper sends the API key and search parameters to Crawlora and may consume credits.

Mitigation: Run it only for intended research requests, protect the API key, and account for API usage.

Risk: Broader retail and store-location endpoints could be used for unrelated location or contact gathering.

Mitigation: Keep queries limited to public resale research and avoid unrelated location or contact collection.

Risk: Marketplace asking prices and source-stated condition or authentication labels can be mistaken for completed sales or independent verification.

Mitigation: Separate asks from confirmed sold evidence, attribute marketplace claims, and mark missing fees or transaction details as not provided.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/luxury-resale-research)
- [Publisher profile](https://clawhub.ai/user/crawlora-org)
- [Endpoint reference](artifact/reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown comparison table or JSON list]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Separates active asks from sold evidence; includes source links, timestamps, currency, condition and seller signals, and explicit gaps where data is unavailable.]

## Skill Version(s):

1.0.2 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
