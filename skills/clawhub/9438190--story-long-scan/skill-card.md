## Description:

Story Long Scan helps agents collect and analyze long-form web-novel ranking data from platforms such as Qidian, Fanqie, Jinjiang, Qimao, and Ciweimao to identify market trends, popular genres, topic candidates, and validation actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[9438190](https://clawhub.ai/user/9438190)

### License/Terms of Use:

MIT-0

## Use Case:

Authors, editors, and agent operators use this skill to scan web-novel ranking samples, compare platform-specific signals, and turn repeated market patterns into practical long-form story topic recommendations. The skill can guide live scraper use, analyze user-provided ranking data, or fall back to bundled trend references when current data is unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Server security evidence reports a suspicious verdict because the browser automation helper uses an unsafe shell command pattern that could allow hostile page content to run local commands.

Mitigation: Review before installing or running; use an isolated workspace and dedicated browser profile, avoid unrelated logged-in sessions, and replace shell command construction with execFileSync or spawnSync argument arrays plus strict HTTPS host allowlists before trusting scraped pages.

Risk: Ranking data can be incomplete, stale, blocked, or misparsed when platform pages change or anti-crawling behavior interferes with collection.

Mitigation: Use the skill's documented data-quality headers and checks, rerun or repair failed collections, and treat sparse or fallback-only analysis as a hypothesis until validated with current ranking samples.

## Reference(s):

- [Scan Output Format](references/scan-output-format.md)
- [Topic Decision](references/topic-decision.md)
- [Genre Trends](references/genre-trends.md)
- [Publishing Guide](references/publishing-guide.md)
- [Reader Profiling](references/reader-profiling.md)
- [OpenClaw Source Metadata](https://github.com/worldwonderer/oh-story-claudecode)
- [ClawHub Skill Page](https://clawhub.ai/9438190/skills/story-long-scan)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, Markdown data files, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce platform scan reports and topic decision notes; scraper-backed workflows depend on network access, current page structure, and browser/CDP availability.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
