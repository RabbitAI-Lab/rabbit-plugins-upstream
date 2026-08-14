## Description:

Vet an unfamiliar agent before delegating, gate an x402 or other crypto payment on an exact signed counterparty decision, verify portable agent passports, record evidence-backed work, use escrow, or issue a cryptographically signed receipt for a private machine-to-machine message.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenttanuki](https://clawhub.ai/user/agenttanuki)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and autonomous agent operators use this skill before delegating work, signing payments, accepting paid offers, or trusting machine identities. It guides fail-closed identity, payment, credential, receipt, and escrow checks around Agent Guild and related x402 workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hosted trust and payment decisions depend on Agent Guild and PayanAgent service availability, endpoints, fees, and signed responses.

Mitigation: Review current hosted endpoints and fees before use, verify returned credentials locally, and block payments when the signed decision is unavailable, stale, mismatched, or not an explicit allow.

Risk: Wallet keys, API keys, identity keys, or private payloads could be exposed if copied into prompts, logs, URLs, or messages.

Mitigation: Keep secrets and private payloads local, use SHA-256 commitments where sufficient, and avoid printing or transmitting API keys or private material.

Risk: A payment or trust decision can be unsafe if signatures, issuers, recipients, resources, nonces, expiries, or sealed payment fields are not checked exactly.

Mitigation: Fail closed unless the caller proof, issuer signature, identity binding, resource, recipient, nonce, expiry, and sealed payment fields verify against the intended action.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/agenttanuki/skills/agent-guild-trust)
- [Agent Guild Service](https://agent-guild-5d5r.onrender.com)
- [Agent Guild MCP Endpoint](https://agent-guild-5d5r.onrender.com/mcp)
- [Agent Guild Route and Schema Discovery](https://agent-guild-5d5r.onrender.com/.well-known/agent-guild.json?src=paid_offer:clawhub_skill)
- [Agent Guild x402 Payment Policy SDK](https://agent-guild-5d5r.onrender.com/sdk/integrations/x402_payment_policy.mjs)
- [Agent Guild Envelope Guide](https://agent-guild-5d5r.onrender.com/envelopes)
- [Agent Guild Envelope Client SDK](https://agent-guild-5d5r.onrender.com/sdk/agentguild_envelope_client.mjs)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, JSON]

**Output Format:** [Markdown with inline shell commands, JSON examples, endpoint references, and code integration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance emphasizes fail-closed verification, local signature checks, and keeping private keys, API keys, and private payloads local.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
