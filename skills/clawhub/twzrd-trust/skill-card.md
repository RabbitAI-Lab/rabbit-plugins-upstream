## Description:

TWZRD Trust helps agents discover x402 payment endpoints and evaluate seller wallet risk before signing payments using readiness cards, merchant cards, wallet scores, gate checks, and receipt verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[twzrd-sol](https://clawhub.ai/user/twzrd-sol)

### License/Terms of Use:

MIT-0

## Use Case:

External agents, developers, and payment-integrating teams use this skill to check x402 sellers and wallet payment risk before signing or settling USDC-on-Solana payments. It provides guidance for preflight checks, merchant-card review, gate enforcement, and receipt verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill combines wallet and payment workflows with actions that can affect whether an agent signs or refuses a payment.

Mitigation: Review the skill before installing and require manual approval for wallet, funding, payment, and auto-pay commands.

Risk: Some package execution paths are unpinned or allow broad version ranges, which can change the code an agent runs.

Mitigation: Prefer pinned package versions, locked environments, and reviewed dependency updates before running payment-related commands.

Risk: The canonical skill URL can change over time, so automatic replacement could alter behavior without review.

Mitigation: Do not allow automatic skill replacement from the canonical URL without a manual diff and provenance check.

Risk: Seller wallets, prices, and intent fields may be disclosed to TWZRD during trust checks.

Mitigation: Treat those fields as shared with TWZRD and avoid sending sensitive intent details unless disclosure is acceptable.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/twzrd-sol/skills/twzrd-trust)
- [Canonical Skill Definition](https://intel.twzrd.xyz/skill.md)
- [TWZRD Intel Service](https://intel.twzrd.xyz)
- [TWZRD MCP Endpoint](https://intel.twzrd.xyz/mcp)
- [TWZRD OpenAPI](https://intel.twzrd.xyz/openapi.json)
- [TWZRD x402 Descriptor](https://intel.twzrd.xyz/.well-known/x402)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with inline bash, TypeScript, JSON, and HTTP examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires curl for core examples; optional Node packages, wallet tooling, and MCP endpoint configuration are described for payment-gate workflows.]

## Skill Version(s):

1.13.25 (source: server release metadata and skill frontmatter metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
