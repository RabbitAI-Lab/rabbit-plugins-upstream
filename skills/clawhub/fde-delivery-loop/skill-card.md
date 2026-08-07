## Description:

An end-to-end delivery skill for Forward Deployed Engineers, solution architects, and enterprise AI POC teams that combines one delivery router with eight specialist modules to turn ambiguous customer needs into evidence, a POC charter, an acceptance-ready PRD, deployment architecture, an Agent Skill, POC evidence, adoption and value conclusions, and reusable delivery assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xukun0821](https://clawhub.ai/user/xukun0821)

### License/Terms of Use:

MIT-0

## Use Case:

Forward Deployed Engineers, solution architects, and enterprise AI POC teams use this skill to route customer-facing AI POC work through discovery, chartering, PRD handoff, deployment architecture, skill and POC design, validation, adoption review, and productization. It supports evidence-based handoffs, audits, rollback decisions, and reusable delivery assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local delivery artifacts, project state logs, or demo inputs may capture sensitive customer information if users include it.

Mitigation: Do not place secrets or raw customer data in state files or demo inputs; review and sanitize generated artifacts before sharing or reuse.

Risk: Optional runnable POC scaffolds could be connected to real systems before the engagement has approved requirements, architecture, permissions, and controls.

Mitigation: Use mocks for demonstrations and require architecture, security, and authorization review before connecting any generated POC to real systems.

Risk: Generated handoffs can overstate POC success, production readiness, adoption, or business value if evidence is incomplete.

Mitigation: Keep success criteria, pass/fail evidence, owners, and rollback points explicit; separate POC success, production readiness, adoption, and business value as distinct reviewed claims.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/xukun0821/skills/fde-delivery-loop)
- [FDE Delivery Loop Overview](SKILL.md)
- [FDE Delivery Router](fde-delivery-router/MODULE.md)
- [FDE Problem Discovery](fde-problem-discovery/MODULE.md)
- [FDE POC Engagement Charter](fde-engagement-charter/MODULE.md)
- [FDE PRD Writer | POC Handoff](fde-prd-writer/MODULE.md)
- [FDE Deployment Architecture](fde-deployment-architect/MODULE.md)
- [FDE Skill and POC Builder](fde-agent-skill-designer/MODULE.md)
- [FDE POC Run and Validation](fde-poc-runner/MODULE.md)
- [FDE Adoption and Value](fde-adoption-and-value/MODULE.md)
- [FDE Delivery Productizer](fde-playbook-productizer/MODULE.md)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [OWASP LLM06: Excessive Agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/)
- [AWS Generative AI Lifecycle Operational Excellence Framework](https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/understanding-gloe.html)
- [OpenAI Practical Guide to Building Agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown packages, JSON state files, code and configuration scaffolds, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local delivery artifacts, project state logs, validation reports, and optional runnable POC scaffolds when requested by the user.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
