## Description:

Researches public BBC, CNN, and Guardian news through the Crawlora API - headlines, article text, live-story updates, search, and topic archives - returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to search, browse, and retrieve public article or live-story content from BBC, CNN, and The Guardian through a normalized Crawlora API workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Crawlora helper can use the configured API key for broader API paths than the documented BBC, CNN, and Guardian endpoints.

Mitigation: Review commands before execution and use a Crawlora API key with minimal privileges or limited value.

Risk: Changing CRAWLORA_API_BASE can redirect requests and the API key to an unintended destination.

Mitigation: Leave CRAWLORA_API_BASE unset unless the destination is explicitly trusted.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)
- [Crawlora API Base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON API output guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the CRAWLORA_API_KEY environment variable and returns normalized JSON from supported public news endpoints.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
