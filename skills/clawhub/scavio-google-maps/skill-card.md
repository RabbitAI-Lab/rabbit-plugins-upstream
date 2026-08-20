## Description:

Search Google Maps for local businesses and places, fetch full place details, and read place reviews as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to find places, enrich local business records with addresses, ratings, coordinates, hours, and phone data, and retrieve reviews from Google Maps through Scavio's API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Map searches and place or review lookups are sent to Scavio's API.

Mitigation: Use the skill only for data the user is comfortable sending to Scavio and avoid including unrelated sensitive information in queries.

Risk: Each request consumes Scavio credits, and pagination can multiply cost.

Mitigation: Confirm with the user before retrieving many result or review pages.

Risk: The skill requires a Scavio API key.

Mitigation: Keep SCAVIO_API_KEY out of source control and use an environment variable or secret store.

Risk: Incorrect or fabricated local business data could mislead downstream work.

Mitigation: Return only data present in Scavio API responses and clearly handle empty or incomplete results.

## Reference(s):

- [Scavio Google Maps documentation](https://scavio.dev/docs/google-maps)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/scavio-google-maps)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON-oriented API response handling and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should be grounded in Scavio API responses and should not fabricate place names, ratings, addresses, or review text.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
