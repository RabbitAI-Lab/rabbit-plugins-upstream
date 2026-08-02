## Description: <br>
Schedule helps agents prepare recurring or one-time task schedules from a user-provided task description and schedule type. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and automation users can use this skill to plan cron, one-time, or interval-based tasks and receive scheduling configuration, task status guidance, or execution-oriented instructions. It is best suited to clearly specified, low-risk automation tasks rather than enterprise workflow orchestration or personnel evaluation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Deferred or recurring tasks may run commands, edit files, call APIs, or repeat automatically without sufficiently strong limits. <br>
Mitigation: Use only clearly specified, low-risk tasks; require explicit confirmation before recurring execution; and restrict execution to allowlisted commands, files, and APIs. <br>
Risk: Task descriptions can be ambiguous, which may lead to unintended timing, command behavior, or file changes. <br>
Mitigation: Require a concrete task description, schedule type, execution time, and scope before creating or enabling a schedule. <br>
Risk: Scheduled API or command tasks may expose credentials or sensitive data through environment variables, command output, or logs. <br>
Mitigation: Keep credentials in environment variables or platform secret storage, avoid logging secrets, and review outputs before sharing them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/schedule) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or JSON with scheduling configuration, command guidance, and status information] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include cron, once, or interval schedule settings derived from the requested task.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter lists 1.0.3) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
