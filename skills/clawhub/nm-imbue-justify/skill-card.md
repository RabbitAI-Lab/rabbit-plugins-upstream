## Description: <br>
Audits changes for additive bias and Iron Law compliance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and code reviewers use this skill after implementation work and before commits or pull requests to audit local changes for additive bias, test expectation drift, unnecessary abstractions, and unreviewed invariant changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may activate on general code-review language even when a full justification audit is not intended. <br>
Mitigation: Use it deliberately for post-implementation or pre-merge review, and treat incidental activations as advisory unless the local diff is being audited. <br>
Risk: Review reports can introduce incorrect or misleading guidance if the agent misreads the local diff or project requirements. <br>
Mitigation: Review the report against the actual git diff, test changes, and stated requirements before changing implementation or merge decisions. <br>
Risk: The artifact covers the skill content only; related Claude Code plugin agents, hooks, or commands are not included in this release artifact. <br>
Mitigation: Review and scan any separately installed plugin components before relying on them in the same workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-imbue-justify) <br>
- [Publisher profile](https://clawhub.ai/user/athola) <br>
- [OpenClaw homepage metadata](https://github.com/athola/claude-night-market/tree/master/plugins/imbue) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, shell commands, guidance] <br>
**Output Format:** [Markdown report with tables and inline shell command examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces an additive-bias score, Iron Law compliance check, change-by-change justification, risk assessment, and recommendations.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
