## Description:

Turns an approved POC PRD into a runnable, risk-controlled deployment architecture and delivery plan covering boundaries, data, permissions, integrations, environments, observability, and risk.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xukun0821](https://clawhub.ai/user/xukun0821)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, field delivery engineers, and solution architects use this skill to turn an approved POC PRD into a deployment architecture and risk package for controlled POC implementation, architecture review, integration planning, and pre-deployment decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive customer or production material may be shared with the agent during architecture planning.

Mitigation: Confirm what data may be shared before use; minimize or de-identify sensitive inputs and treat generated plans as review artifacts.

Risk: A generated deployment plan could be mistaken for authorization to connect to production, transfer external data, change permissions, deploy, or roll back.

Mitigation: Require explicit human confirmation and owner approval for production connections, external data transfer, permission changes, deployment, and rollback.

Risk: POC architecture or technical debt may be copied into production without required controls.

Mitigation: Perform security and compliance review, document POC-to-production gaps, and block production readiness until residual risks are accepted by authorized owners.

Risk: Architectures involving external content or executable tools may introduce prompt-injection, excessive-permission, or unsafe-output risks.

Mitigation: Treat external content as data, apply least privilege, require confirmation for high-risk actions, and verify outputs before writing to downstream systems.

## Reference(s):

- [FDE Deployment Architect Skill Page](https://clawhub.ai/xukun0821/skills/fde-deployment-architect)
- [Deployment Architecture Input Guide](references/architecture-input-guide.md)
- [POC Deployment Architecture Rules](references/architecture-rules.md)
- [Agent Deployment Security Check](references/security-checklist.md)
- [POC Technology Selection Guide](references/technology-selection-guide.md)
- [Deployment Architecture and Risk Package Template](references/deployment-architecture-pack.md)
- [POC to Production Transition](references/production-transition.md)
- [Deployment Architecture Quality Score](references/architecture-quality-rubric.md)
- [POC Architecture Field Manual](references/architecture-field-handbook.md)
- [Complete Example of Deployment Architecture](references/architecture-worked-example.md)
- [Public Method Sources](references/public-sources.md)
- [Azure Well-Architected Framework](https://learn.microsoft.com/en-us/azure/well-architected/)
- [Microsoft: Architects Collaborate with Workload Teams](https://learn.microsoft.com/en-us/azure/well-architected/architect-role/collaboration)
- [Martin Fowler: Architecture Decision Record](https://martinfowler.com/bliki/ArchitectureDecisionRecord.html)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [OWASP LLM06: Excessive Agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/)
- [Azure: Architecture Testing Strategy](https://learn.microsoft.com/en-us/azure/well-architected/operational-excellence/testing)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown deployment architecture and risk package with tables, decision records, risk lists, and production-transition notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Planning output only; no cloud, network, IAM, or production resource changes by default.]

## Skill Version(s):

1.0.0 (source: server release metadata and TRUST-CARD.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
