## Description: <br>
Analyzes code change impact with risk scoring and affected-node mapping before merging so engineers can see what a change touches and where test coverage may be missing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill before merging code changes to estimate affected code paths, prioritize risky nodes, and identify untested functions that need review or tests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may inspect the current repository while estimating code-change impact. <br>
Mitigation: Use it only in repositories where code search and dependency analysis are acceptable. <br>
Risk: The skill may execute an already-installed gauntlet graph_query.py helper from the local Claude plugins directory. <br>
Mitigation: Verify the local gauntlet installation before use and rebuild graph data when the skill reports that graph.db is missing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-pensive-blast-radius) <br>
- [Project homepage](https://github.com/athola/claude-night-market/tree/master/plugins/pensive) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown table with concise findings and recommended actions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include risk scores, affected nodes, file locations, test coverage gaps, and suggested follow-up actions.] <br>

## Skill Version(s): <br>
1.9.17 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
