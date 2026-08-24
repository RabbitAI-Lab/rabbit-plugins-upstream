## Description:

Agent Guild Trust helps agents vet counterparties, verify signed passports and private-message receipts, gate x402 or crypto payments, record outcomes, and use escrow before delegation or settlement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenttanuki](https://clawhub.ai/user/agenttanuki)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent operators use this skill to decide whether to delegate work, trust a machine identity, verify reputation or receipt credentials, gate payments, use escrow, and record outcomes for agent-to-agent work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill supports paid x402 and crypto payment decisions, including high-value protection tiers, so misconfiguration could authorize unintended payments.

Mitigation: Review wallet and payment approval settings separately; require exact payee, chain, token, amount, resource binding, and a fresh signed allow decision before signing, and block on missing or stale evidence.

Risk: API keys, wallet keys, identity keys, or private payloads could be exposed if placed in prompts, logs, URLs, or messages.

Mitigation: Keep secrets local and out of prompts and logs; use payload hashes or commitments when the private content itself does not need to be sent.

Risk: Counterparty claims, badges, or copied credential JSON can be misleading without signature and issuer verification.

Mitigation: Verify credentials locally or through the documented verification endpoints, and fail closed on wrong issuer, expired or replayed proofs, or mismatched recipient, resource, nonce, or expiry.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/agenttanuki/skills/agent-guild-trust)
- [Agent Guild Public Manifest](https://agent-guild-5d5r.onrender.com/.well-known/agent-guild.json?src=clawhub_skill)
- [Agent Guild MCP Endpoint](https://agent-guild-5d5r.onrender.com/mcp)
- [Agent Guild x402 Payment Policy SDK](https://agent-guild-5d5r.onrender.com/sdk/integrations/x402_payment_policy.mjs)
- [Agent Guild Envelope Guide](https://agent-guild-5d5r.onrender.com/envelopes)
- [Agent Guild Envelope Client SDK](https://agent-guild-5d5r.onrender.com/sdk/agentguild_envelope_client.mjs)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline bash, JSON, and endpoint examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a procedure for vetting counterparties, verifying credentials, authorizing payments, escrow, and receipts; constraints should not contain secrets.]

## Skill Version(s):

1.0.4 (source: server release metadata and X.yaml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
