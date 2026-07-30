## Description: <br>
Analyzes ranking data from long-form Chinese web fiction platforms such as Qidian, Fanqie, and JJWXC to surface market trends, popular genres, and topic candidates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[worldwonderer](https://clawhub.ai/user/worldwonderer) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Writers, editors, and web fiction market analysts use this skill to gather ranking samples, compare platform signals, identify genre patterns, and turn scan results into actionable long-form story topic decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may run Node scraper scripts, open browser or CDP sessions, and visit public novel-platform pages. <br>
Mitigation: Install only when that behavior is expected, use an explicit output directory, and review target-site rules before scraping. <br>
Risk: Browser-based scraping can involve an existing logged-in session if a sensitive browser profile is used. <br>
Mitigation: Use a dedicated or non-sensitive browser profile when site sessions should not be exposed to the workflow. <br>
Risk: Ranking-derived topic recommendations can be misleading if based on sparse, stale, or malformed samples. <br>
Mitigation: Review the generated data-quality headers and treat low-sample findings as hypotheses that need further validation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/worldwonderer/skills/story-long-scan) <br>
- [OpenClaw source metadata](https://github.com/worldwonderer/oh-story-claudecode) <br>
- [Scan output format](references/scan-output-format.md) <br>
- [Topic decision guide](references/topic-decision.md) <br>
- [Reader profiling system](references/reader-profiling.md) <br>
- [Genre trends reference](references/genre-trends.md) <br>
- [Publishing guide](references/publishing-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown reports and concise guidance, with optional inline shell commands for Node scraper scripts.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write local Markdown reports and topic-decision files to an explicit output directory.] <br>

## Skill Version(s): <br>
1.1.10 (source: server release evidence; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
