## Description: <br>
FluxA Agent Wallet lets AI agents use a user's wallet within approved scope for x402 payments, USDC transfers, payment links, agent-to-agent transfers, AI social gifting, paid API calls, payment-enabled skills, and related wallet workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cpppppp7](https://clawhub.ai/user/cpppppp7) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent perform approved wallet actions such as paying x402 resources, transferring USDC, creating or paying payment links, issuing short-lived agent identity credentials, and coordinating payment-enabled workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Real-money wallet workflows expose sensitive payment authority and can move funds or reuse mandates beyond the user's intent. <br>
Mitigation: Require explicit confirmation for every transfer, payout, card action, paid API call, and mandate reuse; keep mandates scoped by purpose, amount, and time window. <br>
Risk: Tokens, JWTs, payment headers, payer emails, mandate files, and card details can expose wallet credentials or payment data. <br>
Mitigation: Treat these values as sensitive, avoid revealing raw card details to the agent, do not log JWT credentials, and keep local wallet and mandate files protected. <br>
Risk: Unpinned or outdated wallet tooling can change payment behavior or fail during sensitive wallet operations. <br>
Mitigation: Pin and review CLI/package versions before use, and update deliberately after reviewing the release and security posture. <br>
Risk: Scheduled wallet check-ins can create recurring agent activity around payments and security announcements. <br>
Mitigation: Disable scheduled check-ins unless the user has reviewed and approved the scheduled behavior. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cpppppp7/skills/fluxa-agent-wallet) <br>
- [FluxA Agent Wallet overview](artifact/SKILL.md) <br>
- [Mandate Planning Policy](artifact/MANDATE-PLANNING.md) <br>
- [x402 Payment Reference](artifact/X402-PAYMENT.md) <br>
- [Payout CLI Reference](artifact/PAYOUT.md) <br>
- [Payment Link CLI Reference](artifact/PAYMENT-LINK.md) <br>
- [Transfer to Agent](artifact/TRANSFER-TO-AGENT.md) <br>
- [Agent ID Integration Guide](artifact/INTEGRATION-GUIDE-AGENTID.md) <br>
- [Agent VC CLI Reference](artifact/VC-ISSUE.md) <br>
- [x402 Services Discovery](artifact/x402-SERVICES.md) <br>
- [FluxA Monetize API discovery](https://monetize.fluxapay.xyz/api/discover?type=api) <br>
- [FluxA Monetize skill discovery](https://monetize.fluxapay.xyz/api/discover?type=skill) <br>
- [Agent ID JWT verification documentation](https://docs.fluxapay.xyz/wallet/agent-guide-jwt-verification.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with CLI commands, JSON examples, URLs, and configuration instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include payment authorization URLs, mandate identifiers, payment headers, JWT or VC handling guidance, and local wallet state paths that should be treated as sensitive.] <br>

## Skill Version(s): <br>
1.4.5 (source: server release evidence and target metadata; artifact text also references skill/CLI 0.4.5) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
