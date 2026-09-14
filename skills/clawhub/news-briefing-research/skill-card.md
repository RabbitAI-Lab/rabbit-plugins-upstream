## Description:

Builds source-aware news briefings from GDELT, BBC, CNN, The Guardian, and Yahoo News using the Crawlora API, with links, dates, coverage comparisons, and uncertainty preserved.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and external users use this skill to gather recent public news about a topic, compare source coverage across supported publishers, and produce dated briefings with source links and uncertainty labels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: News search terms, source filters, and article URLs are sent to Crawlora with the user's CRAWLORA_API_KEY.

Mitigation: Use only when third-party processing by Crawlora is acceptable; avoid confidential investigations or regulated private data unless that processing has been approved.

Risk: Search indexes differ by publisher, region, and freshness, so returned coverage may be incomplete or uneven.

Mitigation: State the collection window, source set, and coverage limits; avoid presenting results as exhaustive.

Risk: Sentiment, entity extraction, and coverage volume can be mistaken for verified facts or causal evidence.

Mitigation: Treat these outputs as source-derived signals and separate reported facts, allegations, corrections, and analysis.

## Reference(s):

- [Endpoint reference](artifact/reference/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/news-briefing-research)
- [Crawlora publisher profile](https://clawhub.ai/user/crawlora-org)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with shell command examples and source-linked briefing text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include article URLs, publication or update dates, coverage-window notes, source comparisons, and uncertainty labels.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
