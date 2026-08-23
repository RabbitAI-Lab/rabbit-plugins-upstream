## Description:

Performs web searches through a configured 9Router API across supported providers to find articles, news, and current information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to route web, news, and article searches through a 9Router instance when current external information is needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries and optional authorization tokens are sent to the configured 9Router service and may be routed to upstream search providers.

Mitigation: Use the skill only with trusted router and provider configurations, avoid secrets or highly sensitive private data in queries, and keep credentials in environment variables.

Risk: Search results can be incomplete, stale, or provider-dependent, especially for time-sensitive claims.

Mitigation: Check result timestamps such as published_at when available and compare results across providers or fallback combo models before presenting claims as current.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pmuhammadagus-byte/skills/9router-web-search)
- [9Router setup documentation linked by the skill](https://raw.githubusercontent.com/decolua/9router/refs/heads/master/skills/9router/SKILL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with JSON examples and shell or JavaScript snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return search result JSON from the configured 9Router service, including titles, URLs, snippets, citations, usage, metrics, and provider errors.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
