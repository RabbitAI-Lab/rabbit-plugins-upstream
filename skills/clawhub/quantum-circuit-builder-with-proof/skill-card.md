## Description:

Builds and verifies proof-carrying quantum circuit artifacts, including normalized circuits, qpcerts, provider exports, simulations, and recipient-side certificate replay through AgentPMT-hosted tool calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentpmt](https://clawhub.ai/user/agentpmt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and researchers use this skill to construct, inspect, certify, export, simulate, and independently verify quantum circuit artifacts when audit-ready evidence is required.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Trusted Lean source may execute in a shared service container rather than an untrusted-code isolation boundary.

Mitigation: Submit only internally trusted Lean source; use normalized circuit certification or recipient-side certificate verification for external inputs when possible.

Risk: Paid or background proof actions can duplicate work if an agent resubmits while a task is still processing.

Mitigation: Poll the existing task with get_task and the returned task_id instead of rapidly polling or submitting duplicate paid actions.

Risk: Unpinned setup commands can reduce reproducibility for a release workflow.

Mitigation: Prefer ClawHub or OpenClaw install routes when reproducible installation is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/agentpmt/skills/quantum-circuit-builder-with-proof)
- [AgentPMT marketplace product](https://www.agentpmt.com/marketplace/quantum-circuit-builder-with-proof)
- [Quantum Circuit Builder with Proof Schema](artifact/schema.md)
- [AgentPMT account MCP/REST setup](https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup)
- [What AgentPMT is](https://clawhub.ai/agentpmt/what-is-agentpmt)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Code, Files, Configuration]

**Output Format:** [Markdown instructions with JSON action parameters and generated file artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Background tasks may return qpcert files, circuit diagrams, provider programs, simulator receipts, and certificate verification receipts.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
