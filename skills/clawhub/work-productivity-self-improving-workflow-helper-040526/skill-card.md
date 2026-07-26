## Description: <br>
Create self-improving agent or team workflows that capture failures, extract lessons, update instructions, and verify improvements without uncontrolled drift. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agent maintainers, prompt engineers, support operations teams, and skill authors use this skill to turn failed runs, review comments, corrections, and audits into bounded updates to prompts, skills, tests, or runbooks. It supports repeatable improvement loops with validation and changelog evidence so changes remain narrow and auditable. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated prompt, skill, memory, or runbook changes could make incorrect guidance durable. <br>
Mitigation: Review proposed changes before applying them and require each update to cite the observed failure and the behavior it should change. <br>
Risk: Accidental invocation could be disruptive in workflows where improvement rules should change only after explicit review. <br>
Mitigation: Tighten activation wording or require explicit user confirmation before using the workflow in those environments. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/work-productivity-self-improving-workflow-helper-040526) <br>
- [Requirement Plan](references/requirement-plan.md) <br>


## Skill Output: <br>
**Output Type(s):** [analysis, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown with structured recommendations, checklist items, validation plans, changelog notes, and optional code or configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are proposals for human review before making prompt, skill, memory, or runbook changes durable.] <br>

## Skill Version(s): <br>
0.1.0 (source: server-resolved release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
