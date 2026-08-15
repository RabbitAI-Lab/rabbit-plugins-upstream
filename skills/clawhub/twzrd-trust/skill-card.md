## Description:

TWZRD Trust helps agents discover x402 callables, evaluate Solana sellers before payment, enforce pre-sign payment gates, and optionally retrieve paid trust receipts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[twzrd-sol](https://clawhub.ai/user/twzrd-sol)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to check x402 sellers before signing or sending USDC, wire buyer-side payment gates, inspect seller readiness, and verify receipts. It is intended for agents that need pre-spend risk checks, merchant-card context, and optional paid trust intelligence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Payment-capable paths can move funds if an agent enables paid auto-pay or legacy wallet settings.

Mitigation: Use the hosted/free read-only path unless paid auto-pay is intentional, avoid setting wallet secret environment variables by default, and set strict per-call and session spend caps.

Risk: Telemetry and authorization behavior require review before unattended deployment.

Mitigation: Review the release security summary, decide whether delivery telemetry is acceptable, and disable delivery capture with TWZRD_DELIVERY_CAPTURE=0 when appropriate.

Risk: A warn decision is advisory and is not a hard approval to sign.

Mitigation: Treat warn as a policy choice, respect returned caps, and require buyer-side gate enforcement before signing on host payment paths.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/twzrd-sol/skills/twzrd-trust)
- [Canonical skill file](https://intel.twzrd.xyz/skill.md)
- [TWZRD Agent Intel](https://intel.twzrd.xyz)
- [MCP endpoint](https://intel.twzrd.xyz/mcp)
- [TWZRD Trust Assurance](docs/security-assurance.md)
- [Seller graph pay-guard closeout proof](docs/proofs/seller-graph-payguard-closeout-2026-07-12.md)
- [External refuse proof](docs/proofs/20260716-wash-refuse-transcript.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell and TypeScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference HTTP API calls, MCP tools, npm packages, environment variables, seller decisions, spend caps, and receipt verification steps.]

## Skill Version(s):

1.13.8 (source: server release, skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
