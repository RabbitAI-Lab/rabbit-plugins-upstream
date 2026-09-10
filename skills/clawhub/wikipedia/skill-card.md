## Description:

Access Wikipedia via MCP to search articles, retrieve summaries and extracts, inspect article metadata, get current and historical Wikipedia feeds, and work across 10 language editions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[evanfoglia](https://clawhub.ai/user/evanfoglia)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this MCP skill to give an assistant Wikipedia lookup tools for research, content hooks, article discovery, daily feeds, media lookup, and basic popularity analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and article titles are sent to Wikipedia or Wikimedia services over the network.

Mitigation: Avoid sending secrets, confidential project names, or sensitive internal topics as queries.

Risk: The dependency declaration allows a range of requests versions, which may reduce install reproducibility.

Mitigation: Pin and review dependencies in controlled environments when reproducible installs matter.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/evanfoglia/skills/wikipedia)
- [Wikipedia REST API v1](https://en.wikipedia.org/api/rest_v1)
- [Wikimedia Pageviews API](https://wikimedia.org/api/rest_v1/metrics/pageviews/)
- [Artifact README](artifact/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, API Calls, guidance]

**Output Format:** [Markdown text returned by MCP tool calls, often with article links and structured lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tool outputs may include Wikipedia or Wikimedia URLs, summaries, extracts, image URLs, article metadata, pageview counts, or current and historical feed entries.]

## Skill Version(s):

1.3.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
