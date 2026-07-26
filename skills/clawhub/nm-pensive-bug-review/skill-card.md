## Description: <br>
Hunts bugs with evidence trails. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and code reviewers use this skill to investigate bugs, document evidence-backed defects, prepare minimal fixes, and plan verification before releases, audits, or production issue follow-up. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow may trigger on broad debugging or verification requests and may suggest test, lint, or static-analysis commands. <br>
Mitigation: Review the intended scope and commands before running them, especially in sensitive repositories. <br>
Risk: Bug findings and proposed fixes can be incomplete or incorrect when repository context is missing. <br>
Mitigation: Validate findings with file references, tests, and human review before applying changes. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-pensive-bug-review) <br>
- [Pensive Plugin Source](https://github.com/athola/claude-night-market/tree/master/plugins/pensive) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance] <br>
**Output Format:** [Markdown review report with file references, proposed diffs, test updates, and command evidence.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include suggested test, lint, and static-analysis commands for user review before execution.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release evidence; artifact frontmatter lists 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
