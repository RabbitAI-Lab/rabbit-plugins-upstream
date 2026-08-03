## Description: <br>
Helps account teams create staged customer strategy by organizing decision chains, active projects, key opportunities, blockers, risks, and next actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Account managers, sales teams, and customer-facing operators use this skill to turn confirmed customer facts, project context, risks, and strategy goals into a structured account plan. It is intended to separate facts from assumptions, identify missing or conflicting inputs, and produce next steps only when minimum evidence conditions are met. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Customer strategy guidance can become misleading if unverified assumptions, missing account details, or conflicting inputs are treated as facts. <br>
Mitigation: Require the parameter status table, preserve missing or conflicting information, and proceed to formal analysis only after the minimum evidence and goal conditions are met. <br>
Risk: Use may involve business-sensitive customer and contact details. <br>
Mitigation: Share only appropriate customer information with the agent and keep human confirmation rules in place for account decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zaynpeng/skills/zayn-account) <br>
- [Skill rules](artifact/SKILL.md) <br>
- [Usage template](artifact/examples.md) <br>
- [Test criteria](artifact/tests.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Structured Markdown analysis with parameter status, customer summary, staged goals, risks, next actions, and review checkpoints.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a core customer object, an analysis goal, and at least one reliable evidence item before formal analysis.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
