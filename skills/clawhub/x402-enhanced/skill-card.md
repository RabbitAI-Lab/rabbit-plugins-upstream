## Description: <br>
Internet-native payments using the HTTP 402 Payment Required standard. Set up as a buyer to pay for API access, or as a seller to monetize your APIs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[notorious-d-e-v](https://clawhub.ai/user/notorious-d-e-v) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to implement x402 buyer clients, seller APIs, facilitator configuration, paywall middleware, and testnet-to-production payment setup. It is intended for agents helping with code, shell commands, and configuration for x402-based API payments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent toward direct crypto payment signing and paid API requests. <br>
Mitigation: Require explicit user confirmation before each paid request and configure external wallet or facilitator-side spending limits. <br>
Risk: Private wallet keys may be exposed through chat, logs, or generated configuration examples. <br>
Mitigation: Use dedicated low-balance wallets, prefer testnet while developing, and keep private keys out of prompts, logs, and shared files. <br>


## Reference(s): <br>
- [x402 Documentation](https://docs.x402.org) <br>
- [x402 GitHub Repository](https://github.com/coinbase/x402) <br>
- [ClawHub Skill Page](https://clawhub.ai/notorious-d-e-v/skills/x402-enhanced) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell, TypeScript, Python, and Go code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes buyer and seller examples, payment environment variables, facilitator URLs, network identifiers, paywall setup, and testing guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
