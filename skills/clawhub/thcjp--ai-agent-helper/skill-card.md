## Description: <br>
AI Agent Helper helps developers design and optimize AI agents across prompt engineering, task decomposition, agent-loop patterns, tool selection, structured output parsing, and token optimization. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use this skill to draft, analyze, and improve AI agent prompts, tool descriptions, loop patterns, structured outputs, and operational guardrails. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests command execution and file-writing authority without tight upfront limits. <br>
Mitigation: Use it in a least-privileged workspace, require explicit approval for command execution and file writes, and avoid admin privileges unless a trusted task requires them. <br>
Risk: The skill can guide API calls, callbacks, or credential use through agent workflows. <br>
Mitigation: Require explicit approval before API calls, callbacks, or credential use, and review proposed actions before running them. <br>
Risk: The release security verdict is suspicious even though no specific risk findings were listed. <br>
Mitigation: Review the skill before installing, especially if only prompt-design guidance was expected. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with prompt, JSON, Python, and command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose tool use, file writes, callbacks, API calls, or command execution depending on the host agent permissions.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
