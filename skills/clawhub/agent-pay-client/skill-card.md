## Description: <br>
Reference client for paying x402 (USDC/EVM) and L402 (Lightning) HTTP 402 paywalls; it detects payment requirements, signs or settles payments only with explicitly provided credentials and spending ceilings, and retries the request with proof of payment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[welove111](https://clawhub.ai/user/welove111) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent builders use this skill to inspect HTTP 402 paywalls and, when explicitly configured with credentials and spending ceilings, complete x402 or L402 payments for API access. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Automatic payment paths can spend real funds when credentials are configured. <br>
Mitigation: Use inspection-only mode by default and enable payment only with explicit credentials, spending ceilings, and a reviewed payable URL allowlist. <br>
Risk: The authoritative security guidance flags L402 auto-pay as unsafe until invoice amount validation and TLS verification are fixed. <br>
Mitigation: Keep L402 in manual-approval mode unless those issues are remediated and reviewed. <br>
Risk: Outdated dependencies can increase exposure in payment and HTTP request handling. <br>
Mitigation: Install with current patched dependencies and review dependency updates before using the client with real funds. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/welove111/skills/agent-pay-client) <br>
- [Publisher Website](https://btc-vision.org) <br>
- [x402 Specification](https://x402.org) <br>
- [L402 Specification](https://docs.lightning.engineering/the-lightning-network/l402) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Python examples and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes payment inspection guidance and configuration details for explicit x402 or L402 payment flows.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
