## Description: <br>
Audits changes for additive bias and Iron Law compliance <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill after implementation or before commits and pull requests to audit code changes for additive bias, test mutation, unnecessary abstractions, and invariant-impact risks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may activate for generic code-review requests and spend extra effort producing justification reports before work is considered complete. <br>
Mitigation: Use it intentionally for post-change review, pre-commit review, or pull-request readiness checks where that review discipline is desired. <br>
Risk: The generated review guidance could be incorrect or misleading if accepted without review. <br>
Mitigation: Review and scan the skill before deployment, and have a human reviewer evaluate recommendations before merging changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-imbue-justify) <br>
- [Clawdis homepage](https://github.com/athola/claude-night-market/tree/master/plugins/imbue) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks and review tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces a structured justification report covering additive bias, Iron Law compliance, invariant impact, risk assessment, and recommendations.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata; artifact frontmatter says 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
