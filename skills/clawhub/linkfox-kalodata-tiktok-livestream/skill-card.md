## Description:

Searches Kalodata-backed TikTok Shop livestream leaderboards and retrieves detailed performance metrics for a selected livestream by livestreamId.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to browse TikTok Shop livestream rankings by region, currency, language, and date range, then fetch one livestream's revenue, viewers, duration, GPM, and product count. It is intended for livestream analytics and discovery workflows where paid LinkFox/Kalodata API access is available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a LinkFox/Kalodata API key and makes paid API calls that consume credits.

Mitigation: Confirm each paid call with the user when cost is material, use environment variables for API keys, and avoid sharing keys in chat or logs.

Risk: The skill writes full API responses and request-result caches to local linkfox folders.

Mitigation: Review the local output location before deployment, avoid shared workspaces for sensitive data, and delete cached or saved responses when they are no longer needed.

Risk: The onboarding helper supports account, SMS-code, package, payment, and order-management flows.

Mitigation: Run onboarding, package purchase, or order creation only after explicit user approval, and do not ask users to disclose SMS codes in logged channels.

Risk: The artifact describes automatic feedback reporting to LinkFox when skill quality signals are detected.

Mitigation: Review the feedback behavior before deployment and avoid sending private task context or user-sensitive details unless the user has agreed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-kalodata-tiktok-livestream)
- [Kalodata-TikTok Livestream API Reference](references/api.md)
- [Authentication and Billing Onboarding](references/onboarding.md)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, JSON files, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries and tables, with full JSON API responses saved to local files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are written under a local linkfox session data directory; large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
