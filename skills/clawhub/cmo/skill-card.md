## Description: <br>
Operates as a chief marketing officer for marketing strategy, pipeline planning, budget allocation, channel selection, positioning, lifecycle, launch, measurement, communications, compliance, and team planning. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, founders, and marketing leaders use this skill to diagnose marketing performance, choose channels, size budgets, plan launches, manage positioning, and prepare CMO-level recommendations. It is intended for allocation and strategy decisions, not single-asset execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can reuse local marketing context such as funnel numbers, channel history, constraints, approval thresholds, and brand voice files from ~/Clawic/data/cmo/. <br>
Mitigation: Review or delete ~/Clawic/data/cmo/ before installation or reuse if prior business context should not carry into later sessions. <br>
Risk: Marketing recommendations can affect spend, public statements, price changes, or crisis responses. <br>
Mitigation: Keep money commitments, public statements, price changes, and crisis responses at recommendation stage until the named human approver signs off. <br>
Risk: Marketing compliance rules vary by jurisdiction and can change. <br>
Mitigation: Route regulated-category campaigns, personal-data issues, claims substantiation, and market-entry questions to counsel as described in the artifact compliance guidance. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ivangdavila/skills/cmo) <br>
- [Clawic skill page](https://clawic.com/skills/cmo) <br>
- [Artifact: SKILL.md](artifact/SKILL.md) <br>
- [Artifact: setup.md](artifact/setup.md) <br>
- [Artifact: compliance.md](artifact/compliance.md) <br>
- [Artifact: measurement.md](artifact/measurement.md) <br>
- [Artifact: memory-template.md](artifact/memory-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Configuration, Files] <br>
**Output Format:** [Markdown recommendations, plans, briefs, statements, checklists, formulas, and local configuration or memory updates when the user provides preferences or facts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read and update scoped local context under ~/Clawic/data/cmo/ only when user-provided preferences or facts support it; money commitments and public statements require human sign-off.] <br>

## Skill Version(s): <br>
1.0.5 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
