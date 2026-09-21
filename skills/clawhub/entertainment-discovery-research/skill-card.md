## Description:

Researches movies and TV titles across IMDb, TMDB, JustWatch, Rotten Tomatoes, and Metacritic using the Crawlora API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to discover, compare, and summarize movies and TV shows across entertainment metadata, ratings, reviews, credits, and streaming offer sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Entertainment searches, title IDs, URLs or paths, and locale parameters are sent to Crawlora with the user's Crawlora API key.

Mitigation: Avoid submitting private watchlists or sensitive personal viewing interests, and use a scoped API key appropriate for the task.

Risk: Streaming offers, ratings, reviews, and related metadata vary by source, country, date, plan, provider, and score definition.

Mitigation: Preserve the requested locale, retrieval time, platform title ID, and score definition, and avoid averaging scores across platforms unless denominators are explicit.

Risk: The package includes read-only Metacritic game endpoints even though the main description emphasizes movies and TV.

Mitigation: Keep generated guidance focused on the requested entertainment domain and disclose game endpoint use when a task relies on it.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown or text summaries with optional shell command examples and JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should preserve source IDs, score definitions, locale, and retrieval time where relevant.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
