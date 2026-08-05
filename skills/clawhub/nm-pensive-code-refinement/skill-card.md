## Description: <br>
Improves code quality across duplication, efficiency, and architectural fit. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use Code Refinement to analyze living code for duplication, algorithmic inefficiency, clean-code issues, architectural fit, anti-slop patterns, and error handling gaps. The skill helps produce prioritized refactoring plans and can apply changes when execution is explicitly requested. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can move from analysis into repository-wide refactoring. <br>
Mitigation: Use plan-only mode by default and require explicit approval before edits, commits, or execution waves. <br>
Risk: The skill includes an external insight-generation workflow for posting selected findings. <br>
Mitigation: Disable or review the insight-generation module before allowing findings to be posted externally, and require review of each finding for specificity and sensitivity. <br>
Risk: Scope-override phrasing can bypass branch-size stopping limits. <br>
Mitigation: Do not use scope-override language unless a maintainer has approved expanded refactoring scope. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-pensive-code-refinement) <br>
- [Clawdis homepage](https://github.com/athola/claude-night-market/tree/master/plugins/pensive) <br>
- [Publisher profile](https://clawhub.ai/user/athola) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance] <br>
**Output Format:** [Markdown reports with findings, YAML-style finding blocks, inline shell commands, and optional code changes.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Plan-only by default unless execution is explicitly requested; external insight posting should be reviewed before use.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
