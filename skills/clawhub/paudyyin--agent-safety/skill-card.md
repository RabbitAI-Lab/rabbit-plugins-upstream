## Description: <br>
Agent Safety provides event-driven hooks, input, tool, and output guardrails, iterative execution controls, and operation tracing for agent workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to add safety checks around agent tasks, command execution, message formatting, tool permissions, prompt-injection detection, sensitive-output filtering, and local operation tracing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can automatically intercept tasks, tool calls, and messages, which may change agent behavior. <br>
Mitigation: Use it in a controlled workspace, review and narrow trigger rules, and require explicit registration or approval for new tools before relying on guard decisions. <br>
Risk: Local audit logs and traces may capture sensitive task data, commands, environment details, stdout, or message content. <br>
Mitigation: Configure retention and log clearing, avoid tracing raw environment, stdout, or message content, and use output filtering for sensitive values. <br>
Risk: Iterative execution can continue until a completion promise or maximum iteration limit is reached. <br>
Mitigation: Set conservative max-iteration limits, define a clear completion promise and escape plan, and monitor or cancel loops when behavior diverges. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/paudyyin/skills/agent-safety) <br>
- [Hook API documentation](artifact/references/hook-api.md) <br>
- [Injection patterns](artifact/references/injection_patterns.md) <br>
- [Permission levels](artifact/references/permission_levels.md) <br>
- [Trace schema](artifact/references/trace_schema.md) <br>
- [Security patterns](artifact/rules/security-patterns.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with Python APIs, shell commands, JSON hook decisions, and local audit or trace files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local audit logs, Ralph Loop state, and SQLite trace data when installed and invoked.] <br>

## Skill Version(s): <br>
1.1.0 (source: release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
