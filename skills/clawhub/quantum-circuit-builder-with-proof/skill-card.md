## Description:

Builds proof-carrying quantum circuits, certifies explicit claims with a pinned Lean kernel, verifies external qpcerts, and exports checked offline provider programs through AgentPMT-hosted remote tool calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentpmt](https://clawhub.ai/user/agentpmt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create, certify, exchange, verify, export, and simulate quantum circuit artifacts when circuits must cross a trust boundary or support audit review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid remote proof, verification, export, and simulation actions can spend credits when invoked.

Mitigation: Confirm the user intends to use AgentPMT-hosted paid quantum circuit proof tools before calling paid actions.

Risk: Submitted Lean runs as trusted_direct_v1 in a shared service container rather than an untrusted-code sandbox.

Mitigation: Submit only internally trusted Lean source and inspect receipt fields for execution mode and isolation status.

Risk: Circuit validation, visualization, provider import, provider export, and local simulation can be mistaken for proof or hardware execution.

Mitigation: Describe proof scope precisely and rely on qpcerts from certification or independent verification when proof is required.

Risk: Account secrets, wallet private keys, mnemonics, signatures, or payment headers could be exposed if placed in prompts or logs.

Mitigation: Keep secrets out of prompts and logs and use the setup skill for credential handling.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/agentpmt/skills/quantum-circuit-builder-with-proof)
- [AgentPMT marketplace product](https://www.agentpmt.com/marketplace/quantum-circuit-builder-with-proof)
- [Quantum Circuit Builder with Proof schema](artifact/schema.md)
- [AgentPMT account MCP/REST setup](https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup)
- [What AgentPMT is](https://clawhub.ai/agentpmt/what-is-agentpmt)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Code, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown instructions with JSON request examples, shell command snippets, and references to generated files such as qpcerts, provider programs, and circuit images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Remote tool actions may return background task IDs, budget-scoped File Manager outputs, certificate files, provider source artifacts, simulator receipts, and PNG or JPEG circuit visualizations.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
