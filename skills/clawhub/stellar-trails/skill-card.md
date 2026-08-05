## Description: <br>
Stellar Trails gives agents a structured six-phase workflow with traceability, activation gates, scope controls, and verification reporting across coding, document, analysis, planning, and data tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hoshiyomix](https://clawhub.ai/user/hoshiyomix) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and agent users use this skill to impose a repeatable task workflow for planning, implementation, verification, recovery, and delivery. It is intended to guide an agent's process across broad task types rather than perform one narrow domain operation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may automatically use credentials and alter global git credential or identity settings. <br>
Mitigation: Install only in environments where PAT use and git identity changes are acceptable; gate credential access and write operations behind explicit task relevance and user approval. <br>
Risk: The skill may self-update and start a persistent local web server during broadly triggered tasks. <br>
Mitigation: Review update and server-start behavior before deployment; disable or require approval for automatic updates and background services in restricted environments. <br>
Risk: The skill may write cross-session logs that retain task context. <br>
Mitigation: Confirm that persistent worklog storage is acceptable for the workspace; avoid use with sensitive tasks unless retention and cleanup are controlled. <br>
Risk: Because the skill activates on broad task classes, workflow actions can run even for simple or unrelated requests. <br>
Mitigation: Use in workspaces where always-on process enforcement is desired, or narrow activation and approval gates before installation. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/hoshiyomix/skills/stellar-trails) <br>
- [AskUserQuestion Gate Template](references/askuserquestion-gate.md) <br>
- [SADC Subagent Delegation Template](references/sadc-subagent-delegation.md) <br>
- [Workflow Phases](procedure/phases.md) <br>
- [Error Resolution Procedure](procedure/error-resolution.md) <br>
- [z.ai Sandbox Constraints](knowledge/zai-sandbox.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with inline code and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce plans, reports, task logs, verification notes, and proposed file or command changes through the hosting agent.] <br>

## Skill Version(s): <br>
9.10.4 (source: server release and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
