## Description: <br>
Enforce fine-grained spending policies before executing any payment, transfer, swap, or bridge. Checks Conto policy engine for approval before money leaves your wallet. Use /conto to manage policies or check payments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kwattana](https://clawhub.ai/user/kwattana) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and OpenClaw users use this skill to check payment, transfer, swap, bridge, and x402 API-payment requests against Conto spending policies before funds move. It also supports policy administration and human approval workflows for pending payments when configured with appropriate SDK credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can approve and execute real wallet transfers. <br>
Mitigation: Use low limits and testnet first, and require explicit human confirmation for each transaction before wallet transfer or approval decisions. <br>
Risk: Policy administration commands can create, update, or delete spending policies when an admin SDK key is used. <br>
Mitigation: Prefer a standard SDK key unless policy administration is required, and review policy changes before applying them. <br>
Risk: Setup may store SDK credentials in the OpenClaw configuration file. <br>
Mitigation: Protect ~/.openclaw/openclaw.json and rotate the SDK key if the file may have been exposed. <br>
Risk: If the Conto API is unavailable or returns errors, payment-policy enforcement may be incomplete. <br>
Mitigation: Fail closed on API errors and do not proceed with payments until policy approval is available. <br>


## Reference(s): <br>
- [Conto Homepage](https://conto.finance) <br>
- [ClawHub: Conto Skill](https://clawhub.ai/kwattana/skills/conto) <br>
- [Conto SDK Documentation](https://conto.finance/docs/sdk/skills) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown instructions with bash commands, JSON configuration, and API response guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires CONTO_SDK_KEY, curl, jq, python3, and network access to the Conto API; setup may store SDK credentials in ~/.openclaw/openclaw.json.] <br>

## Skill Version(s): <br>
1.9.0 (source: server release metadata, artifact metadata, and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
