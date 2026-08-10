## Description:

NOMOS Decision Hub helps agents structure deterministic decision analysis, compliance audit, scenario stress testing, root-cause tracing, and human-governed approval workflows.

This skill is for research and development only.

## Publisher:

[nohn3043-arch](https://clawhub.ai/user/nohn3043-arch)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, governance teams, and auditors use this skill to prepare deterministic decision reviews, compare candidates under declared constraints, run counterfactual and stress scenarios, and preserve human approval records. It is most relevant for high-risk business, compliance, incident, and resource-allocation decisions where traceable reasoning is required.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide agents to submit sensitive governance, decision, evidence, and approval data to an API.

Mitigation: Require explicit user approval before analysis submissions or approval-recording calls, and redact confidential evidence, names, and internal references unless the target service is authorized to receive them.

Risk: API keys and database credentials may be needed for connected deployments.

Mitigation: Use a real secret manager for API keys and database credentials, and avoid embedding secrets in prompts, generated files, or shared examples.

Risk: Artifact documentation states that v0.3 is not yet a complete multi-tenant enterprise control plane.

Mitigation: Before production-like use, add durable event storage, organization identity and authorization checks, tenant isolation, rate limiting, observability, backups, and stronger signing infrastructure.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/nohn3043-arch/skills/nomos-decision-hub)
- [Project Homepage](https://github.com/nohn3043-arch/second-perspective)
- [Sealed Report Specification](artifact/references/SealedReportSpec.md)
- [Decision Scenario Library](artifact/references/DecisionScenarioLibrary.md)
- [Intelligent Decision Hub Design](artifact/docs/INTELLIGENT_DECISION_HUB_V0_3.md)
- [Decision Foundation Design](artifact/docs/DECISION_FOUNDATION_V0_2.md)
- [OpenAPI Action Schema](artifact/openapi-action.yaml)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python and shell snippets, JSON report structures, and OpenAPI API call descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce sealed report structures, scenario analyses, audit-log guidance, approval-recording guidance, and deployment configuration.]

## Skill Version(s):

1.2.1 (source: ClawHub release metadata; artifact frontmatter reports 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
