## Description: <br>
Aegis Security guides agents in using blockchain security APIs for token honeypot detection, transaction simulation, address reputation checks, risk scoring, quota checks, x402 payment, and feedback workflows across EVM chains and Solana. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to screen blockchain addresses, tokens, and transactions before DeFi interactions and to decide when manual review or transaction blocking is appropriate. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: External blockchain security API calls can expose addresses, transaction details, client fingerprint identifiers, and optional feedback data. <br>
Mitigation: Install only if that data sharing is acceptable for the intended workflow, and avoid sending private keys, seed phrases, or other secrets. <br>
Risk: Changing client fingerprints can undermine fair quota allocation and may be treated as quota evasion. <br>
Mitigation: Use a stable client fingerprint and do not rotate identifiers to bypass free-tier limits. <br>
Risk: x402 payment integration can spend funds when paid API calls are enabled. <br>
Mitigation: Use a controlled wallet signer and require explicit spending approval before enabling paid retries. <br>
Risk: Blockchain risk classifications are not a 100% guarantee for high-impact decisions. <br>
Mitigation: Require human review for medium, high, or critical findings and for critical transaction decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/aegis-security) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance may include API request examples, risk-level interpretation, quota handling, and x402 payment configuration steps.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
