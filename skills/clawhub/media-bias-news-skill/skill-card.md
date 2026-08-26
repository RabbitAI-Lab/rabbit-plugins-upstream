## Description:

Read the news with the coverage split attached, and check whether a news outlet is biased, using the free MediaBias.news API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fspecii](https://clawhub.ai/user/fspecii)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and research teams use this skill to ask agents for current news summaries, story coverage splits, source bias and factuality ratings, ownership context, and attribution-ready citations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: News searches, outlet names, domains, and pasted article URLs are sent to MediaBias.news for lookup.

Mitigation: Use the skill only for lookups the user intends to send to MediaBias.news, and avoid private, unpublished, or tracking-heavy URLs.

Risk: An unavailable or rate-limited API could lead an agent to answer from memory instead of evidence.

Mitigation: If the MediaBias.news API cannot be reached or returns a rate limit, state that the check did not run and avoid guessing outlet ratings or coverage splits.

Risk: Bias and factuality ratings can be misleading if flattened into a single consensus label.

Mitigation: Report each rater's verdict separately, name the rater, and preserve disagreements among AllSides, Ad Fontes Media, and Media Bias/Fact Check.

## Reference(s):

- [Server-resolved source repository](https://github.com/fspecii/media-bias-news-skill)
- [MediaBias.news](https://mediabias.news)
- [MediaBias.news API discovery](https://mediabias.news/api/v1)
- [MediaBias.news OpenAPI specification](https://mediabias.news/api/v1/openapi.json)
- [MediaBias.news methodology](https://mediabias.news/methodology)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown, Shell commands, API Calls]

**Output Format:** [Markdown guidance with curl examples and API response interpretation rules]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires HTTP access to MediaBias.news; no API key is required; outputs should cite canonical MediaBias.news pages and named third-party raters.]

## Skill Version(s):

0.1.0 (source: server release metadata; artifact frontmatter version 1.2.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
