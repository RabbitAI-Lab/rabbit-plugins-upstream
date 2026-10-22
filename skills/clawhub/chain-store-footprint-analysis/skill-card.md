## Description:

Compares observed chain-store locations, geographic overlap, and amenity coverage using Crawlora business directories and live locators while preserving source limits and location uncertainty.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts, developers, and business teams compare observed branches and amenities across chains within a defined area, reconcile duplicate locations, and identify gaps in available coverage.

### Deployment Geography for Use:

Global, subject to coverage in the selected Crawlora datasets and locators

## Known Risks and Mitigations:

Risk: API requests send the Crawlora key and supplied search parameters or request bodies to Crawlora.

Mitigation: Keep the key private, restrict request scopes and page limits, and omit unrelated secrets from queries and bodies.

Risk: Partial datasets and capped locator results may undercount branches or make gaps look definitive.

Mitigation: Record source coverage and caps, verify uncertain matches, and report counts as observed coverage rather than an official census.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/chain-store-footprint-analysis)
- [Crawlora endpoint reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown with a branch evidence ledger, area-by-brand matrix, and coverage notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source and time evidence, deduplicated counts, and explicit unknown or incomplete areas.]

## Skill Version(s):

1.0.2 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
