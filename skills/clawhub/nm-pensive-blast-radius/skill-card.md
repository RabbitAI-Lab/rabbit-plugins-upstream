## Description: <br>
Analyzes code change impact with risk scoring and affected-node mapping so developers can understand what a change touches and what lacks test coverage before merging. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill before merging code changes to map affected files or functions, identify missing test coverage, and prioritize review based on risk. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may read and search local repository contents to map changed files and call sites. <br>
Mitigation: Use it only in repositories whose contents may be inspected by the agent, and review proposed commands before execution. <br>
Risk: Repository search fallbacks using rg or grep can produce false positives. <br>
Mitigation: Prefer graph or semantic analysis when available, and manually verify affected nodes and test gaps before acting on the results. <br>
Risk: Risk suggestions may be incorrect or misleading if accepted without review. <br>
Mitigation: Treat the risk table and suggested actions as review inputs, then confirm coverage, security relevance, and backward compatibility before merging. <br>


## Reference(s): <br>
- [Pensive plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/pensive) <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-pensive-blast-radius) <br>


## Skill Output: <br>
**Output Type(s):** [analysis, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with risk tables, prioritized findings, suggested actions, and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use graph-based impact results when available, or repository search fallbacks for manual analysis.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
