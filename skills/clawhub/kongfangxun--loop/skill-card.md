## Description: <br>
LOOP orchestrates a self-iterative development cycle for sofagent projects, routing tasks through coding, audit, review, and human confirmation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kongfangxun](https://clawhub.ai/user/kongfangxun) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and maintainers use LOOP to coordinate agent-assisted code changes, audit checks, code review, and human approval in sofagent-style projects. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can grant broad repository-changing and self-modifying agent authority. <br>
Mitigation: Use it only in a disposable branch or controlled repository with explicit approval gates for file edits, commits, pushes, agent-definition changes, and audit-rule changes. <br>
Risk: Scheduled or outer-loop self-optimization can change agent behavior over time. <br>
Mitigation: Keep scheduled and outer-loop optimization disabled until human approval gates are in place for proposed changes. <br>
Risk: The loop relies on sofagent-audit as a guardrail. <br>
Mitigation: Confirm sofagent-audit is installed and active before relying on LOOP audit results. <br>


## Reference(s): <br>
- [ClawHub LOOP skill page](https://clawhub.ai/kongfangxun/skills/loop) <br>
- [Agency Agents format](https://github.com/jnMetaCode/agency-agents-zh) <br>
- [DeepAgentsJS](https://github.com/langchain-ai/deepagentsjs) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and generated development, audit, and review outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May coordinate repository edits, commits, audit checks, review reports, and reflection records through configured agents.] <br>

## Skill Version(s): <br>
1.0.3 (source: ClawHub release metadata; artifact frontmatter and package.json list 1.0.5) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
