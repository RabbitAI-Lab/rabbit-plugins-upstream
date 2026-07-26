## Description: <br>
A FluxA Agent Wallet skill that enables agents to request budgets, sign x402 payments, and call paid endpoints autonomously. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cpppppp7](https://clawhub.ai/user/cpppppp7) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to let an agent request a bounded FluxA wallet budget, obtain an x402 payment mandate, and call paid HTTP endpoints with X-PAYMENT headers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Delegated payment authority can spend user-approved funds on paid endpoints. <br>
Mitigation: Use small task-specific budgets and verify the exact paid endpoint and payment payload before authorizing spending. <br>
Risk: The bundled wallet CLI exposes direct payout capability beyond x402 payment signing. <br>
Mitigation: Avoid payout commands unless an intentional transfer is part of the task. <br>
Risk: Wallet credentials are stored locally in ~/.fluxa-ai-wallet-mcp/config.json. <br>
Mitigation: Protect that file during use and remove it when the wallet configuration is no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cpppppp7/skills/fluxa-x402-payment) <br>
- [Agent ID initialization guide](initialize-agent-id.md) <br>
- [Payment flow error handling guide](error-handle.md) <br>
- [FluxA Wallet App](https://wallet.fluxapay.xyz) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown instructions with bash and curl command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance may lead an agent to call FluxA wallet services and paid HTTP endpoints after user authorization.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and changelog) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
