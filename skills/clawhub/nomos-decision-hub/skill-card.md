## Description:

Deterministic decision engine for causal analysis, compliance audit, scenario stress testing, and root-cause tracing; enterprise deployment requires an independent service and database.

This skill is for research and development only.

## Publisher:

[nohn3043-arch](https://clawhub.ai/user/nohn3043-arch)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and governance reviewers use this skill when a user explicitly asks for NOMOS Decision-Hub, second_perspective, sealed reports, causal counterfactual analysis, root-cause tracing, or declared scenario stress testing. It helps produce auditable decision analyses and sealed reports while keeping final approval outside the algorithm.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive business or personnel decision records may be sent to or stored by a NOMOS decision service.

Mitigation: Install only for a trusted NOMOS service and avoid sending confidential records to third-party endpoints without approval.

Risk: Misconfigured API keys, OIDC settings, database credentials, public base URLs, or exposed ports can weaken service boundaries.

Mitigation: Configure API keys, OIDC, database access, and public URLs carefully; isolate exposed service ports and restrict database access.

Risk: Approval actions can affect governance records if submitted without review.

Mitigation: Require explicit human confirmation and authorization checks before approval actions are submitted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/nohn3043-arch/skills/nomos-decision-hub)
- [Project homepage](https://github.com/nohn3043-arch/second-perspective)
- [Sealed Report Specification](references/SealedReportSpec.md)
- [Decision Scenario Library](references/DecisionScenarioLibrary.md)
- [Intelligent Decision-Hub v0.3](docs/INTELLIGENT_DECISION_HUB_V0_3.md)
- [Decision Foundation v0.2](docs/DECISION_FOUNDATION_V0_2.md)
- [OpenAPI action schema](openapi-action.yaml)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python and shell snippets; JSON reports and OpenAPI-compatible configuration where applicable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce tamper-evident sealed decision reports and decision logs from declared inputs.]

## Skill Version(s):

1.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
