## Description:

Searches Kalodata TikTok Shop leaderboards and retrieves a selected shop's detail by shopId, including revenue, sales volume, product counts, revenue channel split, and creator, video, and livestream counts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce analysts, sellers, and agents use this skill to browse TikTok Shop leaderboards by market and time window, then inspect a selected shop's sales, product, revenue-channel, and creator engagement metrics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a LinkFox API key and can use environment-configured gateway URLs.

Mitigation: Install only in environments where the LinkFox credential is approved for agent use, and review LINKFOX_TOOL_GATEWAY and related overrides before running lookups.

Risk: The skill writes full lookup responses to local linkfox session directories.

Mitigation: Review local retention expectations and avoid running it in workspaces where saved TikTok shop metrics or account-related outputs should not persist.

Risk: The bundled onboarding flow can perform SMS login and payment order actions.

Mitigation: Use those commands only after explicit user intent, and prefer existing approved credentials or manual account management when available.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-kalodata-tiktok-shop)
- [Kalodata TikTok Shop API Reference](references/api.md)
- [Authentication and Billing Onboarding](references/onboarding.md)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, JSON files, shell commands, configuration guidance, API calls]

**Output Format:** [Markdown summaries and tables, stdout JSON or summaries, and saved JSON response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes full lookup responses under a local linkfox session directory; large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
