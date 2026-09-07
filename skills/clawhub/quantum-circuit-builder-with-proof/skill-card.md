## Description:

Quantum Circuit Builder with Proof helps agents build, inspect, certify, verify, export, and simulate quantum circuits with Lean-backed qpcert proof certificates through AgentPMT-hosted remote tool calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentpmt](https://clawhub.ai/user/agentpmt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and quantum computing teams use this skill to generate normalized circuits from templates or provider snippets, certify claim ledgers as qpcerts, verify third-party certificates, and export audit-ready circuit artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Quantum circuit data, claim ledgers, certificates, and Lean source may be sent to AgentPMT-hosted actions.

Mitigation: Submit only the minimum needed circuit and proof material, and do not submit secrets, wallet material, proprietary research, or sensitive certificates.

Risk: Lean-backed actions run trusted Lean in a shared service container rather than an untrusted-code sandbox.

Mitigation: Use only internally trusted Lean source for Lean-backed actions, and prefer normalized-circuit or bounded provider-import flows when they satisfy the task.

Risk: Setup routes may include mutable or unpinned installer commands.

Mitigation: Use pinned or reviewed setup routes for account configuration before connecting MCP or REST access.

## Reference(s):

- [Action schema reference](artifact/schema.md)
- [AgentPMT marketplace product](https://www.agentpmt.com/marketplace/quantum-circuit-builder-with-proof)
- [ClawHub skill page](https://clawhub.ai/agentpmt/skills/quantum-circuit-builder-with-proof)
- [AgentPMT account MCP/REST setup](https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup)
- [What AgentPMT is](https://clawhub.ai/agentpmt/what-is-agentpmt)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Code, Shell commands, Configuration instructions, Files]

**Output Format:** [Markdown with JSON examples, inline shell commands, and file references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can produce or reference qpcert files, circuit diagrams, provider program exports, simulation receipts, and task status results through AgentPMT-hosted actions.]

## Skill Version(s):

1.0.1 (source: artifact/SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
