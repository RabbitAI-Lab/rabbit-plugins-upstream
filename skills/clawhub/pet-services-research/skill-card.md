## Description:

Researches public Rover sitter and trainer profiles through the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to discover public Rover sitters, dog walkers, and trainers by location, or to inspect public provider profiles as normalized JSON through Crawlora.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Rover search locations, profile slugs, and the Crawlora API key are sent to Crawlora.

Mitigation: Use only intended public search inputs, avoid private notes or unrelated personal data in requests, and install only where Crawlora API use is acceptable.

Risk: The helper executes shell commands that call an external API.

Mitigation: Review the documented route set and require CRAWLORA_API_KEY before use; the helper is scoped to the listed Rover endpoints.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)
- [Crawlora API Base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands that return JSON from the Crawlora API]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and supports the documented Rover search and profile endpoints.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
