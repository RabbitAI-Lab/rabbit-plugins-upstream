## Description: <br>
Story Long Scan helps agents collect and analyze long-form Chinese web-novel rankings from platforms such as Qidian, Fanqie, JJWXC, Qimao, and Ciweimao to identify genre trends, topic candidates, and validation actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[worldwonderer](https://clawhub.ai/user/worldwonderer) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External writers, publishing analysts, and agents use this skill to gather ranking samples and turn them into market scans, reader profiles, and topic decisions for long-form Chinese web novels. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill runs local Node.js scraper scripts and may use a browser-CDP session to visit ranking pages. <br>
Mitigation: Review commands before execution and use a dedicated browser profile when existing login state should not be involved. <br>
Risk: The skill writes generated reports to a local output directory. <br>
Mitigation: Choose the output directory intentionally and review generated Markdown files before relying on them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/worldwonderer/skills/story-long-scan) <br>
- [OpenClaw source metadata](https://github.com/worldwonderer/oh-story-claudecode) <br>
- [genre-trends.md](artifact/references/genre-trends.md) <br>
- [publishing-guide.md](artifact/references/publishing-guide.md) <br>
- [reader-profiling.md](artifact/references/reader-profiling.md) <br>
- [scan-output-format.md](artifact/references/scan-output-format.md) <br>
- [topic-decision.md](artifact/references/topic-decision.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown reports, concise text guidance, and shell command suggestions for scraper execution.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write local Markdown reports and topic-decision files to a user-selected output directory.] <br>

## Skill Version(s): <br>
1.1.9 (source: server release evidence; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
