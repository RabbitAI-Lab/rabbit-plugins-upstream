## Description: <br>
Checks Solana wallets and x402 sellers before payment by returning readiness, trust, merchant, and receipt-verification guidance from TWZRD's observed payment corpus. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[twzrd-sol](https://clawhub.ai/user/twzrd-sol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to preflight Solana wallet and x402 seller payments, check merchant and wallet trust signals, decide whether to proceed, and verify TWZRD receipts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can influence whether an agent signs or sends Solana/x402 payments. <br>
Mitigation: Require explicit workflow approval before acting on payment decisions or changing payment routing. <br>
Risk: Paid x402 trust and merchant calls can spend USDC on Solana. <br>
Mitigation: Run the free preflight and merchant-card checks first, then require operator approval before paid endpoints are called. <br>
Risk: The skill may involve network calls, optional package installs, MCP setup, facilitator routing changes, and canonical skill refreshes. <br>
Mitigation: Approve endpoint changes, package installs, MCP additions, routing changes, and refreshes before execution. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/twzrd-sol/skills/twzrd-trust) <br>
- [Canonical Skill Source](https://intel.twzrd.xyz/skill.md) <br>
- [TWZRD Service Homepage](https://intel.twzrd.xyz) <br>
- [TWZRD MCP Endpoint](https://intel.twzrd.xyz/mcp) <br>
- [TWZRD OpenAPI 3.1 Descriptor](https://intel.twzrd.xyz/openapi.json) <br>
- [TWZRD x402 Descriptor](https://intel.twzrd.xyz/.well-known/x402) <br>
- [TWZRD Facilitator Support](https://intel.twzrd.xyz/supported) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, text, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with curl and npx shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses TWZRD HTTP and optional MCP endpoints; no API key is required; paid x402 calls may spend USDC on Solana.] <br>

## Skill Version(s): <br>
1.8.0 (source: server release evidence; artifact metadata version 1.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
