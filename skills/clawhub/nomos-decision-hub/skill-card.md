## Description: <br>
NOMOS Decision Hub helps agents analyze deterministic decision workflows with causal tracing, scenario stress testing, auditable records, and human governance boundaries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nohn3043-arch](https://clawhub.ai/user/nohn3043-arch) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, governance teams, and decision-system reviewers use this skill to design, inspect, and explain deterministic decision engines, audit trails, scenario stress tests, API contracts, and deployment patterns for high-stakes choices. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: External compliance claims may influence adoption or trust decisions. <br>
Mitigation: Verify compliance claims and supporting reports before relying on them for production approval. <br>
Risk: Example deployment commands include API key and database connection patterns that could expose secrets if copied directly. <br>
Mitigation: Use a secret manager or orchestrator-managed secrets for API keys and database DSNs. <br>
Risk: High-stakes decision workflows can lead users to over-rely on generated rankings or reports. <br>
Mitigation: Keep human authorization, real authentication, tenant isolation, backups, and durable audit storage in the production deployment path. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/nohn3043-arch/skills/nomos-decision-hub) <br>
- [Project homepage](https://github.com/NOHN-AI/second-perspective) <br>
- [README](artifact/README.md) <br>
- [Intelligent Decision Hub v0.3](artifact/docs/INTELLIGENT_DECISION_HUB_V0_3.md) <br>
- [Decision Foundation v0.2](artifact/docs/DECISION_FOUNDATION_V0_2.md) <br>
- [OpenAPI action contract](artifact/openapi-action.yaml) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Python, shell, YAML, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce deployment and API examples for review before execution; final decisions remain with human or organizational authorities.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
