## Description:

Operate HeyTraders through the live heytraders_cli browser command catalog when the user asks to inspect, navigate, configure, or manage the HeyTraders application.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heytraders](https://clawhub.ai/user/heytraders)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to inspect, navigate, configure, and manage the HeyTraders application through the live HeyTraders browser command catalog while leaving credentials, authentication, wallet approvals, and final financial decisions with the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can help operate a trading application, where state changes or financial actions may have real consequences.

Mitigation: Keep final trade approvals, wallet approvals, exchange connections, login, CAPTCHA, and 2FA in the user's hands, and require explicit user instruction before financial or irreversible actions.

Risk: Using stale command names, identifiers, schemas, or readiness information could produce incorrect actions or misleading guidance.

Mitigation: Refresh commands, schemas, readiness, identifiers, and results from the live HeyTraders browser command catalog before acting or claiming success.

Risk: Credential or secret exposure could occur if sensitive values are passed through the browser tool.

Mitigation: Do not send login details, API keys, exchange credentials, wallet secrets, tokens, cookies, private keys, browser storage, or recovery phrases through heytraders_cli.

## Reference(s):

- [HeyTraders](https://hey-traders.com)
- [ClawHub skill page](https://clawhub.ai/heytraders/skills/heytraders)
- [Publisher profile](https://clawhub.ai/user/heytraders)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with structured JSON command envelopes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves structured errors and user-action-required results from the live browser tool.]

## Skill Version(s):

2.0.0 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
