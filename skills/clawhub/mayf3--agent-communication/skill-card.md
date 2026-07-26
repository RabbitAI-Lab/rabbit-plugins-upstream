## Description: <br>
Enable cross-agent bidirectional messaging using sessions_send for coordination, result sharing, and service requests between agents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mayf3](https://clawhub.ai/user/mayf3) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to coordinate work between OpenClaw agents through direct sessions_send calls, including request-response delegation, result sharing, and protocol-based task handoff. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The optional helper script persistently sets OpenClaw session visibility to all, which can broaden which agents may see or interact with session context. <br>
Mitigation: Review the script before running it, use it only when broad cross-agent visibility is intended, keep the generated backup, and restore the prior configuration when broad visibility is no longer needed. <br>
Risk: Cross-agent messages can share task context with the target agent and may produce incorrect or malformed responses if protocols or session keys are wrong. <br>
Mitigation: Use explicit agent session keys, send only necessary context, set timeouts appropriate to the task, and validate responses before acting on them. <br>


## Reference(s): <br>
- [Agent Communication advanced patterns](references/advanced-patterns.md) <br>
- [ClawHub skill page](https://clawhub.ai/mayf3/agent-communication) <br>
- [Publisher profile](https://clawhub.ai/user/mayf3) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, code, shell commands, configuration] <br>
**Output Format:** [Markdown with JavaScript and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes session key conventions, timeout guidance, communication patterns, and an optional helper script for OpenClaw session visibility configuration.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
