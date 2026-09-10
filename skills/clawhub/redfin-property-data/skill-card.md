## Description:

Search Redfin listings for sale, sold or for rent, pull one property in full with the Redfin Estimate and MLS fact sheet, and read housing-market stats for a region.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and real-estate analysts use this skill to search Redfin sale, sold, and rental listings, retrieve full property details, and gather regional housing-market statistics through Scavio's Redfin API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Scavio API key and uses paid API credits after the free balance is exhausted.

Mitigation: Use a key scoped to Scavio access, keep it out of source control, and monitor credit usage before running broad listing searches.

Risk: Real-estate listing data and estimates can change quickly and may be mistaken for authoritative appraisals.

Mitigation: Report when data was fetched, include listing URLs for verification, and avoid presenting estimates as appraisals.

Risk: Incorrect Redfin region inputs can return plausible but wrong results, especially city names passed as location or ZIP codes used as region_id values.

Mitigation: Use a Redfin region URL, a bare ZIP in location, or a verified region_id and region_type pair, and validate the returned region before relying on results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/redfin-property-data)
- [Scavio Redfin Search documentation](https://scavio.dev/docs/redfin-search?utm_source=agent-skills&utm_medium=skill&utm_campaign=redfin-property-data)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=redfin-property-data)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with JSON API responses and Python, JavaScript, TypeScript, and bash examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY. The documented API endpoints return structured JSON envelopes containing data, response_time, credits_used, and credits_remaining.]

## Skill Version(s):

1.0.3 (source: evidence release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
