## Description:

Search Zillow listings for sale, for rent or sold, pull one property in full with Zestimate and tax history, and read a real-estate agent's profile and reviews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, real estate analysts, and agentic workflows use this skill to search Zillow listings, retrieve detailed property records, and fetch Zillow agent profiles and reviews through Scavio's API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search, property, and agent inputs are sent to Scavio's external API.

Mitigation: Use the skill only where sending those inputs to Scavio is acceptable for the user's data handling requirements.

Risk: Each request consumes Scavio credits, including requests that return empty results.

Mitigation: Review filters before calling the API and relax overly narrow searches instead of retrying unchanged requests.

Risk: Zestimate and similar values can be mistaken for appraisals or verified sale prices.

Mitigation: Label Zestimate values as estimates and avoid presenting them as listing prices, appraisals, or transaction facts.

Risk: The skill requires an API key for Scavio.

Mitigation: Store SCAVIO_API_KEY in environment secrets and do not include it in source code, prompts, or shared logs.

## Reference(s):

- [Scavio Zillow documentation](https://scavio.dev/docs/zillow-search)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/scavio-zillow)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API request and response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses SCAVIO_API_KEY and returns structured Zillow search, property, and agent review data from Scavio API calls.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
