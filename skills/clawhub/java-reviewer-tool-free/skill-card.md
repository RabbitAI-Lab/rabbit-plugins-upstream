## Description: <br>
Java代码审查免费版 helps Java developers review code changes, classify findings across six review dimensions, and produce structured reports with fix suggestions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers use this skill to review Java git diffs or source files before submission, identify style, exception-handling, security, performance, design, and resource-management issues, and receive Markdown findings with suggested fixes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests command execution and file write access for a code review workflow. <br>
Mitigation: Use it only in repositories where command execution and file writes are acceptable, and require explicit approval before running build, git, or other shell commands or modifying files. <br>
Risk: The artifact describes broader modify, delete, deploy, and save-style behavior than a Java code review tool normally needs. <br>
Mitigation: Keep use scoped to reviewing Java diffs or source files and treat generated fixes as proposals that must be reviewed before application. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/java-reviewer-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown review report with severity-ranked findings, Java code examples, and optional shell commands for inspecting diffs.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Critical, Major, Minor, and Suggestion severity labels; generated fixes require developer review before use.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
