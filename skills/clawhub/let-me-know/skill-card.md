## Description: <br>
Notify the user before starting any long-running task and keep them updated with a start message, a configurable heartbeat update, and an immediate completion or failure message. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fogyoy](https://clawhub.ai/user/fogyoy) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Agents use this skill during long-running installs, builds, tests, or other multi-minute tasks to notify users before work starts, send live progress heartbeats at a configurable interval, and report completion or failure immediately. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can direct an agent to restart the gateway if reminder cleanup remains stuck. <br>
Mitigation: Require explicit user or operator approval before any gateway restart, or remove that fallback and rely on retry plus one-time cleanup. <br>
Risk: Progress heartbeats may expose sensitive task details if logs are copied into user messages. <br>
Mitigation: Summarize status at a high level and avoid secrets, tokens, local paths, and sensitive log lines. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/fogyoy/skills/let-me-know) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or chat text with optional shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes start, heartbeat, completion, and failure notifications; heartbeat interval defaults to 5 minutes and can be user configured.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
