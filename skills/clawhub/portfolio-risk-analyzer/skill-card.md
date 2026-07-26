## Description: <br>
Analyzes crypto portfolios across multiple chains for risk exposures, stress tests, and optimization guidance with automated BANKR buyback monetization. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kellyclaudeai](https://clawhub.ai/user/kellyclaudeai) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Crypto traders, DeFi operators, and agents use this skill to inspect wallet exposures, estimate portfolio risk, run stress-test style checks, and generate rebalancing or hedging guidance before taking financial action. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Recurring wallet-funded token buybacks can execute swaps without strong safeguards. <br>
Mitigation: Disable automatic buybacks by default, require explicit approval, and add transaction limits, logs, and emergency stop controls before deployment. <br>
Risk: Payment and buyback flows can expose wallet funds if configured with a main private key. <br>
Mitigation: Use a dedicated low-balance hot wallet, never a main wallet key, and review or replace transaction helper scripts before installation. <br>
Risk: Wallet, voice, SMS/email, and provider API data can contain sensitive user information. <br>
Mitigation: Document privacy handling, minimize stored data, protect provider credentials, and review Twilio and API data flows before production use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kellyclaudeai/skills/portfolio-risk-analyzer) <br>
- [README](README.md) <br>
- [Skill documentation](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Text, JSON API responses, and Markdown-style guidance with shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May require wallet addresses, chain selection, RPC endpoints, provider API keys, and payment or token-holding context.] <br>

## Skill Version(s): <br>
0.1.0 (source: release evidence, skill.json, package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
