## Description: <br>
LOOP helps a sofagent-based agent run a self-iterating development cycle that routes a task through coding, audit, review, and human confirmation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kongfangxun](https://clawhub.ai/user/kongfangxun) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and maintainers use LOOP to coordinate automated code changes, tests, commits, audit checks, code review, and human approval for sofagent or adapted projects. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can drive a broad development loop that edits files, runs tests, creates commits, and coordinates review agents. <br>
Mitigation: Install it only in repositories where this behavior is intended, review the installer first, and run on a clean branch. <br>
Risk: Automatic activation or sub-agent coordination may start changes before the user has clearly scoped the task. <br>
Mitigation: Keep human approval gates enabled before pushes, rule changes, and release actions, and use explicit task prompts in sensitive repositories. <br>
Risk: The loop can modify agent or review rules, which may weaken future review behavior if accepted without scrutiny. <br>
Mitigation: Require human review for changes to agent definitions, review standards, and audit workflow documents. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kongfangxun/skills/sofagent-loop) <br>
- [README](README.md) <br>
- [LOOP design](LOOP.md) <br>
- [Quick start](quick-start.md) <br>
- [Agency Agents format](https://github.com/jnMetaCode/agency-agents-zh) <br>
- [DeepAgentsJS](https://github.com/langchain-ai/deepagentsjs) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown text with shell command snippets and proposed or applied code and configuration changes.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce commits, review reports, reflection records, and audit history when used with sofagent/OpenClaw; the documented loop includes human confirmation.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release, SKILL.md frontmatter, package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
