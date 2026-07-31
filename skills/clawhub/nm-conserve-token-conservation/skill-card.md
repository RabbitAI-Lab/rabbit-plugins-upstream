## Description: <br>
Enforces token quota management at session start with conservation and compression checks for every session or before large context loads. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to keep long-running agent sessions within token and context budgets. It guides quota checks, read budgeting, delegation decisions, compression review, and concise logging before large analyses or context-heavy work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can influence how an agent budgets file reads, summarizes context, and delegates work, which may affect task completeness if applied too rigidly. <br>
Mitigation: Review the generated conservation plan against the active task and approve additional context reads when the task genuinely requires them. <br>
Risk: External delegation may expose private task details if used without considering data sensitivity. <br>
Mitigation: Avoid external delegation for private or sensitive work unless the operator has explicitly approved the tool and data handling path. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-conserve-token-conservation) <br>
- [Publisher profile](https://clawhub.ai/user/athola) <br>
- [Claude Night Market conserve plugin](https://github.com/athola/claude-night-market/tree/master/plugins/conserve) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with concise checklists and command suggestions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces token-saving steps, delegation notes, remaining-runway guidance, and next-action lists.] <br>

## Skill Version(s): <br>
1.9.17 (source: ClawHub release metadata; artifact frontmatter lists 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
