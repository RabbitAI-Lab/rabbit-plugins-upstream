## Description:

长篇网文扫榜。分析起点、番茄、晋江等平台排行榜数据，提炼市场趋势与热门题材。触发方式：/story-long-scan、/长篇扫榜、「长篇什么火」「起点排行」。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

Writers, editors, and fiction-market analysts use this skill to collect or ingest Chinese web-novel ranking data and turn repeated ranking patterns into market reports, topic candidates, risk thresholds, and validation actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill makes outbound requests to Chinese web-novel platforms and may use a Chrome/CDP browser session for collection.

Mitigation: Install only if that collection behavior is acceptable, and avoid using a sensitive logged-in browser profile when scraping is not intended for that session.

Risk: Broad trigger phrases can route ordinary ranking questions into this market-scanning workflow.

Mitigation: Prefer explicit slash commands and confirm the target platform and topic direction before running collection.

Risk: The scraper scripts can write generated Markdown outputs to a chosen directory.

Mitigation: Choose the output directory deliberately and review generated reports before using them for publishing or project decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/worldwonderer/skills/story-long-scan)
- [OpenClaw source metadata](https://github.com/zenstory-ai/oh-story-claudecode)
- [Scan output format](references/scan-output-format.md)
- [Topic decision guide](references/topic-decision.md)
- [Genre trends reference](references/genre-trends.md)
- [Publishing guide](references/publishing-guide.md)
- [Reader profiling reference](references/reader-profiling.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance, files]

**Output Format:** [Markdown reports, Markdown decision files, and inline shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write ranking reports and topic-decision files to a user-selected output directory.]

## Skill Version(s):

1.1.13 (source: server release metadata; artifact frontmatter is 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
