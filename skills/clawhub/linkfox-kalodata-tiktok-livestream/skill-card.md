## Description:

Searches Kalodata TikTok Shop livestream leaderboards and retrieves detailed performance metrics for a selected livestream by livestreamId.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and commerce analysts use this skill to browse TikTok Shop livestream rankings by market, currency, language, and date range, then inspect one livestream's revenue, viewers, duration, GPM, and product count. It is useful for data lookup and reporting, not for ad management or content creation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses LinkFox API keys and can call paid Kalodata endpoints that consume credits.

Mitigation: Install only when the user accepts the paid LinkFox/Kalodata integration, keep API keys private, and warn before repeated or expanded calls that may incur additional credit usage.

Risk: The skill makes external network calls and allows LINKFOX_* gateway environment variables to override service endpoints.

Mitigation: Use trusted endpoint values only, avoid pointing gateway variables at untrusted hosts, and review network behavior before deployment.

Risk: The scripts store full response and cache files locally, which may include detailed livestream analytics and account-adjacent session metadata.

Mitigation: Keep generated linkfox response and cache files out of shared or committed workspaces, and clean local artifacts according to the user's retention policy.

Risk: Onboarding can guide users through phone-based login and payment flows.

Mitigation: Use the onboarding flow only when authentication or billing evidence requires it, and ensure users understand the account and payment action before continuing.

Risk: The evidence security verdict is suspicious because feedback, onboarding, credential, payment, persistence, and external-call behavior need manual review.

Mitigation: Review the release and security evidence before installation, and disable or restrict automatic feedback reporting where that is not appropriate.

## Reference(s):

- [Kalodata-TikTok直播搜索与详情 API Reference](references/api.md)
- [Authentication and Billing Onboarding](references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-kalodata-tiktok-livestream)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with JSON API responses and saved response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts save full API responses under a local linkfox session directory, use a 24-hour parameter cache by default, and print either full JSON or a summarized response depending on size.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
