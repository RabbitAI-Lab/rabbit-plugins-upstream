## Description: <br>
Muniu Liumia guides agents through a Chinese-first spec-driven workflow that parses PRDs, designs architecture, plans tasks, generates implementation guidance, and audits delivery quality. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[timeaground](https://clawhub.ai/user/timeaground) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and product teams use this skill to turn PRDs or feature descriptions into structured specs, architecture plans, executable task lists, implementation guidance, and delivery audit reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: In existing projects, the skill may inspect repository files to understand architecture or audit implementation. <br>
Mitigation: Invoke it only in repositories you are comfortable having analyzed, and review generated guidance before applying it. <br>
Risk: Requirements parsing, implementation guidance, or audit reports may be incomplete if PRDs, project context, or code evidence are missing. <br>
Mitigation: Provide complete inputs, answer clarification questions, and verify generated specs, task plans, and audit findings before relying on them. <br>


## Reference(s): <br>
- [Phase 1 PRD Parser](references/phase-1-prd-parser.md) <br>
- [Phase 2 Architecture Designer](references/phase-2-arch-designer.md) <br>
- [Phase 3 Task Planner](references/phase-3-task-planner.md) <br>
- [Phase 4 Implementation Guidance](references/phase-4-implementation.md) <br>
- [Phase 5 Trace Audit](references/phase-5-trace.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown documents with structured tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Chinese output by default, with English available when requested; existing-project workflows may read project files for architecture context or delivery audits.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
