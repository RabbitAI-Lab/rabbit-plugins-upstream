## Description: <br>
Use when an AI coding agent needs bounded development loops, persistent project-local Docs/ state, context budgeting, environment escalation rules, safe stop gates, and evidence-based completion decisions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cuihaijun](https://clawhub.ai/user/cuihaijun) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to coordinate AI coding work through bounded implementation, verification, review, and stop decisions. It is most useful when multiple agents, long-running tasks, or persistent project-local state are needed to avoid target drift and unsupported completion claims. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The optional automation runner can repeatedly invoke agent commands, which could amplify mistakes if it is given an untrusted command or excessive loop budget. <br>
Mitigation: Use only trusted LoopCommand values, keep MaxLoops low, review runner configuration before use, and stop automation when a task requires secrets, production systems, destructive Git operations, or privileged unattended actions. <br>
Risk: Persistent Docs/ state and logs can accidentally capture sensitive project details if users record secrets, private data, full transcripts, or unsanitized command output. <br>
Mitigation: Record only concise command results and evidence paths, keep local logs out of public commits unless sanitized, and block or escalate work that requires credentials, production data, or external account access. <br>


## Reference(s): <br>
- [Agent Loop Engineering on ClawHub](https://clawhub.ai/cuihaijun/skills/agent-loop-engineering) <br>
- [Completion Gate](references/completion-gate.md) <br>
- [Checker And Evidence Gate](references/checker-and-evidence.md) <br>
- [Environment Escalation](references/environment-escalation.md) <br>
- [Automation Runner](references/automation-runner.md) <br>
- [Runner Adapters](references/runner-adapters.md) <br>
- [Security Policy](SECURITY.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, configuration, shell commands] <br>
**Output Format:** [Markdown guidance with templates, reference procedures, PowerShell and Node.js helper commands, and project-local Docs/ state conventions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces bounded loop decisions such as Continue, Done, Done with Risk, Blocked, and Invalid State; helper scripts may emit textual or JSON validation summaries.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
