## Description: <br>
Analyzes ranking data from long-form Chinese web-novel platforms such as Qidian, Fanqie, Qimao, Ciweimao, and Jinjiang to identify market trends and topic opportunities. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[9438190](https://clawhub.ai/user/9438190) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, writers, and publishing analysts use this skill to gather or ingest web-novel ranking samples, compare platform-specific signals, and produce scan reports plus topic-decision recommendations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may make outbound requests to web-novel ranking sites during data collection. <br>
Mitigation: Run collection only in environments where those requests are expected and permitted, and review the selected platforms before starting broad scans. <br>
Risk: Browser-based collection can involve an existing Chrome profile, including site logins or cookies. <br>
Mitigation: Use a separate browser profile for CDP collection when existing browsing state should not be involved. <br>
Risk: The skill can write multiple ranking reports and topic-decision files to an output directory. <br>
Mitigation: Choose an explicit output directory and review generated files before using them in downstream writing or publishing workflows. <br>


## Reference(s): <br>
- [Scan Output Format](references/scan-output-format.md) <br>
- [Topic Decision](references/topic-decision.md) <br>
- [Genre Trends](references/genre-trends.md) <br>
- [Reader Profiling](references/reader-profiling.md) <br>
- [Publishing Guide](references/publishing-guide.md) <br>
- [OpenClaw source metadata](https://github.com/worldwonderer/oh-story-claudecode) <br>
- [ClawHub skill page](https://clawhub.ai/9438190/skills/story-long-scan) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, text, shell commands, code, guidance] <br>
**Output Format:** [Markdown reports and recommendations with inline shell commands for optional scraper execution] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write platform ranking scan files and a topic-decision Markdown file to a user-selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
