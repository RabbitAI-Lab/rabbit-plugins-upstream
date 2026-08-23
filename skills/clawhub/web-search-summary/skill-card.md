## Description:

Search the web for a topic and produce a structured summary with key findings, sources, and actionable takeaways.

This skill is ready for commercial/non-commercial use.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and other external users use this skill to turn a web search query into a concise research brief with key findings, notable points, and sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends the user's search query to web search and fetch tools and may retrieve external pages.

Mitigation: Avoid including secrets or sensitive private information in search queries, and review fetched sources before relying on the summary.

Risk: Search summaries can be incomplete, stale, or influenced by low-quality external pages.

Mitigation: Check the listed sources and use follow-up research for decisions that require high confidence or current facts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/terrycarter1985/skills/web-search-summary)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown research brief with summary, key findings, notable points, and sources]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a query plus optional freshness, count, and maxChars parameters to guide search and summarization.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
