## Description: <br>
Structures complex decision requests into decision items, evidence, option comparisons, recommendations, risks, and required confirmations for fast leader review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, managers, and internal collaborators use this skill to turn a complex business question into a concise decision brief with clear input status, evidence, comparable options, risks, a recommendation, and the specific approvals needed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Decision briefs may include sensitive business context, evidence, costs, or approval details. <br>
Mitigation: Provide only the business context needed for the decision and avoid unnecessary sensitive information. <br>
Risk: Incorrect, conflicting, or unverified evidence could lead to an unreliable recommendation. <br>
Mitigation: Verify sensitive evidence, conflicts, and final approvals manually before acting on the brief. <br>
Risk: The skill may organize a recommendation before the decision is actually approved. <br>
Mitigation: Keep recommendations distinct from approved decisions and require explicit leader confirmation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zaynpeng/skills/zayn-decision) <br>
- [Skill source](artifact/SKILL.md) <br>
- [README](artifact/README.md) <br>
- [Examples](artifact/examples.md) <br>
- [Tests](artifact/tests.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown decision brief with parameter status, decision item, evidence, option comparison, recommendation, risks, and required confirmations.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires enough user-provided context and at least one reliable evidence item before producing a formal analysis; otherwise it requests missing information or marks output as preliminary.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
