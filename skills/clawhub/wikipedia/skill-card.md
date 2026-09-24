## Description:

Access Wikipedia via MCP to search articles, retrieve summaries, fetch curated daily content, inspect article structure, view page metrics, and explore related Wikipedia and Wikimedia resources across 10 supported language editions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[evanfoglia](https://clawhub.ai/user/evanfoglia)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this MCP skill to add read-only Wikipedia and Wikimedia lookup tools for research, content hooks, article discovery, media discovery, and general knowledge retrieval. It is useful when an agent needs sourced article links, summaries, sections, pageviews, current events, related articles, contributors, references, or multilingual Wikipedia access without an API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lookup terms, article titles, dates, and optional coordinates are sent to Wikipedia and Wikimedia services.

Mitigation: Use the skill only where those queries are acceptable to disclose, and apply outbound allowlisting for wikipedia.org, wikimedia.org, and commons.wikimedia.org in stricter environments.

Risk: Dependency and documentation hygiene issues could affect repeatability or review clarity.

Mitigation: Pin the requests dependency for controlled deployments and confirm install instructions against the deployed MCP configuration.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/evanfoglia/skills/wikipedia)
- [Publisher profile](https://clawhub.ai/user/evanfoglia)
- [Artifact README](artifact/README.md)
- [Artifact skill definition](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, API responses]

**Output Format:** [Markdown-formatted tool responses with source links, tables, article metadata, media URLs, and plain-text extracts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses depend on live Wikipedia and Wikimedia endpoints; most tools are read-only lookups with optional language, title, date, count, limit, or location parameters.]

## Skill Version(s):

1.6.11 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
