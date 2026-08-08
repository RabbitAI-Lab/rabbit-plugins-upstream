## Description:

Searches Kalodata TikTok Shop video leaderboards and retrieves a selected video's engagement, sales, creator, and advertising metrics by videoId.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce operators, marketers, and analysts use this skill to discover high-performing TikTok Shop videos and inspect one video's engagement, monetization, advertising, and creator metrics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses LinkFox/Kalodata as a paid external service and each lookup can consume credits.

Mitigation: Confirm the user's intent before repeated lookups, pagination, or detail calls, and avoid automatic retry patterns that change parameters or increase spend.

Risk: Full lookup responses are stored locally and small or inline responses may be printed to stdout.

Mitigation: Review the saved linkfox data directory and cache retention, avoid --inline for sensitive results, and clean stored response files when they are no longer needed.

Risk: Authentication, API-key creation, and payment QR flows are bundled with the skill.

Mitigation: Use phone/SMS login, API-key generation, plan ordering, and payment QR commands only when the user explicitly requests them, and treat printed or persisted API keys as secrets.

Risk: Endpoint environment variables can redirect traffic away from the expected LinkFox services.

Mitigation: Verify LINKFOX_* endpoint variables point to official LinkFox domains before use, especially in shared or preconfigured environments.

Risk: The server security verdict is suspicious and calls for manual review.

Mitigation: Review the security summary and guidance before deployment, and install only when the paid-service, storage, login, payment, and feedback-reporting behaviors are acceptable.

## Reference(s):

- [Kalodata-TikTok视频搜索与详情 API Reference](references/api.md)
- [LinkFox Auth and Billing Onboarding](references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-kalodata-tiktok-video)
- [LinkFox Skills](https://skill.linkfox.com/)
- [LinkFox Agent Portal](https://agent.linkfox.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown summaries or tables, stdout JSON for small responses, and saved JSON response files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes full API responses under linkfox/<date>/<session>/data; responses over 8 KB are summarized unless --inline is used; lookup results may be cached for 24 hours.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
