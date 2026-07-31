## Description: <br>
TWZRD Trust helps agents discover x402 callables and evaluate Solana seller or wallet risk before paying by using preflight, merchant-card, gate-eval, and receipt-verification workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[twzrd-sol](https://clawhub.ai/user/twzrd-sol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and agent operators use this skill to assess x402/Solana sellers before payment, check wallet reputation, apply wash-flag refusal guidance, and verify TWZRD receipts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can direct agents toward service-provided commands in a payment workflow. <br>
Mitigation: Inspect any next_action.command before execution and do not allow automatic execution without operator review. <br>
Risk: The skill describes refreshing itself from an external canonical URL outside ClawHub review. <br>
Mitigation: Avoid external self-updates unless the publisher's canonical URL is intentionally trusted and the fetched content is reviewed before use. <br>
Risk: The security verdict is suspicious despite a coherent payment-safety purpose. <br>
Mitigation: Use the skill only for explicit x402/Solana seller or wallet-risk checks and review it before installing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/twzrd-sol/skills/twzrd-trust) <br>
- [Canonical skill markdown](https://intel.twzrd.xyz/skill.md) <br>
- [TWZRD service homepage](https://intel.twzrd.xyz) <br>
- [Agent orientation](https://intel.twzrd.xyz/llms.txt) <br>
- [x402 descriptor](https://intel.twzrd.xyz/.well-known/x402) <br>
- [OpenAPI 3.1 specification](https://intel.twzrd.xyz/openapi.json) <br>
- [Streamable HTTP MCP endpoint](https://intel.twzrd.xyz/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Markdown] <br>
**Output Format:** [Markdown guidance with HTTP, shell, TypeScript, and JSON-oriented examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl for core HTTP examples; optional flows reference TWZRD gate and receipt-verifier packages.] <br>

## Skill Version(s): <br>
1.13.1 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
