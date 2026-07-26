## Description: <br>
Perry Coding Agents dispatches coding tasks to OpenCode or Claude Code on Perry workspaces for development work, PR reviews, and isolated coding tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gricha](https://clawhub.ai/user/gricha) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and maintainers use this skill to delegate coding tasks, PR review follow-up, and CI fixes to remote Perry workspaces running OpenCode or Claude Code. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Remote background coding agents may have broad long-running execution and callback authority. <br>
Mitigation: Require explicit approval before dispatching work and avoid sensitive repositories unless remote agents creating branches or PRs is acceptable. <br>
Risk: Remote workspace targeting can connect to the wrong host if workspace identity is not verified. <br>
Mitigation: Use trusted workspace IPs and prefer pinned SSH host keys. <br>
Risk: Callback tokens used by dispatched agents can be exposed or reused. <br>
Mitigation: Avoid long-lived callback tokens and rotate or scope tokens used in wake callbacks. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gricha/skills/perry-coding-agents) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown with bash command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes task-tracking guidance, remote dispatch commands, and callback instructions for long-running agent work.] <br>

## Skill Version(s): <br>
1.5.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
