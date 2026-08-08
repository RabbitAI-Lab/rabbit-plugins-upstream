## Description:

Helps agents manage Shopee Follow Prize campaigns through LinkFox's Shopee developer proxy, including creating, listing, viewing, updating, ending, and deleting campaigns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce operators and developers use this skill to manage Follow Prize promotions for authorized Shopee stores through LinkFox scripts and API guidance. It supports campaign creation, retrieval, updates, early ending, and deletion when the user provides the required shop or merchant context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, end, or delete Shopee Follow Prize campaigns.

Mitigation: Confirm campaign identifiers, request bodies, and destructive actions with the store operator before executing API calls.

Risk: The skill handles LinkFox account login, API keys, billing orders, and Shopee shop operations.

Mitigation: Install only if the user trusts LinkFox, keep API keys private, and require explicit user confirmation for account or billing setup.

Risk: Endpoint environment variables can alter which LinkFox host receives requests.

Mitigation: Pin LinkFox endpoint variables to trusted hosts before running the scripts.

Risk: Saved response files may contain sensitive shop, campaign, or account data.

Mitigation: Treat saved linkfox response files as sensitive data and avoid sharing them outside the authorized workspace.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-follow-prize)
- [Shopee Follow Prize API index](https://open.shopee.com/documents/v2/v2.follow_prize.add_follow_prize?module=113&type=1)
- [Follow Prize API reference](references/api.md)
- [Follow Prize onboarding guide](references/onboarding.md)
- [Add Follow Prize](references/apis/add-follow-prize.md)
- [Get Follow Prize List](references/apis/get-follow-prize-list.md)
- [Get Follow Prize Detail](references/apis/get-follow-prize-detail.md)
- [Update Follow Prize](references/apis/update-follow-prize.md)
- [End Follow Prize](references/apis/end-follow-prize.md)
- [Delete Follow Prize](references/apis/delete-follow-prize.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON files]

**Output Format:** [Markdown guidance with shell commands and JSON API response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts save full API responses under linkfox/<date>/<session>/data and print either full JSON or a summary depending on response size.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
