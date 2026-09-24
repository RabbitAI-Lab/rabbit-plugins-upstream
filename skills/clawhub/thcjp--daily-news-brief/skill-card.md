## Description:

Daily News Brief helps users compile an 8:00 AM summary of international affairs, economic trends, and technology developments for quick daily review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users, professionals, researchers, and teams use this skill to generate concise daily news briefs covering global events, markets, and technology. It is useful when users want scheduled news collection, summarization, and delivery through channels such as Feishu or WeChat.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence flags scheduled execution while the artifact declares only read access.

Mitigation: Review the actual script source and schedule before installation, and enable the scheduled task only in an environment where recurring execution is intended.

Risk: The skill may require API keys or service credentials for news processing and distribution.

Mitigation: Use scoped credentials, keep them outside the skill artifact, and avoid granting access beyond the configured news and delivery services.

Risk: The skill may write files such as generated briefs, templates, configuration, or history archives.

Mitigation: Constrain output paths to a known workspace and inspect configured file destinations before running the workflow.

Risk: The skill may post generated briefs to third-party services and configured recipients.

Mitigation: Verify every output channel and recipient before enabling delivery, especially Feishu or WeChat identifiers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/daily-news-brief)
- [Reuters World News](https://www.reuters.com/world)
- [BBC World News](https://www.bbc.com/news/world)
- [Bloomberg Markets](https://www.bloomberg.com/markets)
- [TechCrunch](https://techcrunch.com)
- [The Verge Technology](https://www.theverge.com/tech)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown news brief with shell command and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The described workflow can run on a daily schedule, write local brief archives, and distribute generated briefs to configured third-party channels.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
