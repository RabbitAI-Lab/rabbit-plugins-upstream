## Description:

Routes and orchestrates Alibaba Cloud Simple Log Service (SLS) work across specialist skills for application integration, index management, exact querying, exploratory analysis, and visualization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to route broad or multi-stage Alibaba Cloud SLS requests to the right specialist skills and coordinate application log landing, index readiness, exact queries, exploratory analysis, visualization, and installation of missing specialists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Missing specialist skills may require global installation before the workflow can continue.

Mitigation: Ask for one explicit user approval before global installation, install only the selected missing specialists, and verify each specialist is discoverable before use.

Risk: Cloud changes routed through specialist skills can affect Alibaba Cloud SLS resources.

Mitigation: Preserve each specialist's approval gates and require review of proposed index, query, integration, or analysis actions before execution.

Risk: The router could overstate unsupported stages such as managed alert resources, host-agent collection, or persistent dashboards.

Mitigation: State unsupported stages as gaps and distinguish recommendations or drafts from deployed cloud resources.

Risk: Alibaba Cloud access credentials could be exposed if requested or repeated in chat.

Mitigation: Never request, read, or expose AccessKey ID or AccessKey Secret values.

## Reference(s):

- [Install Specialist Skills](references/install-specialist-skills.md)
- [Application Log Landing](references/workflows/application-log-landing.md)
- [Index and Query Readiness](references/workflows/index-query-readiness.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with optional inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routes work to installed specialist skills, preserves specialist approval gates, and reports unsupported SLS stages as gaps rather than deployed resources.]

## Skill Version(s):

0.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
