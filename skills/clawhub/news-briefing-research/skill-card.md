## Description:

Builds source-aware news briefings from GDELT, BBC, CNN, The Guardian, and Yahoo News using the Crawlora API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to gather recent public news, compare coverage across sources, track timelines, and produce dated briefings with source links and uncertainty preserved.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: News queries, article URLs, Yahoo identifiers, and the Crawlora API key are sent to a third-party Crawlora API.

Mitigation: Use the skill only with public news research inputs, avoid secrets or sensitive personal data, and use a scoped Crawlora API key.

Risk: Search indexes differ by source, region, and freshness, so results may be incomplete or uneven.

Mitigation: State the collection window and source set, compare multiple endpoints, and avoid describing the result set as exhaustive.

Risk: Yahoo News comment endpoints can expose public user comments that may contain sensitive or personal content.

Mitigation: Use comment analysis only when it is explicitly needed and summarize cautiously without collecting unnecessary personal data.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/news-briefing-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown briefing with source links, dates, and optional JSON returned from shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Crawlora API key; results depend on public source coverage, freshness, and endpoint limits.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
