## Description: <br>
Weekly Review helps an agent turn collected AI usage, prompt review, session cleanup, and weekly retrospective data into a structured report with dashboard tables and charts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[testman2025](https://clawhub.ai/user/testman2025) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and agent users use this skill to summarize weekly AI usage, review prompt quality, identify efficient and inefficient work patterns, align open sessions, and generate a weekly report. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Weekly review inputs may contain sensitive usage, conversation, project, or session details. <br>
Mitigation: Provide or approve the review_input data explicitly and keep collection limited to the relevant project folders. <br>
Risk: The legacy analyzer can read a local SQLite session database when intentionally pointed at one. <br>
Mitigation: Use the public review-input rendering path by default; only configure a database path or related environment variables when that local analysis is intended. <br>
Risk: Attribution and cleanup recommendations can be misleading if the calling agent skips file-system verification. <br>
Mitigation: Follow the skill workflow by checking relevant paths with Glob or ls before attributing work patterns or recommending cleanup. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/testman2025/skills/weekly-review) <br>
- [Homepage](https://github.com/testman2025/weekly-review-skill) <br>
- [Review input schema](schema/README.md) <br>
- [Skill README](README.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Files, Configuration, Guidance] <br>
**Output Format:** [Markdown report with optional SVG chart files, or JSON when requested] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can be used through a CLI or lightweight MCP tool with a review_input object supplied by the calling agent.] <br>

## Skill Version(s): <br>
1.2.5 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
