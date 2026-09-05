## Description:

Search Redfin listings for sale, sold or for rent, pull one property in full with the Redfin Estimate and MLS fact sheet, and read housing-market stats for a region.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query Scavio's Redfin data API for listings, property details, comparable sales, and regional housing-market statistics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Real-estate queries and property or region identifiers are sent to Scavio's external API.

Mitigation: Tell users when external API calls are required and avoid sending sensitive or unnecessary query details.

Risk: API calls can consume paid credits after the free allowance.

Mitigation: Prefer one appropriately broad search page, explain credit use before repeated calls, and monitor remaining credits.

Risk: The Scavio API key could be exposed if copied into source code or logs.

Mitigation: Store SCAVIO_API_KEY in the environment or a secret store and avoid hard-coding it in examples or generated files.

Risk: Incorrect Redfin region parameters can return plausible data for the wrong location.

Mitigation: Use Redfin region URLs or ZIP codes for location searches, and only use region_id together with region_type when both are known.

Risk: Listing data changes quickly and Redfin Estimates are not appraisals.

Mitigation: State when data was fetched, include listing URLs for verification, and label estimates clearly.

## Reference(s):

- [Scavio Redfin documentation](https://scavio.dev/docs/redfin-search?utm_source=agent-skills&utm_medium=skill&utm_campaign=redfin-property-data)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=redfin-property-data)
- [ClawHub skill listing](https://clawhub.ai/scavio-ai/skills/redfin-property-data)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration, JSON]

**Output Format:** [Markdown guidance with API request examples and structured JSON response descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY and sends requests to Scavio's external API.]

## Skill Version(s):

1.0.2 (source: server release evidence; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
