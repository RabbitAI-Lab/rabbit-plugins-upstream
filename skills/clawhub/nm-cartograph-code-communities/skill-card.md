## Description: <br>
Detects architectural clusters and coupling boundaries via community detection on the code graph. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to identify module clusters, coupling boundaries, and refactoring targets in a codebase. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may read local project Python files while analyzing code structure. <br>
Mitigation: Run it only in repositories intended for local architecture analysis, and review prompts before using it on private repositories. <br>
Risk: When the separate gauntlet plugin is installed, the skill may run a local graph-query helper. <br>
Mitigation: Confirm the discovered helper path and command before execution. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-cartograph-code-communities) <br>
- [Cartograph Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/cartograph) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with shell command snippets, tables, warnings, and Mermaid diagrams] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include coupling warnings, cohesion notes, and improvement suggestions.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
