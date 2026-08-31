## Description:

Deterministic decision engine for causal analysis, compliance audit, scenario stress testing, and root-cause tracing, with deployment support for an independent service and database.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nohn3043-arch](https://clawhub.ai/user/nohn3043-arch)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, governance teams, and auditors use this skill to run structured decision analyses that produce auditable reports, scenario stress tests, causal counterfactuals, and review queues. The output is an audit aid and does not replace final legal, medical, financial, safety, or business approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A live deployment can expose sensitive service configuration such as API keys and database connection strings.

Mitigation: Store SP_API_KEY and SP_DATABASE_DSN in a managed secret store, limit environment access, and rotate credentials after testing or incident response.

Risk: Binding the service publicly without isolation can expose decision APIs and reports to unauthorized users.

Mitigation: Place the service behind network isolation, enforce identity and authorization, review the OpenAPI contract, and avoid public exposure until tenant controls are in place.

Risk: Decision reports may be mistaken for final approval in high-impact legal, medical, financial, safety, or business contexts.

Mitigation: Use reports as auditable decision support only, require named human approval, and route high-impact decisions to qualified domain reviewers.

Risk: The current artifact describes a functioning application core, not a complete enterprise multi-tenant control plane.

Mitigation: Add durable event storage, tenant isolation, OIDC or equivalent identity, authorization policy, rate limiting, observability, backups, and key-managed signatures before production-scale deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/nohn3043-arch/skills/nomos-decision-hub)
- [Project homepage](https://github.com/nohn3043-arch/second-perspective)
- [Sealed Report Specification](references/SealedReportSpec.md)
- [Decision Scenario Library](references/DecisionScenarioLibrary.md)
- [Intelligent Decision-Hub v0.3](docs/INTELLIGENT_DECISION_HUB_V0_3.md)
- [Decision Foundation v0.2](docs/DECISION_FOUNDATION_V0_2.md)
- [OpenAPI action contract](openapi-action.yaml)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with Python, shell, OpenAPI, and JSON artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces deterministic decision reports, sealed-report guidance, scenario templates, API usage guidance, and deployment configuration.]

## Skill Version(s):

2.0.1 (source: server release metadata; artifact frontmatter reports 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
