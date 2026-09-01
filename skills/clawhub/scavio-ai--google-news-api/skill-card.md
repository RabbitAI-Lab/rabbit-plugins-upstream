## Description:

Search Google News for headlines by keyword, topic, or publication as structured JSON, including headline, source, date, and link.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Agents, developers, analysts, journalists, and media monitoring teams use this skill to retrieve current Google News headlines for keywords, topics, entities, sections, stories, or publications. It is useful for current-events research, monitoring, and summarizing fresh reporting without relying on training data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: News queries are sent to Scavio.

Mitigation: Install only when sharing those queries with Scavio is acceptable for the intended workflow.

Risk: Each API request spends Scavio credits.

Mitigation: Ask before broad pagination or repeated searches, and monitor credit usage.

Risk: The skill requires an API key.

Mitigation: Store SCAVIO_API_KEY in an environment variable or secret store, not in source code.

Risk: Returned headlines and links may still require editorial judgment.

Mitigation: Use only API-returned source names and links, cite them when summarizing, and avoid fabricating missing details.

## Reference(s):

- [Scavio Google News API documentation](https://scavio.dev/docs/google-news)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/google-news-api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown instructions with bash, Python, and JSON examples; API responses return structured JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY and uses one Scavio credit per request.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter is 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
