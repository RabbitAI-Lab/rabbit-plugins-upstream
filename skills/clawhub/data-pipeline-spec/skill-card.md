## Description: <br>
Design an ETL/ELT data pipeline specification. Use when asked to design a data pipeline, spec an ETL or ELT process, document a data ingestion workflow, or plan a data integration. Produces a complete pipeline spec with sources, transforms, destinations, SLAs, error handling, and data quality rules. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohitagw15856](https://clawhub.ai/user/mohitagw15856) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, data engineers, analytics engineers, and architecture reviewers use this skill to draft ETL, ELT, streaming, or batch pipeline specifications for engineering handoff or review. It helps capture sources, transformations, destinations, schedules, SLAs, data quality checks, monitoring, security, and recovery requirements. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may include real API keys, passwords, connection strings, or raw sensitive data while describing source systems and destinations. <br>
Mitigation: Use placeholders or sanitized architecture details, and keep secrets in the appropriate credential store rather than the prompt or generated spec. <br>
Risk: Generated pipeline specifications may omit organization-specific compliance, access-control, data residency, or incident-response requirements. <br>
Mitigation: Have data engineering, security, and compliance owners review the generated spec before implementation or production use. <br>
Risk: Incomplete or inaccurate user inputs can lead to misleading SLAs, data quality checks, recovery plans, or transformation logic. <br>
Mitigation: Validate the generated spec against real source behavior, consumer requirements, and operational constraints before handoff. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mohitagw15856/skills/data-pipeline-spec) <br>
- [Data Pipeline Spec homepage](https://mohitagw15856.github.io/pm-claude-skills/skill/data-pipeline-spec.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown pipeline specification with tables, checklists, and text architecture diagrams] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user-provided pipeline purpose, source systems, destination, transformation type, frequency or SLA, volume estimate, data quality requirements, and team or stack details.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
