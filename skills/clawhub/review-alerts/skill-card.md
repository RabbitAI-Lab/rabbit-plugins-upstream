## Description:

Monitors subscribed Amazon ASINs for negative review spikes and rating drops, then helps agents read unread alerts, inspect affected reviews, and generate review analysis or response guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon marketplace operators use this skill to monitor product reviews, detect negative sentiment alerts, review the supporting comments, and request concise reports or response suggestions. It is intended for account-authenticated ARI workflows that may read existing data, create reports, export files, or manage monitoring after the required confirmations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend ARI account credits automatically when account confirmation rules allow it.

Mitigation: Use only with an intended ARI account API key; set autoconfirm off or ask for quote-only behavior when every paid action should require explicit approval.

Risk: The skill makes authenticated network calls and stores an ARI API key locally.

Mitigation: Do not share API keys in chat, verify that ARI_BASE_URL is not set to an unexpected host, and revoke or recreate keys from the ARI account page if access is uncertain.

Risk: The skill can change persistent monitoring/account state and write exported reports or review CSV files locally.

Mitigation: Confirm monitoring changes before execution and choose export destinations deliberately.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/review-alerts)
- [ARI CLI and API Reference](references/reference.md)
- [User Guide](使用说明.md)
- [ARI Account and API Keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI Billing](https://ari.funewa.com/zh/billing)
- [ARI Reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown, concise text, inline shell commands, JSON-backed CLI results, and exported Markdown/HTML/CSV files when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Amazon review samples, trend summaries, report links, credit usage, account status, and local export paths; the skill requires an ARI API key.]

## Skill Version(s):

1.4.8 (source: evidence.release, SKILL.md frontmatter, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
