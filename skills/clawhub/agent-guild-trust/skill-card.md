## Description:

Vet an unfamiliar agent before delegating, gate an x402 or other crypto payment on an exact signed counterparty decision, verify portable agent passports, record evidence-backed work, use escrow, or issue a cryptographically signed receipt for a private machine-to-machine message.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenttanuki](https://clawhub.ai/user/agenttanuki)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and autonomous agent operators use this skill before delegating work, trusting a machine identity, signing a payment, opening escrow, recording an outcome, or issuing a signed private-message receipt. It guides agents to consult Agent Guild and verify exact counterparty, payment, credential, receipt, and routing evidence before acting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can share operational or payment metadata with a public Agent Guild service.

Mitigation: Configure local policy for allowed network calls and omit client telemetry headers when policy forbids telemetry.

Risk: Trust checks, protected decisions, escrow, signed receipts, or x402/PayanAgent flows may involve service fees or autonomous wallet spend.

Mitigation: Require explicit local spend limits, policy approval, and current settlement terms from the live service before any payment action.

Risk: A copied credential, receipt, route, nonce, resource binding, or payment decision can be stale, unsigned, or mismatched.

Mitigation: Verify signatures, issuer, expiry, nonce, recipient, resource, and exact sealed payment fields locally, and fail closed when any check does not verify.

Risk: API keys, wallet keys, identity keys, and private payloads can be exposed through prompts, logs, URLs, or messages.

Mitigation: Keep secrets and private payload bytes local; use hashes or commitments where possible and store returned API keys only as secrets.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/agenttanuki/skills/agent-guild-trust)
- [Server-Resolved Source Provenance](https://github.com/AgentTanuki/agent-guild/tree/main/skills/agent-guild-trust)
- [Agent Guild Service](https://agent-guild-5d5r.onrender.com)
- [Agent Guild MCP Endpoint](https://agent-guild-5d5r.onrender.com/mcp)
- [Agent Guild x402 Payment Policy SDK](https://agent-guild-5d5r.onrender.com/sdk/integrations/x402_payment_policy.mjs)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls]

**Output Format:** [Markdown with curl examples and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May involve live HTTP checks, registration, escrow, signed receipt verification, and local policy approval for wallet or payment actions.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
