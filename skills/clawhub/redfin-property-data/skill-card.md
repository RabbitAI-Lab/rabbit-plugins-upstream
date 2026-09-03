## Description:

Search Redfin listings for sale, sold, or rent, retrieve complete property details with the Redfin Estimate and MLS facts, and read regional housing-market stats through three 1-credit endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and real-estate analysts use this skill to search Redfin for sale, sold, and rental listings, retrieve full property facts and estimates, and gather regional housing-market statistics for lead lists, comp analyses, and market-trend datasets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent needs access to a Scavio API key.

Mitigation: Store SCAVIO_API_KEY in the environment or a secret manager and avoid placing live keys in prompts, source files, or logs.

Risk: User-directed Redfin requests spend Scavio credits.

Mitigation: Confirm query scope before high-volume searches, prefer one appropriately sized page where possible, and monitor credits_remaining in API responses.

Risk: Real-estate listing data changes quickly and estimates are not appraisals.

Mitigation: Include fetch timestamps and source listing URLs in user-facing answers, and label Redfin Estimate values as estimates rather than appraised values.

Risk: Incorrect region identifiers can return plausible data for the wrong location.

Mitigation: Use a Redfin region URL, a bare ZIP code in location, or a paired region_id and region_type, and never treat a ZIP code as region_id.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/redfin-property-data)
- [Scavio Redfin Search docs](https://scavio.dev/docs/redfin-search)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, API calls]

**Output Format:** [Markdown guidance with inline code examples and structured JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; Redfin API calls use Scavio credits and listing data should be timestamped because it changes quickly.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
