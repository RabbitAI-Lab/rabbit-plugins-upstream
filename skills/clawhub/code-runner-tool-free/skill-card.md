## Description: <br>
Runs coding tasks in non-interactive environments through a PTY workflow with automatic prompt responses, project file synchronization, timeout controls, and captured output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to ask an agent to run code review, refactoring, feature development, and test-oriented coding tasks in Unix-like non-interactive environments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Automatic yes-to-prompts behavior may approve unsafe or unintended actions during code execution. <br>
Mitigation: Use the skill only in disposable or version-controlled workspaces and disable or tightly constrain automatic confirmations when possible. <br>
Risk: The skill can write changes back to projects and includes sudo/root-oriented setup guidance. <br>
Mitigation: Avoid sudo or root execution for normal tasks, use a dedicated low-privilege user, and review diffs before keeping generated changes. <br>
Risk: Prompts, code context, and logs may be sent to an external coding CLI or LLM provider. <br>
Mitigation: Do not use the skill with secrets or sensitive business data unless external data handling and callback behavior have been verified. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline Python and shell examples; runtime output may include text logs and JSON-like status summaries.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write changes back to the target project when used with an external coding CLI.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
