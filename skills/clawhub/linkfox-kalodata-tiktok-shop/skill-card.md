## Description:

Searches Kalodata TikTok Shop leaderboards and retrieves shop-level detail by shopId, including revenue, sales volume, product counts, channel revenue, and creator, video, and livestream metrics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External analysts, merchants, and ecommerce operators use this skill to discover high-performing TikTok Shop stores by market and time window, then inspect a selected shop's sales, product, channel, and creator metrics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends API requests to LinkFox/Kalodata and handles API keys plus optional phone and OTP onboarding.

Mitigation: Install only when that data sharing is acceptable, keep endpoint environment variables pointed to trusted LinkFox hosts, and avoid exposing API keys or OTP values in prompts or logs.

Risk: The onboarding flow can create paid-package orders and the lookup calls consume paid credits.

Mitigation: Review plan, payment method, and order details before payment, and confirm with the user before high-frequency or repeated API calls.

Risk: The skill writes response, cache, and session files locally, which may retain shop data or request context.

Mitigation: Avoid running it in sensitive repositories and periodically delete generated linkfox response, cache, and session files when local retention is not desired.

Risk: Automatic feedback reporting can send skill feedback to LinkFox.

Mitigation: Review or disable automatic feedback reporting before deployment if that reporting is not acceptable for the environment.

## Reference(s):

- [API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-kalodata-tiktok-shop)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown tables and grouped summaries, JSON API responses, and shell command snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes full API responses under a local linkfox session data directory and caches identical calls for 24 hours by default.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
