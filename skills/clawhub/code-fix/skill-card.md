## Description: <br>
Systematic code error diagnosis and fix skill for compilation errors, runtime exceptions, type errors, logic bugs, crash analysis, dependency conflicts, and unexpected behavior. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yun520-1](https://clawhub.ai/user/yun520-1) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to diagnose reported code errors, isolate root causes, apply minimal fixes, and verify that failures are resolved. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cache cleanup, dependency reinstall, or environment comparison commands can remove local files or expose sensitive configuration. <br>
Mitigation: Confirm the project directory and expected changes before running cleanup or reinstall commands, and redact secrets such as API keys, passwords, and tokens. <br>
Risk: Debugging fixes can introduce incorrect changes when the root cause is not established. <br>
Mitigation: Require reproduction, root-cause isolation, minimal edits, and verification with the original failure case or relevant tests. <br>


## Reference(s): <br>
- [Code Fix on ClawHub](https://clawhub.ai/yun520-1/skills/code-fix) <br>


## Skill Output: <br>
**Output Type(s):** [analysis, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline code and shell command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose or apply code edits and local verification steps depending on the agent environment.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
