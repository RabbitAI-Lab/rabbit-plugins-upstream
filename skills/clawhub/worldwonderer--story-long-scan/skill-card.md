## Description:

Analyzes ranking data from Chinese long-form web-novel platforms such as Qidian, Fanqie, and Jinjiang to surface market trends, popular genres, and topic candidates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

External writers, editors, and market analysts use this skill to collect or review web-novel ranking samples, compare platform-specific signals, and turn those signals into genre trends and topic recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can fetch ranking pages from listed novel platforms and save local report files.

Mitigation: Install it only for that workflow and choose an intentional output directory before running scraper commands.

Risk: Browser/CDP collection can interact with logged-in site state on supported platforms.

Mitigation: Use a separate browser or CDP session when logged-in platform state should not be exposed to scraper activity.

Risk: Sparse or stale ranking samples can lead to overconfident market conclusions.

Mitigation: Use the skill's data-quality checks and require enough cross-platform or cross-list samples before treating a pattern as a trend.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/worldwonderer/skills/story-long-scan)
- [OpenClaw source metadata](https://github.com/worldwonderer/oh-story-claudecode)
- [Scan output format](references/scan-output-format.md)
- [Topic decision guide](references/topic-decision.md)
- [Genre trends reference](references/genre-trends.md)
- [Publishing guide](references/publishing-guide.md)
- [Reader profiling](references/reader-profiling.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Files, Guidance]

**Output Format:** [Markdown reports, local Markdown files, and inline shell commands for ranking scrapers]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May fetch public ranking pages and write report files to a selected output directory.]

## Skill Version(s):

1.1.12 (source: server release metadata; artifact frontmatter declares 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
