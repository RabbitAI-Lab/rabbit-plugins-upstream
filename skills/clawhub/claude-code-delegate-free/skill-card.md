## Description: <br>
Claude Code Delegate Free helps developers delegate bounded programming tasks such as code generation, completion, simple refactoring, documentation, syntax checking, and execution logging to an AI agent. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to turn natural-language programming requests into simple code generation, code completion, refactoring, documentation, and execution-log outputs. It is intended for bounded coding tasks rather than deep multi-repository analysis, large batch rewrites, or complex architecture decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad coding-delegate authority can read files, write changes, execute commands, or interact with repositories in ways that may alter code or expose sensitive context. <br>
Mitigation: Install only in a sandboxed or non-production workspace unless each planned file change, shell command, and external interaction can be reviewed and approved. <br>
Risk: Generated code, refactoring output, or debugging guidance may be incorrect, insecure, or unsuitable for complex architecture work. <br>
Mitigation: Keep tasks bounded, avoid repositories containing secrets or live deployment credentials, review generated code and logs, and run project tests and security scans before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/claude-code-delegate-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown or JSON containing generated code, task steps, execution logs, and error details.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include generated code, language labels, line counts, execution logs, retry status, and error messages.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
