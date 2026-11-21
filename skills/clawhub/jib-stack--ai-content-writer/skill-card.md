## Description:

Creates topic-based content in styles suited to platforms such as WeChat, Xiaohongshu, Zhihu, LinkedIn, and social media.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jib-stack](https://clawhub.ai/user/jib-stack)

### License/Terms of Use:

MIT-0

## Use Case:

Content writers and social media teams can draft topic-based articles and posts in platform-specific styles, with selectable tone and length and optional keywords.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: When TAVILY_API_KEY is configured, topic-derived text may be sent to Tavily as a search query.

Mitigation: Avoid using sensitive topics, or leave TAVILY_API_KEY unset when external search is not wanted.

Risk: Security scanning was incomplete: only 3 of 4 components were scanned, tool-misuse analysis was degraded, and two referenced files were missing.

Mitigation: Review the skill and any unscanned or missing components before use, especially before relying on the documented rewrite and SEO functions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jib-stack/skills/ai-content-writer)
- [Project homepage](https://github.com/openclaw/ai-writing-assistant)

## Skill Output:

**Output Type(s):** [Markdown, Files]

**Output Format:** [Markdown content, optionally saved to a file]

**Output Parameters:** [1D (topic, platform style, tone, length, and optional keywords)]

**Other Properties Related to Output:** [May include topic-related search results when TAVILY_API_KEY is configured.]

## Skill Version(s):

1.0.0 (source: server release evidence, README changelog dated 2026-03-20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
