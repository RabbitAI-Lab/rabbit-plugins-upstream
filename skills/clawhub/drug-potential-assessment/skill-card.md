## Description:

Assesses candidate drugs for druggability, differentiation, clinical feasibility, competitive intensity, and commercial potential for early pipeline screening or same-target comparisons.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Pharma R&D, business development, investment, and IP teams use this skill to collect multi-source intelligence on a disease area, target, or research field, score candidate drugs, and generate structured diligence reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can run broad pharma, patent, company, clinical, sequence, and chemistry research queries that may be slow, costly, or unavailable without the required data services.

Mitigation: Confirm access to the required data services and set query scope, budget, and timeout expectations before use.

Risk: The package metadata does not declare the specialized MCP dependencies that the workflow expects.

Mitigation: Review and tighten package metadata before deployment so required services are explicit.

Risk: Drug-development scoring and recommendations may be incomplete or misleading if data coverage is low or sources conflict.

Mitigation: Require source tracing, confidence labels, coverage annotations, and expert review before using outputs for R&D, investment, or IP decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/drug-potential-assessment)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown report with structured tables and ECharts chart configurations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include a main report, summary card, candidate score table, data coverage table, and chart configurations.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
