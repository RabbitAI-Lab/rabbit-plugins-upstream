## Description:

Manages Shopee Follow Prize campaigns for authorized stores through LinkFox gateway scripts covering add, list, detail, update, end, and delete operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, e-commerce operators, and agent developers use this skill to create, inspect, update, end, or delete Shopee Follow Prize promotions for stores that already have LinkFox Shopee authorization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, end, or delete live Shopee Follow Prize campaigns.

Mitigation: Require explicit user confirmation before each add, update, end, or delete action and verify the target shop or merchant identifier before execution.

Risk: The skill handles LinkFox API keys, login details, SMS codes, payment flows, and QR files.

Mitigation: Treat keys, phone numbers, verification codes, payment artifacts, stdout logs, and saved session files as sensitive and clean them up when they are no longer needed.

Risk: The skill saves complete business API responses locally.

Mitigation: Review saved linkfox session data for sensitive store or campaign information and avoid sharing full response files unless necessary.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-follow-prize)
- [Publisher profile](https://clawhub.ai/user/linkfox-ai)
- [Follow Prize API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)
- [Shopee add_follow_prize documentation](https://open.shopee.com/documents/v2/v2.follow_prize.add_follow_prize?module=113&type=1)
- [Shopee get_follow_prize_list documentation](https://open.shopee.com/documents/v2/v2.follow_prize.get_follow_prize_list?module=113&type=1)
- [Shopee update_follow_prize documentation](https://open.shopee.com/documents/v2/v2.follow_prize.update_follow_prize?module=113&type=1)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with shell commands and JSON API responses saved to local files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Small responses are printed in full; larger responses are summarized while the complete response is written under a linkfox session data directory.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
