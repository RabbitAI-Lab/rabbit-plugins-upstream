## Description:

Queries Jiimore Amazon niche-market intelligence for a single niche ID, including market metrics, buyer reviews, competition, price trends, inventory, and growth indicators.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers, commerce analysts, and agents use this skill to retrieve and summarize Jiimore niche-market metrics for a known Amazon niche ID. It supports market, pricing, demand, competition, launch, review, advertising, profitability, and inventory analysis for US, Japan, and Germany marketplace data.

### Deployment Geography for Use:

Global; queried marketplace data is limited to US, JP, and DE.

## Known Risks and Mitigations:

Risk: The skill calls external LinkFox/Jiimore services and uses API-key authentication.

Mitigation: Verify the endpoint environment variables and use only API keys you intend to expose to the skill.

Risk: The onboarding flow can guide phone/SMS login, create or retrieve API keys, and create paid orders after a selected plan and payment method.

Mitigation: Prefer self-service account setup on the official LinkFox site, do not share phone codes or API keys unless intentionally running onboarding, and confirm plan and payment method before order creation.

Risk: Full API responses and payment artifacts may be saved locally in LinkFox session directories.

Mitigation: Review saved files for sensitive account, market, or payment data and manage workspace access and retention accordingly.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-jiimore-get-niche-info)
- [API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, JSON files, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API or script outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Queries one nicheId per call; full responses are saved locally, with stdout returning full JSON for small responses or a compact summary for larger responses.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
