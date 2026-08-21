## Description:

Search Google Hotels for a destination and dates, then fetch per-property vendor pricing and full details as structured JSON, with price, rating, class, and amenity filters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search lodging for a destination and travel dates, compare properties by price, rating, class, amenities, and retrieve per-property booking source prices. It is suited for agents that need structured hotel search results and property details from Scavio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hotel destinations, stay dates, filters, and selected property lookup tokens are sent to Scavio using the user's API key.

Mitigation: Avoid including unnecessary personal details in travel queries and use the skill only when sending those travel details to Scavio is acceptable.

Risk: Each documented hotel search or detail call consumes one Scavio credit.

Mitigation: Monitor API credit use, page results intentionally, and avoid repeated detail lookups unless the property data is needed.

## Reference(s):

- [Scavio Google Hotels documentation](https://scavio.dev/docs/google-hotels)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/scavio-google-hotels)

## Skill Output:

**Output Type(s):** [json, code, shell commands, guidance]

**Output Format:** [Markdown guidance with shell commands, Python examples, API request details, and structured JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; documented Scavio hotel search and detail calls each cost one credit.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
