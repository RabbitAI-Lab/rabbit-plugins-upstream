## Description:

Researches public BBC, CNN, and Guardian news through the Crawlora API - headlines, article text, live-story updates, search, and topic archives - returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and analysts use this skill to search and retrieve public news headlines, article text, live-story updates, and topic archives from BBC, CNN, and The Guardian through Crawlora's API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: News search terms, article URLs, and request parameters are sent to Crawlora with the user's Crawlora API key.

Mitigation: Use the skill only with inputs appropriate for Crawlora to process, and avoid private, embargoed, or sensitive research inputs unless Crawlora is trusted for that data.

Risk: The skill returns current public news data from external outlets, which may be incomplete, updated, or unavailable at request time.

Mitigation: Review returned article metadata and outlet context before relying on the output for time-sensitive conclusions.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with shell commands that return JSON from Crawlora API endpoints]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and returns normalized public news data as JSON.]

## Skill Version(s):

1.0.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
