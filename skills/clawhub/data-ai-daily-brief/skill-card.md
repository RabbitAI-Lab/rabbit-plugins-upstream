## Description:

Turns an industry into a structured daily intelligence brief by searching, filtering, writing, validating format, and delivering reports to configured channels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and operations teams use this skill to create recurring industry intelligence briefs with sourced items, impact judgments, machine format checks, and optional delivery to workplace channels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated briefs can be sent to external chat, email, bot, or GitHub Pages destinations.

Mitigation: Review generated content before delivery and enable only destinations approved for the information being summarized.

Risk: Delivery channels require webhooks, bot tokens, SMTP credentials, or a GitHub token.

Mitigation: Use least-privilege tokens or webhooks, store secrets outside generated reports, and rotate credentials if a destination is no longer trusted.

Risk: Daily brief content may include stale, duplicated, or weakly sourced items if the workflow is skipped.

Mitigation: Keep the recency checks, first-hand source tracing, deduplication check, format pre-flight, and business review gate in place before publishing.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/haiyangchenbj/skills/data-ai-daily-brief)
- [README](artifact/README.md)
- [Chinese README](artifact/README_zh.md)
- [Changelog](artifact/CHANGELOG.md)
- [CodeBuddy](https://www.codebuddy.ai/)

## Skill Output:

**Output Type(s):** [text, markdown, HTML, shell commands, configuration, guidance]

**Output Format:** [Markdown daily brief, HTML report, JSON configuration, channel-specific messages, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated briefs include source links, sectioned summaries, impact judgments, format pre-flight checks, and optional delivery to configured channels.]

## Skill Version(s):

5.0.4 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
