## Description:

Search Google Hotels for a destination and dates, then fetch per-property vendor pricing and full details — as structured JSON. Price, rating, class, and amenity filters. v2 engine, 1 credit per request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search lodging for destinations and dates, compare price, rating, class, and amenity filters, and retrieve per-property details and vendor pricing through Scavio's API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hotel search details are sent to Scavio as the data provider.

Mitigation: Use the skill only when the user accepts sharing destination, date, and filter details with Scavio.

Risk: Each search or detail request spends Scavio API credits.

Mitigation: Confirm the intended query scope before broad searches and monitor remaining credit balance.

Risk: SCAVIO_API_KEY could be exposed if stored in source files or logs.

Mitigation: Keep the API key in an environment variable or secret store and do not commit it to source control.

## Reference(s):

- [Scavio Google Hotels documentation](https://scavio.dev/docs/google-hotels?utm_source=agent-skills&utm_medium=skill&utm_campaign=google-hotels-api)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/google-hotels-api)
- [Scavio publisher profile](https://clawhub.ai/user/scavio-ai)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with shell commands, code snippets, and JSON API request and response examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; search and detail API calls each spend one Scavio credit.]

## Skill Version(s):

1.0.2 (source: server release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
