## Description: <br>
Claude Code Runner helps developers run Claude Code for programming tasks through PTY-based invocation, including code generation, review, refactoring, debugging, testing, and deployment support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to delegate concrete software engineering tasks to Claude Code, such as reviewing code, refactoring, adding endpoints, and fixing bugs. It is best suited to workspaces with a clear technical stack and task scope. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can cause an agent to run shell commands and change code in a workspace. <br>
Mitigation: Use it only in trusted workspaces and review proposed commands and file changes before accepting them. <br>
Risk: The skill mentions root or sudo use for user switching, which can increase the impact of unsafe or incorrect commands. <br>
Mitigation: Avoid privileged execution unless it is required for a specific task, and require explicit review for deployment or user-switching operations. <br>
Risk: PTY-based execution may not handle every interactive prompt or long-running command reliably. <br>
Mitigation: Monitor interactive tasks and retry with narrower prompts or manual steps when behavior is unclear. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/claude-code-runner) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>
- [Homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or JSON-like status output with code and shell snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include generated code, review findings, retry/error notes, and environment configuration guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter reports 0.1.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
