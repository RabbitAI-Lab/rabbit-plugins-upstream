## Description:

Researches public BBC, CNN, and Guardian news through the Crawlora API - headlines, article text, live-story updates, search, and topic archives - returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and research agents use this skill to retrieve current public headlines, article text, live-story updates, search results, and topic archives from BBC, CNN, and The Guardian through Crawlora.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper sends the user's Crawlora API key and requested article URLs, sections, topics, or search queries to Crawlora.

Mitigation: Install and use the skill only when sharing those requests with Crawlora is acceptable for the user's workflow.

Risk: Calls outside the documented public-news endpoint set could broaden data exposure or behavior.

Mitigation: Use the bundled helper's documented GET-only routes for BBC, CNN, and The Guardian.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Crawlora publisher profile](https://clawhub.ai/user/crawlora-org)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/news-media-research)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples; helper calls return JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends requested news URLs, sections, topics, or search queries to the Crawlora API.]

## Skill Version(s):

1.0.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
