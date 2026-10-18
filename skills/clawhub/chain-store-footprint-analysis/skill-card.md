## Description:

Compare observed chain-store coverage using Crawlora Starbucks directories, live chain locators, and Google Maps business records within a defined area.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts and developers compare observed branch counts, geographic overlap, amenities, and coverage gaps across chains in a defined area while preserving source and location uncertainty.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill sends a Crawlora API key and business-location queries to Crawlora.

Mitigation: Install only if that external service and data sharing are acceptable; protect the API key.

Risk: Unbounded searches can consume credits or return capped, incomplete location results.

Mitigation: Bound requests by geographic scope and budget; record pages, caps, and source coverage.

Risk: Partial results and ambiguous chain identities can misstate branch counts or suggest unsupported gaps.

Mitigation: Verify brand and location matches, deduplicate branches, and present counts as observed coverage rather than an official census.

## Reference(s):

- [Endpoint reference](artifact/reference/endpoints.md)
- [ClawHub skill listing](https://clawhub.ai/crawlora-org/skills/chain-store-footprint-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Branch evidence ledger, deduplicated area-by-brand matrix, source coverage, and incomplete or unknown areas.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
