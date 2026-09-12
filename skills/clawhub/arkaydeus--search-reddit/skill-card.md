## Description:

Search Reddit in real time using OpenAI web_search with enrichment (engagement + top comments). Use when you need recent Reddit threads, subreddit-filtered results, or quick link lists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arkaydeus](https://clawhub.ai/user/arkaydeus)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to find recent Reddit discussion threads, filter by time or subreddit, and collect enriched links with engagement and top comment context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reddit search terms are sent to OpenAI, and Reddit thread JSON is requested for result enrichment.

Mitigation: Avoid searching for secrets or sensitive private text, and prefer a skill-specific OpenAI API key when available.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/arkaydeus/skills/search-reddit)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown-style console text, compact text, links-only text, or JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include Reddit thread URLs, subreddit names, dates, engagement counts, relevance notes, top comment excerpts, and optional JSON fields.]

## Skill Version(s):

1.0.0 (source: server release metadata and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
