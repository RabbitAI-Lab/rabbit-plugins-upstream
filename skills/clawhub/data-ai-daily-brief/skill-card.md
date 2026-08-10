## Description:

Turn any industry into a daily intelligence briefing; an AI agent searches, filters, writes, and delivers structured daily briefs to 9 channels with machine-checked formatting and a business review gate.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to configure an AI agent that researches public sources, filters industry-relevant signals, writes a structured daily brief, and delivers Markdown or HTML reports through configured channels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured webhook URLs, bot tokens, SMTP credentials, and GitHub tokens may be exposed if stored long term in daily-brief-config.json.

Mitigation: Prefer environment variables where supported, review daily-brief-config.json before use, and limit tokens to the minimum required scope.

Risk: GitHub Pages delivery can publish generated reports publicly.

Mitigation: Enable GitHub Pages only for reports intended for public access and review generated Markdown or HTML before deployment.

Risk: Automated web research can include stale or unverified items if the review gate is skipped.

Mitigation: Use the skill's recency, first-hand-source, format pre-flight, and business review checks before sending a brief.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/data-ai-daily-brief)
- [README.md](artifact/README.md)
- [README_zh.md](artifact/README_zh.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and HTML report files, plus channel-delivery commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can initialize configuration, generate report files, and send reports only through configured delivery channels.]

## Skill Version(s):

5.0.1 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
