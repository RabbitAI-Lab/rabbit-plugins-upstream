## Description:

Researches public BBC, CNN, and Guardian news through the Crawlora API, including headlines, article text, live-story updates, search, and topic archives, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search and read public news coverage from BBC, CNN, and The Guardian via Crawlora. It supports retrieving normalized JSON for headlines, articles, live updates, searches, and topic archives.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected news search terms, article URLs, and the Crawlora API key are sent to Crawlora.

Mitigation: Use only with public news research inputs, and do not submit secrets, confidential investigations, regulated data, or private URLs.

## Reference(s):

- [Endpoint reference](artifact/reference/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/news-media-research)
- [Crawlora](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command examples and raw JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends selected news queries or public article URLs to Crawlora.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
