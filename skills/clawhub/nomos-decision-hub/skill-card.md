## Description: <br>
This skill helps users build, evaluate, audit, or study deterministic decision-making workflows with causal counterfactual analysis, compliance-grade audit trails, scenario stress testing, algorithm-ledger verification, and human-in-the-loop governance. <br>

This skill is for research and development only. <br>

## Publisher: <br>
[nohn3043-arch](https://clawhub.ai/user/nohn3043-arch) <br>

### License/Terms of Use: <br>
MIT-0; artifact terms state individual non-commercial research only and paid authorization for government or enterprise use <br>


## Use Case: <br>
Developers, auditors, and governance reviewers use this skill to study and prototype deterministic decision workflows, inspect causal counterfactual behavior, review audit-ledger concepts, and prepare deployment plans for a separately installed NOMOS engine. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is an onboarding and research bundle, while the full engine and any production deployment are separate software surfaces. <br>
Mitigation: Review, pin, scan, and configure the upstream engine separately before using it with real business, legal, financial, medical, or safety decisions. <br>
Risk: Decision reports can be mistaken for final authority in high-stakes workflows. <br>
Mitigation: Keep human and domain-professional approval outside the algorithm, and use the reports as auditable inputs rather than final decisions. <br>
Risk: Production examples involve credentials, persistence, identity, and retention controls that are environment-specific. <br>
Mitigation: Define secrets management, durable storage, OIDC or API-key controls, retention policy, and access-control plans before production use. <br>
Risk: Artifact terms describe individual non-commercial research use and paid authorization for government or enterprise use. <br>
Mitigation: Confirm license and commercial authorization status before redistribution, government use, enterprise use, or production deployment. <br>


## Reference(s): <br>
- [NOMOS Decision-Hub skill](https://clawhub.ai/nohn3043-arch/skills/nomos-decision-hub) <br>
- [NOMOS Intelligent Decision-Hub overview](references/README.md) <br>
- [Decision Foundation v0.2](references/DECISION_FOUNDATION_V0_2.md) <br>
- [Intelligent Decision-Hub v0.3](references/INTELLIGENT_DECISION_HUB_V0_3.md) <br>
- [Enterprise deployment guide](references/ENTERPRISE_DEPLOYMENT.md) <br>
- [IMDA AI Verify causal audit report](references/IMDA_AI_Verify_Causal_Audit_Report.pdf) <br>
- [OpenAPI action schema](references/openapi-action.yaml) <br>
- [Market-entry sample decision](references/market_entry.json) <br>
- [Materica compliance design](references/MATERICA_COMPLIANCE_DESIGN.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration, JSON] <br>
**Output Format:** [Markdown guidance with code snippets, shell commands, configuration examples, JSON examples, and OpenAPI reference material.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill is a research and onboarding bundle; the full NOMOS engine must be installed separately before runnable examples can execute.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata); artifact manifest reports 1.1.0 <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
