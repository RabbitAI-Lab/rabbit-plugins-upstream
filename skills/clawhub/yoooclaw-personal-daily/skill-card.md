## Description:

Generates a personalized Chinese daily news digest from configured interest topics using current-day search results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vivalavida-say-hi](https://clawhub.ai/user/vivalavida-say-hi)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to turn their configured topics of interest into a concise daily news briefing with grouped stories, source URLs, and a short trend summary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads configured interest topics and sends derived search terms to web search tools.

Mitigation: Configure only topics you are comfortable using for web search, and narrow trigger wording if the digest should run only on explicit request.

Risk: News digests can include stale, low-quality, or misleading search results if source quality or date signals are weak.

Mitigation: Review included source URLs before relying on the digest for decisions; the skill is designed to filter non-current news and skip sparse topics instead of inventing items.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vivalavida-say-hi/skills/yoooclaw-personal-daily)
- [ClawHub publisher profile](https://clawhub.ai/user/vivalavida-say-hi)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown-style conversational text in Chinese with source URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs a daily digest capped at about 1500 Chinese characters, or a short fallback message when no relevant current-day news is found.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
