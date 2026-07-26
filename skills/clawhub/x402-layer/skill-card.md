## Description: <br>
x402 Singularity Layer helps agents pay for APIs with USDC, deploy and manage monetized endpoints, handle credits, webhooks, marketplace listings, wallet-first agent registration, reputation, support, and staking workflows across Base, Ethereum, Polygon, BSC, Monad, and Solana. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivaavimusic](https://clawhub.ai/user/ivaavimusic) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and agent operators use this skill to integrate x402/Singularity Layer payment flows, deploy monetized APIs, consume paid endpoints, verify webhooks, manage marketplace and control-plane resources, register or rate agents, and perform optional wallet-backed staking or support workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can spend USDC and submit blockchain transactions. <br>
Mitigation: Use a dedicated low-balance wallet and review payment, staking, destination, and network details before executing any spend or signing flow. <br>
Risk: The skill can mutate owner-scoped x402 resources such as endpoints, webhooks, marketplace listings, campaigns, and registrations. <br>
Mitigation: Use scoped API keys or PATs, prefer trusted default hosts, and confirm create, update, delete, registration, and feedback actions before running them. <br>
Risk: Credentialed flows may use wallet private keys, Solana signer keys, endpoint API keys, PATs, AWAL, or OWS. <br>
Mitigation: Set only the credentials required for the selected runbook, avoid long-lived high-value keys, and keep read-only discovery on the no-secret path. <br>
Risk: Some support workflows can revoke XMTP installations. <br>
Mitigation: Review XMTP revoke actions explicitly and avoid revoking installations unless the account owner intends that change. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ivaavimusic/skills/x402-layer) <br>
- [x402 Studio](https://studio.x402layer.cc) <br>
- [OpenClaw skill documentation](https://docs.x402layer.cc/agentic-access/openclaw-skill) <br>
- [Agent Registry and Reputation (ERC-8004 / Solana-8004)](references/agent-registry-reputation.md) <br>
- [Agentic Endpoint Creation](references/agentic-endpoints.md) <br>
- [World AgentKit Benefits](references/agentkit-benefits.md) <br>
- [Credit-Based Access](references/credit-based.md) <br>
- [Marketplace Discovery](references/marketplace.md) <br>
- [Singularity MCP Control Plane](references/mcp-control-plane.md) <br>
- [OpenWallet / OWS (Optional Wallet Backend)](references/openwallet-ows.md) <br>
- [Pay-Per-Request (Direct Mode)](references/pay-per-request.md) <br>
- [Payment Signing Reference](references/payment-signing.md) <br>
- [Integrating Payments Into Your App](references/payments-integration.md) <br>
- [$SGL Staking (agentic)](references/staking.md) <br>
- [Webhooks and Payment Genuineness Verification](references/webhooks-verification.md) <br>
- [XMTP Support in Studio](references/xmtp-support.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, configuration snippets, and code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose wallet, API, webhook, endpoint, marketplace, and staking actions that require user review before execution.] <br>

## Skill Version(s): <br>
1.14.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
