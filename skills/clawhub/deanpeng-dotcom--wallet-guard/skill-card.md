## Description: <br>
Wallet Guard helps agents assess Web3 wallet, token, approval, NFT, and phishing risks using Antalpha/GoPlus-backed security checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deanpeng-dotcom](https://clawhub.ai/user/deanpeng-dotcom) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, security reviewers, and Web3 users use this skill through an agent to scan wallet addresses, token contracts, approvals, NFT contracts, and suspicious URLs before transactions or wallet connections. It provides security guidance and risk findings, not a cryptographic guarantee of safety. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Wallet addresses, contract addresses, URLs, chain selections, and optional GoPlus credentials may be sent to external Antalpha/GoPlus-backed services. <br>
Mitigation: Use only non-secret public addresses and URLs, avoid seed phrases, private keys, and wallet-signing approvals, and confirm that external service use fits the user's privacy requirements. <br>
Risk: A clean scan is security guidance and may miss risks outside the supported checks, chains, or available third-party data. <br>
Mitigation: Treat results as decision support, verify high-value transactions independently, and review risky approvals with trusted revocation tools before acting. <br>
Risk: External service failures, timeouts, or invalid responses can prevent a reliable scan. <br>
Mitigation: If a scan cannot be completed, do not infer safety; retry later or perform manual review before transacting. <br>


## Reference(s): <br>
- [Wallet Guard on ClawHub](https://clawhub.ai/deanpeng-dotcom/wallet-guard) <br>
- [GoPlus Security](https://gopluslabs.io) <br>
- [Revoke.cash](https://revoke.cash) <br>
- [Antalpha](https://antalpha.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Concise Markdown security reports with risk scores, key findings, and recommended actions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses should avoid raw JSON, mask addresses unless full values are needed, and attribute data to Antalpha AI data aggregation.] <br>

## Skill Version(s): <br>
3.0.2 (source: server release evidence and SKILL.md frontmatter, released 2026-06-18) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
