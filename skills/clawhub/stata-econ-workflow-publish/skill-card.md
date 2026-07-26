## Description: <br>
Provides a Stata econometrics research workflow for do-file authoring, debugging, execution guidance, replication review, log verification, quality scoring, and empirical project management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xht-322](https://clawhub.ai/user/xht-322) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Researchers, students, and developers working with Stata use this skill to structure empirical economics projects, draft and run do-files, verify logs, review econometric methods, and prepare reproducible replication workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill combines command execution guidance with Stata package installation and workflow automation. <br>
Mitigation: Require explicit user approval before running local commands, installing packages, or executing do-files. <br>
Risk: The security summary flags automatic persistent project-memory changes as an area needing review. <br>
Mitigation: Review and approve any proposed writes to persistent project files such as MEMORY.md, CLAUDE.md, or TOOLS.md. <br>
Risk: The security guidance notes broad activation language and possible username logging in reproducibility logs. <br>
Mitigation: Narrow activation triggers before deployment and remove or redact usernames from logs before sharing. <br>


## Reference(s): <br>
- [Stata Econ Workflow Publish on ClawHub](https://clawhub.ai/xht-322/skills/stata-econ-workflow-publish) <br>
- [codex-stata-for-economists](https://github.com/maxwell2732/codex-stata-for-economists) <br>
- [Stata-MCP](https://github.com/sepinetam/stata-mcp) <br>
- [Stata-MCP documentation](https://docs.statamcp.com) <br>
- [Data Protection Protocol](references/data-protection.md) <br>
- [Log Verification Protocol](references/log-verification.md) <br>
- [Quality Gates](references/quality-gates.md) <br>
- [Replication-First Protocol](references/replication-first.md) <br>
- [Reproduction Protocol](references/reproduction-protocol.md) <br>
- [Stata Coding Convention](references/stata-coding-convention.md) <br>
- [Workflow Quick Reference](references/workflow-quickref.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline code blocks, command examples, review reports, templates, and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose local Stata, Python, and package-management commands that should be reviewed before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
