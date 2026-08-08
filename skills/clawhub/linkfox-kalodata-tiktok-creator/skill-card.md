## Description:

Searches Kalodata TikTok Shop creator leaderboards and retrieves selected creator profile, performance, sales, contact, and associated shop details by region, currency, language, and date range.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators, analysts, and agents use this skill to discover high-performing TikTok Shop creators and inspect one creator's profile, sales, audience, live/video metrics, contact channels, and associated shops.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: LinkFox may receive creator queries, API credentials, session metadata, phone/SMS login data during onboarding, and feedback text.

Mitigation: Install only if that data sharing is acceptable, avoid submitting sensitive creator queries, and limit onboarding data to what is required.

Risk: The skill includes account and payment flows for authentication and billing recovery.

Mitigation: Review the payment flow before use and confirm any plan or payment selection with the user before executing billing-related commands.

Risk: Full API responses and cache data may be persisted locally and can include creator contact or billing-related information.

Mitigation: Clean up saved linkfox data and cache files when they are no longer needed, especially in shared workspaces.

Risk: Overridden LinkFox endpoint environment variables could route requests away from the expected service.

Mitigation: Avoid running the skill with overridden LinkFox endpoint environment variables unless the endpoint is trusted.

## Reference(s):

- [Kalodata TikTok Creator API Reference](artifact/references/api.md)
- [Authentication and Billing Onboarding](artifact/references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-kalodata-tiktok-creator)
- [Publisher Profile](https://clawhub.ai/user/linkfox-ai)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries, JSON API responses, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes full API responses to dated linkfox data files and may print summaries for large responses.]

## Skill Version(s):

1.0.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
