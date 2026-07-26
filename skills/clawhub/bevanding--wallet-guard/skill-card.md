## Description: <br>
Wallet Guard helps agents check Web3 wallet, token, approval, NFT, phishing-site, and DeFi rug-pull risks using Antalpha/GoPlus-backed security services. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bevanding](https://clawhub.ai/user/bevanding) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to request wallet security checks, token contract scans, address blacklist checks, approval risk reviews, NFT safety checks, phishing-site detection, and DeFi rug-pull risk guidance before interacting with Web3 assets. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Wallet addresses, contract addresses, approval targets, URLs, and optional GoPlus credentials may be sent to Antalpha/GoPlus-backed services for analysis. <br>
Mitigation: Install only if this data sharing is acceptable; use limited-purpose GoPlus credentials and avoid submitting unnecessary identifiers. <br>
Risk: Scan results are risk guidance rather than a guarantee of wallet safety, and beta or unavailable external checks may have limited accuracy. <br>
Mitigation: Treat clean results as advisory, verify high-value decisions with additional tools, and use manual revocation workflows when risk is found or scans fail. <br>
Risk: Unspecified chains can trigger broader multi-chain approval scans than needed. <br>
Mitigation: Specify the intended chain whenever possible to reduce unnecessary checks and data exposure. <br>


## Reference(s): <br>
- [ClawHub Wallet Guard release](https://clawhub.ai/bevanding/wallet-guard) <br>
- [Antalpha AI MCP server](https://mcp.antalpha.com/wallet-guard) <br>
- [GoPlus Security](https://gopluslabs.io) <br>
- [Revoke.cash](https://revoke.cash) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, API Calls, Guidance] <br>
**Output Format:** [Markdown security report with concise findings and remediation guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses wallet addresses, contract addresses, chain IDs, URLs, and optional GoPlus API credentials; user-facing responses are limited to the most important findings.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata, SKILL.md frontmatter, README changelog) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
