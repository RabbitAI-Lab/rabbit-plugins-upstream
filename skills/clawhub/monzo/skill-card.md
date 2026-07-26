## Description: <br>
Access Monzo bank account - check balance, view transactions, manage pots, send feed notifications. For personal finance queries and banking automation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rhesketh](https://clawhub.ai/user/rhesketh) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and agents use this skill to connect to a user's Monzo account, check balances, review transaction history, manage savings pots, attach receipts, send app feed notifications, and manage webhooks through command-line scripts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can maintain persistent Monzo API access through stored OAuth credentials. <br>
Mitigation: Install only on a machine the user controls, protect MONZO_KEYRING_PASSWORD, keep credential and config files restricted, and review Monzo connected apps regularly. <br>
Risk: The skill can perform account-changing actions such as pot movement, receipt deletion, transaction annotation, feed notifications, and webhook changes without built-in confirmation. <br>
Mitigation: Require explicit user confirmation before running any command that changes account state or creates external notifications or webhooks. <br>
Risk: Secrets may be exposed through shared config, shell history, process listings, or compromised local systems. <br>
Mitigation: Use a secrets manager or restricted environment file where possible, avoid putting real secrets in shared files or command history, and revoke Monzo API access if the host is compromised. <br>
Risk: Webhooks can send transaction notifications to configured endpoints. <br>
Mitigation: Register only HTTPS endpoints controlled by the user and validate Monzo webhook signatures, rate limit requests, and monitor webhook activity. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/rhesketh/skills/monzo) <br>
- [Monzo Developer Portal](https://developers.monzo.com/) <br>
- [Monzo](https://monzo.com) <br>
- [OpenClaw](https://github.com/openclaw/openclaw) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and human-readable or JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires MONZO_KEYRING_PASSWORD and local CLI tools curl, jq, openssl, and bc; some operations require Monzo app approval.] <br>

## Skill Version(s): <br>
1.0.2 (source: release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
