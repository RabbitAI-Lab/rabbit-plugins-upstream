## Description: <br>
Orchestrates Claude Code (小c) for heavier coding tasks such as code review, module generation, complex debugging, and architecture design while the primary agent coordinates the workflow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[turnpound](https://clawhub.ai/user/turnpound) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and coding agents use this skill to decide when to delegate heavyweight code review, code generation, debugging, and architecture tasks to a Claude Code CLI subprocess and how to structure those prompts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Delegating work to a secondary Claude Code process with bypassed permissions can grant broad project read, write, and command execution access. <br>
Mitigation: Install only when that delegation model is intended, verify the target directory before each use, and require explicit approval before commands that use bypassed permissions or add broad project directories. <br>
Risk: The delegated agent may produce or apply incorrect code changes, especially when prompts are incomplete or context is missing. <br>
Mitigation: Prefer read-only or no-tools modes for review, keep prompts self-contained, and review generated code and file changes before relying on them. <br>


## Reference(s): <br>
- [Source repository](https://github.com/TURNPOUND/claude-code-skill) <br>
- [ClawHub skill page](https://clawhub.ai/turnpound/skills/claude-code-skill-2) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Markdown] <br>
**Output Format:** [Markdown with inline shell command templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the claude binary and is marked for win32 environments in ClawHub metadata.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
