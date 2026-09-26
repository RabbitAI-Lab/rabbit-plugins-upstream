## Description: <br>
Agent Group helps AI agents coordinate multi-agent conversation, LLM application, and automation workflow tasks from user instructions and optional context. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external agent users can use this skill to route AI model calls, intelligent conversation, agent orchestration, and general automation workflows. It is not intended for decisions that require 100% determinism. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests broad local file and shell execution powers. <br>
Mitigation: Use it only in workspaces where command execution and file reads or writes are acceptable, and review proposed commands before execution. <br>
Risk: The trigger wording and purpose are broad, which can make unintended invocation more likely. <br>
Mitigation: Invoke it for explicit multi-agent, LLM, or automation tasks, and require extra review for sensitive files, credentials, or irreversible actions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/agent-group) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with JSON examples and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read, write, search files, and execute shell commands when the host agent grants those tools.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
