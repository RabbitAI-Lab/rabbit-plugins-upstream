## Description: <br>
AI CGO is an AI-driven growth advisory skill that routes business growth requests into diagnosis, workflow design, or optimization modes with metric-linked recommendations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[qomob](https://clawhub.ai/user/qomob) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, operators, and growth teams use this skill to diagnose growth bottlenecks, design AI-assisted growth workflows, and prioritize funnel or campaign improvements tied to revenue, conversion, retention, or cost reduction. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may ask for and retain business metrics, customer details, strategy notes, or internal benchmarks in reusable knowledge or router-signal files. <br>
Mitigation: Review any proposed knowledge-base or router-signal update before approval, and omit sensitive or proprietary details unless retention is intentional. <br>
Risk: Growth recommendations can rely on assumed CAC, LTV, payback, or benchmark data when the user has not provided validated metrics. <br>
Mitigation: Provide current unit-economics data when available and review recommendations before using them for budget, pricing, sales, or marketing decisions. <br>


## Reference(s): <br>
- [Server-resolved source repository](https://github.com/qomob/cgo) <br>
- [ClawHub skill page](https://clawhub.ai/qomob/skills/cgo-2) <br>
- [AI CGO Capability Model](references/capability-model.md) <br>
- [Harness Engineering Framework](references/harness-engineering.md) <br>
- [AI CGO Growth Workflow Design](references/workflow-design.md) <br>
- [Router Signal Table](learnings/router-signals.md) <br>
- [AI CGO Knowledge Base](learnings/kb.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, configuration] <br>
**Output Format:** [Structured Markdown with metric tables, workflows, recommendations, and follow-up questions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include assumptions, routing confidence, referenced metrics, and session-level execution notes.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
