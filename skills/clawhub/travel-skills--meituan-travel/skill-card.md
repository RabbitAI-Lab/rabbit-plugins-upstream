## Description:

Meituan travel Skill for finding hotels, flights, train tickets, attraction tickets, vacation options, discounts, price comparisons, and itinerary support through Meituan travel services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

Travel assistants and end users use this skill to query Meituan travel services for hotels, flights, trains, attraction tickets, vacation options, discounts, and itinerary suggestions. The skill returns booking-oriented results with key details such as prices, ratings, links, and availability-oriented travel guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill invokes an unpinned npm/npx CLI that can access MEITUAN_HT_TOKEN.

Mitigation: Review the npm package provenance before installing and prefer a pinned exact version or lockfile-based install.

Risk: MEITUAN_HT_TOKEN is a sensitive credential used to access Meituan travel services.

Mitigation: Provide the token only in a trusted runtime, avoid logging or displaying it, and rotate it if exposure is suspected.

Risk: Travel actions may affect paid services, quotas, or billing.

Mitigation: Confirm token permissions, billing scope, and user intent before using the skill for booking-oriented or payment-adjacent workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/meituan-travel)
- [Publisher profile](https://clawhub.ai/user/travel-skills)
- [Meituan developer portal](https://developer.meituan.com)
- [Meituan token setup](https://developer.meituan.com/zh/v2/dev/token)
- [Meituan travel API endpoint](https://mcp-open-cater.meituan.com)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown travel results by default, raw JSON when requested, and Markdown setup guidance with shell command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include booking links, prices, ratings, hotel or carrier names, marketing text, images when supported, and API error messages.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
