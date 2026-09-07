## Description:

Search Google Hotels for hotel discovery, prices, or availability.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn Google Hotels requests into Dataify Scraper API searches and receive concise hotel availability, price, and property results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hotel search details are sent to Dataify for processing.

Mitigation: Use the skill only when third-party API processing is acceptable, and avoid highly sensitive travel plans.

Risk: The Dataify API token could be exposed through chat, command arguments, or persistent shell configuration.

Mitigation: Prefer a session-scoped DATAIFY_API_TOKEN environment variable, never print the token value, and use persistent configuration only intentionally.

## Reference(s):

- [Dataify Google Hotels API](references/google_hotels_api.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown text with optional shell commands and compact hotel-search results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return raw JSON or HTML only when explicitly requested by the user.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
