## Description:

Search koopje.ai for Belgian second-hand deals and auctions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[antarcticaice](https://clawhub.ai/user/antarcticaice)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to search, compare, price, and retrieve Belgian second-hand marketplace listings and live auction lots through the koopje.ai API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an API key for koopje.ai and the key may authorize more than read-only search actions.

Mitigation: Store KOOPJE_API_KEY securely, scope usage to search and read operations when possible, and do not expose the key in prompts, logs, or shared outputs.

Risk: The API includes saved-listing and own-listing endpoints that can change account state or publish public listings.

Mitigation: Require an explicit user preview and confirmation before saving, removing, renewing, drafting, publishing, or sending prior conversation context to koopje.ai.

Risk: Location filters can use exact latitude and longitude.

Mitigation: Prefer Belgian postcode searches when sufficient and ask before sending exact coordinates.

## Reference(s):

- [koopje.ai /v1 API reference](references/api.md)
- [koopje.ai API](https://koopje.ai)
- [koopje.ai agent-readable docs index](https://koopje.ai/llms.txt)
- [koopje.ai n8n integration template](https://koopje.ai/koppelen)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with JSON examples and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires KOOPJE_API_KEY for authenticated koopje.ai API calls; search results should include price, location, source, and listing URL.]

## Skill Version(s):

1.0.8 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
