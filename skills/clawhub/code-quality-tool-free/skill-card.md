## Description: <br>
Helps independent developers and small teams review code style, basic security risks, and accessibility checks through agent-guided Markdown instructions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and small teams use this skill to run quick local code-quality reviews before commits or during lightweight code review. It focuses on naming and formatting conventions, basic secret and unsafe-pattern checks, and accessibility checklist guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may inspect local project files and run simple shell checks. <br>
Mitigation: Limit scans to the intended project directory and review commands before execution. <br>
Risk: The skill may propose fixes, configuration files, or git hook changes. <br>
Mitigation: Review proposed writes and hook changes before allowing an agent to modify files. <br>
Risk: Basic grep-style checks and checklist guidance can miss issues or produce false positives. <br>
Mitigation: Treat findings as review aids and confirm important results with language-specific tooling or human review. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/code-quality-tool-free) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash, Python, YAML, and checklist examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose local command checks, configuration files, review checklists, and fix guidance.] <br>

## Skill Version(s): <br>
1.0.2 (source: ClawHub release evidence; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
