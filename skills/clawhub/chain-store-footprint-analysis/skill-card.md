## Description:

Compare observed chain-store locations across defined areas using Crawlora's Starbucks, chain-locator, and Google Maps business data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts and developers compare observed branch counts, geographic overlap, amenities, and coverage gaps for specified chains and areas while tracking source limitations and uncertain matches.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the service sends the Crawlora API key and location-query details to Crawlora.

Mitigation: Use a dedicated API key and share only query details you are comfortable sending to Crawlora.

Risk: Broad searches may exceed an intended credit budget or return capped, incomplete results.

Mitigation: Set geographic scope and call/page budgets before searching; record caps and missing coverage.

Risk: Observed business records can contain uncertain chain matches and are not an official branch census.

Mitigation: Corroborate store identity and location across sources; label unverified matches and avoid interpreting gaps as confirmed absences.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [ClawHub skill listing](https://clawhub.ai/crawlora-org/skills/chain-store-footprint-analysis)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands]

**Output Format:** [Markdown narrative and tables, with optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Branch evidence ledger, deduplicated area-by-brand matrix, source coverage, and incomplete or unknown areas.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
