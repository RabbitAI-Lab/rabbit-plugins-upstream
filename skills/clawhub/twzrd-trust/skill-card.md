## Description: <br>
TWZRD Trust helps agents discover x402 callables, evaluate Solana seller wallets before payment, apply preflight and gate checks, and verify TWZRD receipts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[twzrd-sol](https://clawhub.ai/user/twzrd-sol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and agent operators use this skill before x402 payments to discover callable services, check seller wallet risk, enforce payment gates where they control signing, and verify receipts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is payment-adjacent and can guide agents toward paid trust calls or wallet-funded workflows. <br>
Mitigation: Review seller decisions, payment amounts, and wallet funding state before approving any payment or AgentCash command. <br>
Risk: TWZRD responses may include next_action.command values for use inside a payment workflow. <br>
Mitigation: Inspect each returned command before execution and run only commands the operator understands and intends to authorize. <br>
Risk: Optional MCP setup and remote service calls route trust checks through TWZRD infrastructure. <br>
Mitigation: Install only when TWZRD participation in x402 seller checks is acceptable for the deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/twzrd-sol/skills/twzrd-trust) <br>
- [Canonical skill file](https://intel.twzrd.xyz/skill.md) <br>
- [TWZRD Trust homepage](https://intel.twzrd.xyz) <br>
- [TWZRD MCP endpoint](https://intel.twzrd.xyz/mcp) <br>
- [Machine-readable x402 descriptor](https://intel.twzrd.xyz/.well-known/x402) <br>
- [OpenAPI specification](https://intel.twzrd.xyz/openapi.json) <br>
- [Facilitator support endpoint](https://intel.twzrd.xyz/supported) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration, Code] <br>
**Output Format:** [Markdown with inline shell commands, HTTP examples, JSON-oriented response interpretation, and TypeScript snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes payment-adjacent decision guidance, optional MCP setup, and receipt verification steps.] <br>

## Skill Version(s): <br>
1.13.4 (source: server release metadata and skill frontmatter metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
