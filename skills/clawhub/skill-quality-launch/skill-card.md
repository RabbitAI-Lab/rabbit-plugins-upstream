## Description: <br>
Quality Launch helps quality leads plan pre-production quality launch for new lines or factories, covering targets, deliverables, quality gates, ramp-up controls, and KPI monitoring. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Quality and manufacturing teams use this skill before a new production line, factory, or project ramp to collect launch details and create a structured quality launch plan. It is intended for planning quality targets, APQP-style deliverables, quality gates, ramp-up controls, and KPI review before execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may provide internal production, capacity, milestone, owner, and quality-target details while preparing a launch plan. <br>
Mitigation: Use the skill only in approved environments for that data, avoid unnecessary sensitive details, and review generated plans before sharing. <br>
Risk: Missing enterprise data can make the generated plan incomplete or leave placeholder values unresolved. <br>
Mitigation: Treat missing fields as required follow-up items and validate targets, owners, dates, and readiness status with responsible teams before execution. <br>
Risk: The artifact describes Markdown and HTML report generation, but no supporting output-generation script is included. <br>
Mitigation: Treat this as a functionality limitation and verify the final Markdown and HTML outputs manually or with approved local tooling. <br>


## Reference(s): <br>
- [Source repository](https://github.com/duding-engicool/skill-quality-launch) <br>
- [Source commit](https://github.com/duding-engicool/skill-quality-launch/commit/53b644b739a6b0cb062c670a962cf4dd74399bba) <br>
- [ClawHub skill page](https://clawhub.ai/duding-engicool/skills/skill-quality-launch) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, HTML] <br>
**Output Format:** [Structured quality launch plan in Markdown and HTML] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user-provided production, milestone, quality target, owner, and readiness details; missing values should remain marked for enterprise completion.] <br>

## Skill Version(s): <br>
0.1.0 (source: release evidence; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
