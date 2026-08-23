## Description:

Analyzes Amazon ASIN traffic-source composition and exposure distribution across organic search, sponsored ads, brand ads, video ads, recommendations, and period-over-period keyword changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, ecommerce analysts, and agent users use this skill to query LinkFox SIF data for ASIN traffic-source breakdowns, competitor comparisons, ad-channel exposure, and current-versus-previous-period keyword changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a LinkFox API key and onboarding flows can print or help generate credentials.

Mitigation: Treat API keys as secrets, avoid sharing terminal output containing keys, and rotate the key if it is exposed.

Risk: The skill can guide users through paid credit-package ordering when balance is insufficient.

Mitigation: Run billing and payment commands only after explicit user intent, and confirm plan and payment method before creating an order.

Risk: The skill stores full API response data locally, which may include product, query, session, or account-related context.

Mitigation: Use the saved files only in trusted workspaces and delete local LinkFox output directories when the data is no longer needed.

Risk: Onboarding can collect a phone number and SMS verification code for LinkFox account setup.

Mitigation: Use the phone/SMS path only when the user chooses it, and avoid retaining phone numbers or verification codes outside the immediate setup flow.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-sif-asin-summary)
- [LinkFox Publisher Profile](https://clawhub.ai/user/linkfox-ai)
- [SIF-ASIN流量来源 API 参考](references/api.md)
- [解决认证和积分问题](references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with tables, JSON summaries, saved JSON files, and shell command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are saved under a local linkfox session data directory; small responses can be printed inline and larger responses are summarized.]

## Skill Version(s):

1.0.8 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
