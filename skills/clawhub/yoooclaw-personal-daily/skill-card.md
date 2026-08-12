## Description:

Generates a source-linked Chinese personalized daily news digest from configured user interests, using available web search where possible and fixed RSS feeds as a fallback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vivalavida-say-hi](https://clawhub.ai/user/vivalavida-say-hi)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to turn configured interests or scheduled-task topics into a concise Chinese daily news briefing with source links, publication-time checks, and trend signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured interests may be sent as search queries to external search providers.

Mitigation: Review the interests file and scheduled-task topics before use, and include only topics suitable for external search.

Risk: The fallback path fetches fixed external RSS feeds over the network.

Mitigation: Deploy only in environments where outbound requests to the listed RSS sources are acceptable.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/vivalavida-say-hi/skills/yoooclaw-personal-daily)
- [Hermes Daily Generation](references/generate/hermes.md)
- [OpenClaw Daily Generation](references/generate/openclaw.md)
- [Search Acquisition](references/acquisition/search.md)
- [RSS Acquisition](references/acquisition/rss.md)
- [Daily Output Template](references/output/template.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Chinese Markdown-style daily digest with inline source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The final response is capped at 1500 Chinese characters and does not generate files.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
