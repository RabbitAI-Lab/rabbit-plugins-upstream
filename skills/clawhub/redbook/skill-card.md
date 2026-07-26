## Description: <br>
Search, read, analyze, and automate Xiaohongshu content via CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lucasygu](https://clawhub.ai/user/lucasygu) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, content operators, and analysts use this skill to run the redbook CLI for Xiaohongshu research, creator analysis, engagement workflows, and content operations through an agent. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can give an agent access to a logged-in Xiaohongshu session and browser cookies. <br>
Mitigation: Use a dedicated browser profile or test account, avoid saving cookies unless necessary, and clear ~/.redbook/cookies.json after use. <br>
Risk: The CLI can perform live account actions such as posting, replying, uploading, and deleting content. <br>
Mitigation: Review every post, delete, reply, and upload command before execution, and prefer preview or dry-run flows where available. <br>
Risk: Installation behavior may modify local agent skill directories and node_modules. <br>
Mitigation: Install in a controlled environment and review the postinstall behavior before deploying to shared or sensitive systems. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lucasygu/skills/redbook) <br>
- [Project homepage](https://github.com/lucasygu/redbook) <br>
- [README](README.md) <br>
- [Skill instructions](SKILL.md) <br>
- [Content Language Strategy](docs/content-language-strategy.md) <br>
- [Research: Automation, OpenClaw, ClawHub, and Gemini Integration](docs/research-task-1789.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with CLI commands and optional JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce files such as rendered image cards when the corresponding CLI commands are executed.] <br>

## Skill Version(s): <br>
0.8.1 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
