## Description:

Searches Kalodata TikTok Shop video leaderboards and retrieves detailed video engagement, sales, GPM, and advertising metrics by video ID.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce operators and analysts use this skill to discover high-performing TikTok Shop videos and inspect one selected video's performance metrics. It is also used to guide authentication, credit balance, and payment steps needed to call the LinkFox/Kalodata APIs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends API requests, account onboarding data, billing actions, and automatic feedback to LinkFox/Kalodata endpoints.

Mitigation: Install only when that data sharing is acceptable, and avoid submitting phone, SMS, or payment details unless registration or recharge is intended.

Risk: Environment URL overrides can redirect requests away from the default LinkFox services.

Mitigation: Use URL override environment variables only for destinations you control and trust.

Risk: Saved response files may contain sensitive business analytics, creator identifiers, or billing-related outputs.

Mitigation: Treat files in local linkfox output directories as sensitive business data and avoid sharing them broadly.

Risk: Each API call consumes paid credits, and repeated searches or detail lookups can create unexpected costs.

Mitigation: Warn users before additional paid calls, reuse the 24-hour cache when appropriate, and avoid automatic parameter probing after failures.

## Reference(s):

- [Kalodata TikTok Video API Reference](references/api.md)
- [Authentication and Billing Onboarding](references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-kalodata-tiktok-video)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, JSON, files, guidance]

**Output Format:** [Markdown guidance with JSON API responses, shell commands, and saved JSON data files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts call LinkFox/Kalodata APIs, cache matching requests for 24 hours, and save full responses under a local linkfox session directory.]

## Skill Version(s):

1.0.2 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
