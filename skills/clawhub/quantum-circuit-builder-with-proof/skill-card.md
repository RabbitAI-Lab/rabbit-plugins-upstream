## Description:

Quantum Circuit Builder with Proof helps agents build, inspect, export, simulate, certify, and independently verify proof-carrying quantum circuit artifacts through AgentPMT-hosted remote tool calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentpmt](https://clawhub.ai/user/agentpmt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and auditors use this skill when a quantum circuit needs machine-checkable evidence, provider exports, simulation receipts, or independent replay of an externally supplied qpcert. It is most relevant when proof scope and trust boundaries need to be explicit rather than implied by a normal circuit-building workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary marks the release suspicious because it delegates authority to live remote instructions and uses hosted services for proof-related work.

Mitigation: Install from pinned or verified setup routes, check freshness before relying on endpoints or schemas, and review the returned action results rather than treating remote guidance as proof.

Risk: Circuit data and trusted Lean source may be sent to AgentPMT remote services.

Mitigation: Submit only data that is appropriate for the AgentPMT service, avoid secrets and third-party confidential material, and keep tool inputs scoped to the minimum needed for the task.

Risk: Submitted Lean for certification, export, or local execution runs in a shared cloud service mode that is not untrusted-code isolation.

Mitigation: Use only internally trusted Lean source, do not submit adversarial Lean, and inspect receipt fields such as execution_mode and untrusted_code_isolation when assessing results.

Risk: Several actions are paid and proof-related work runs as background tasks.

Mitigation: Poll existing tasks with the free get_task action, avoid duplicate paid submissions while processing, and confirm the relevant credit cost before invoking paid actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/agentpmt/skills/quantum-circuit-builder-with-proof)
- [AgentPMT marketplace product](https://www.agentpmt.com/marketplace/quantum-circuit-builder-with-proof)
- [AgentPMT account MCP/REST setup](https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup)
- [AgentPMT file management](https://clawhub.ai/agentpmt/file-management)
- [What is AgentPMT](https://clawhub.ai/agentpmt/what-is-agentpmt)
- [Artifact skill instructions](artifact/SKILL.md)
- [Artifact action schema](artifact/schema.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with JSON tool parameters, code examples, file references, receipts, certificates, diagrams, and provider-source exports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Remote actions may create background tasks, consume listed credits, and return qpcert files, PNG/JPEG circuit diagrams, JSON receipts, OpenQASM 3, Qiskit, Cirq, or Braket source artifacts.]

## Skill Version(s):

1.0.4 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
