## Description: <br>
Run and manage long tasks exceeding HTTP timeouts by starting, updating, and completing them asynchronously with immediate responses. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[enderfga](https://clawhub.ai/user/enderfga) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to keep long-running command, analysis, file-processing, or external API tasks from failing due to HTTP timeouts while still sending task completion or failure messages back to the active user session. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Task results and session IDs can be sent to a configured push endpoint. <br>
Mitigation: Use ASYNC_TASK_PUSH_URL only with trusted HTTPS endpoints and trusted authentication tokens. <br>
Risk: Task descriptions, result messages, and failure messages may contain sensitive information. <br>
Mitigation: Avoid putting secrets or sensitive data in task descriptions, result messages, or failure messages. <br>
Risk: The skill stores local task state while coordinating asynchronous task completion. <br>
Mitigation: Install only from a trusted source and review local state handling before use in sensitive environments. <br>


## Reference(s): <br>
- [Async Task on ClawHub](https://clawhub.ai/enderfga/skills/async-task) <br>
- [OpenClaw](https://openclaw.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash code blocks and command-line status messages] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can send task results, failure messages, session identifiers, and status updates through OpenClaw, Clawdbot, or a configured HTTPS push endpoint.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
