## Description:

Use when configuring OpenClaw to run TWZRD preflight checks before payment-shaped x402 tool calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[twzrd-sol](https://clawhub.ai/user/twzrd-sol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw operators use this skill to configure a preflight gate for payment-shaped x402 or AgentCash-style tool calls before payment details can reach a signer.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Payment metadata is sent to the TWZRD service for preflight evaluation.

Mitigation: Review the endpoint, mode, failMode, wallet allow/deny lists, and matcher settings before deployment.

Risk: The default enforce and fail-closed posture can block payment-shaped tool calls before they reach a signer.

Mitigation: Use the failMode and shadow-mode settings deliberately during rollout, and confirm that blocking behavior matches the operator's payment policy.

## Reference(s):

- [TWZRD Preflight on ClawHub](https://clawhub.ai/twzrd-sol/skills/twzrd-preflight)
- [TWZRD Intel Endpoint](https://intel.twzrd.xyz)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with bash and JSON code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides npm installation, OpenClaw plugin configuration, and HTTP client wrapping guidance.]

## Skill Version(s):

0.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
