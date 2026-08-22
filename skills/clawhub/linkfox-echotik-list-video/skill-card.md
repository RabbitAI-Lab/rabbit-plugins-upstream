## Description:

Searches and analyzes TikTok video data across supported TikTok Shop markets, with filters for region, creator, product, category, views, duration, publish time, and ad, AI, or selling-video flags.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketers, and analysts use this skill to find and compare TikTok videos by marketplace, creator, product, category, engagement, sales attribution, and content flags. It supports video-level performance review, content benchmarking, and campaign discovery using EchoTik and LinkFox API data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill makes LinkFox API calls that consume credits and may lead users into billing flows when balance is insufficient.

Mitigation: Require explicit user confirmation before paid calls, repeated calls, payment order creation, or credit-purchase guidance.

Risk: Full analytics responses may include commercially sensitive TikTok performance and sales-attribution data saved in local linkfox cache and session folders.

Mitigation: Tell users where full responses are stored and advise review or cleanup of local linkfox folders when results are sensitive.

Risk: Authentication and onboarding flows can request phone numbers, SMS codes, and API key setup.

Mitigation: Use the documented onboarding flow only for auth or billing errors, avoid exposing secrets in output, and ask before collecting or using credentials.

Risk: The bundled security verdict is suspicious because the skill includes analytics calls, local storage behavior, automatic feedback reporting, and account/payment onboarding.

Mitigation: Review the skill and its generated local files before installation or deployment, and disable or gate feedback and payment-related actions where policy requires.

## Reference(s):

- [API Reference](references/api.md)
- [Authentication and Billing Onboarding](references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-echotik-list-video)

## Skill Output:

**Output Type(s):** [Analysis, API Calls, JSON, Markdown, Files, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown summaries and tables with saved JSON response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are saved under a local linkfox session directory; small responses can be printed inline, while larger responses are summarized with key fields and samples.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
