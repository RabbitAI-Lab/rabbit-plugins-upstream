## Description:

长篇网文扫榜。分析起点、番茄、晋江等平台排行榜数据，提炼市场趋势与热门题材。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

External writers, market researchers, and developers use this skill to scan Chinese web-novel ranking data, identify recurring genre signals, and produce topic-selection guidance for long-form web fiction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs local Node.js scraper scripts against public ranking pages and saves local Markdown reports.

Mitigation: Review the commands before execution, choose an explicit output directory, and install only if local scraping and report writing are acceptable.

Risk: Browser-CDP scraping can view pages available in the active browser session, including logged-in content if that session is used.

Mitigation: Use a dedicated or logged-out browser profile unless authenticated access is intentional, and review platform terms before scraping.

## Reference(s):

- [网文题材趋势与流派参考](references/genre-trends.md)
- [网文平台运营与书名简介指南](references/publishing-guide.md)
- [读者画像系统](references/reader-profiling.md)
- [扫榜数据采集格式规范](references/scan-output-format.md)
- [选题决策：从扫榜数据到写什么能爆](references/topic-decision.md)
- [ClawHub skill page](https://clawhub.ai/worldwonderer/skills/story-long-scan)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports with inline shell commands and structured tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save local Markdown scan reports and topic-decision files in the selected output directory.]

## Skill Version(s):

1.1.11 (source: ClawHub release metadata; artifact frontmatter: 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
