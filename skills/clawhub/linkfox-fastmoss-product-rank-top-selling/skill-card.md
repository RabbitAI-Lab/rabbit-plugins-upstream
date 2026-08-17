## Description:

FastMoss-TikTok热销榜 helps agents query FastMoss data for TikTok Shop top-selling product rankings by market, category, and day, week, or month time windows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce operators and agents use this skill to retrieve TikTok Shop bestseller rankings across supported markets for product scouting, trend review, and category-level ranking analysis.

### Deployment Geography for Use:

Global; ranking data is limited to the supported TikTok Shop markets listed by the skill.

## Known Risks and Mitigations:

Risk: The skill sends ranking queries, API credentials, onboarding requests, feedback, and payment-order actions to LinkFox/FastMoss services.

Mitigation: Install only when use of LinkFox/FastMoss services is acceptable, prefer the official account portal for signup or billing, and keep API keys out of shared shell startup files when possible.

Risk: Full API responses and payment QR artifacts may be saved locally under linkfox output directories.

Mitigation: Review the local linkfox directories after use and delete stored responses or QR artifacts that should not be retained.

Risk: Ranking calls consume credits, and billing flows can create payment orders when credits are missing.

Mitigation: Confirm user intent before repeated lookups or billing actions and avoid automatic retries that change parameters solely to consume additional requests.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-fastmoss-product-rank-top-selling)
- [Publisher profile](https://clawhub.ai/user/linkfox-ai)
- [FastMoss-TikTok热销榜单 API 参考](references/api.md)
- [解决认证和积分问题](references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON summaries, with optional shell commands and local JSON result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The ranking script writes full API responses to a local linkfox directory, uses a 24-hour local cache for repeated parameter sets, and summarizes large responses unless inline output is requested.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
