## Description:

Search Google Maps businesses and places, retrieve place details, and inspect review samples or photos through the Crawlora REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill for targeted Google Maps place research, including business comparisons, addresses, ratings, review themes, source URLs, and place details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Place queries and the Crawlora API key are sent to Crawlora.

Mitigation: Use the skill only when that sharing is acceptable, keep the key in the environment, and avoid sensitive or broad collection requests.

Risk: Search results, reviews, and photos are snapshots and may be incomplete or non-representative.

Mitigation: Include retrieval time and source URLs, preserve unknown fields, and avoid claiming a complete review survey or guaranteed current conditions.

Risk: Live Google Maps requests can be rate limited or fail due to access or transient service errors.

Mitigation: Space requests at least one second apart, back off on 429, retry a transient 5xx once, and stop on 401 or 403.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/google-maps-research)
- [Crawlora Publisher Profile](https://clawhub.ai/user/crawlora-org)
- [Crawlora API Key Setup](https://crawlora.net)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown summaries and tables, with optional shell commands and Crawlora JSON responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports should include retrieval time, source URL, rating and review count together, and unknowns for unavailable fields.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
