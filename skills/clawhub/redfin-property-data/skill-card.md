## Description:

Search Redfin listings for sale, sold or for rent, pull one property in full with the Redfin Estimate and MLS fact sheet, and read housing-market stats for a region.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to search Redfin property listings, retrieve detailed property records, and collect regional housing-market statistics through Scavio's Redfin API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Real-estate queries and listing identifiers are sent to Scavio and may consume API credits.

Mitigation: Use the skill only when sending those property details to Scavio is acceptable, and monitor the credits used and remaining fields returned by the API.

Risk: The skill requires SCAVIO_API_KEY for authenticated API access.

Mitigation: Store SCAVIO_API_KEY in the environment or a secret store and do not commit it to source control.

Risk: Fast-moving listings and Redfin Estimates can become stale or be mistaken for appraisals.

Mitigation: Include the fetch time when reporting listing data, provide source listing URLs for verification, and present estimates as estimates rather than appraisals.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/redfin-property-data)
- [Scavio Redfin Search Documentation](https://scavio.dev/docs/redfin-search)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Code, Shell commands, Configuration]

**Output Format:** [Markdown with JSON request examples and inline Python, JavaScript, and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides agents to call Scavio Redfin endpoints that return structured JSON envelopes containing data, response time, credits used, and credits remaining.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
