## Description: <br>
Fetches and parses CCTV News Broadcast (Xinwen Lianbo) highlights for a given date. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to retrieve date-based CCTV Xinwen Lianbo news highlights and turn them into structured news lists and summaries for research, information collection, and workflow automation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks for broad command execution. <br>
Mitigation: Use it only in an environment where shell access is acceptable, review proposed commands before execution, and prefer a version that documents exact commands. <br>
Risk: The artifact describes scraping and scheduled monitoring without clear source restrictions or safeguards. <br>
Mitigation: Restrict use to approved news sources, avoid unattended scheduled execution, and confirm scraping limits before deployment. <br>


## Reference(s): <br>
- [Cctv News Fetcher on ClawHub](https://clawhub.ai/thcjp/skills/cctv-news-fetcher) <br>
- [SkillHub homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with structured JSON-style results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May require network access and shell execution depending on the agent environment.] <br>

## Skill Version(s): <br>
1.0.1 (source: artifact frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
