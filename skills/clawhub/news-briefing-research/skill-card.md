## Description:

Builds source-aware news briefings from GDELT, BBC, CNN, The Guardian, and Yahoo News using the Crawlora API. Use for recent headlines, topic monitoring, source comparison, and coverage timelines with links, dates, and uncertainty preserved.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, researchers, and developers use this skill to gather recent public news, compare coverage across supported sources, and produce dated briefings that preserve links, timestamps, and uncertainty.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and endpoint requests are sent to Crawlora as a third-party news API.

Mitigation: Use the skill only when comfortable with that third-party API, and do not submit secrets, private URLs, confidential watchlists, or sensitive internal research terms.

Risk: Yahoo News comment endpoints return public user-generated comments, which may be noisy or sensitive.

Mitigation: Use comment endpoints only when public comments are specifically needed, and label comment-derived material separately from reported article content.

Risk: Search indexes differ by source, region, and freshness, so results may not be exhaustive.

Mitigation: State the collection window, source set, coverage limits, and uncertainty in generated briefings.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/news-briefing-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with source links, dates, caveats, and inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include raw JSON from Crawlora endpoints when commands are executed and piped through jq.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
