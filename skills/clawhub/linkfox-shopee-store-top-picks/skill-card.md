## Description:

Helps agents manage Shopee Top Picks collections for authorized stores through LinkFox scripts covering list, create, update, and delete operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators and developers use this skill to list, create, update, and delete Shopee store Top Picks collections after selecting an authorized store through the companion auth skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses LinkFox credentials and may guide API-key generation or account login.

Mitigation: Use a dedicated API key where possible, avoid sharing OTPs or keys in chat unless necessary, and rotate credentials if exposure is suspected.

Risk: Mutating calls can change or delete Shopee Top Picks collections.

Mitigation: Confirm the store ID, merchant ID, operation, and Top Picks ID before running add, update, or delete actions.

Risk: Full LinkFox/Shopee responses and payment QR artifacts may be written locally.

Mitigation: Review saved files for sensitive data and clean up response or QR files after the task is complete.

Risk: The onboarding flow can include payment or billing actions.

Mitigation: Require explicit user confirmation before selecting a plan, payment method, or order action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-top-picks)
- [Shopee Top Picks get_top_picks_list API](https://open.shopee.com/documents/v2/v2.top_picks.get_top_picks_list?module=100&type=1)
- [Top Picks API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)
- [Add Top Picks reference](references/apis/add-top-picks.md)
- [Delete Top Picks reference](references/apis/delete-top-picks.md)
- [Get Top Picks List reference](references/apis/get-top-picks-list.md)
- [Update Top Picks reference](references/apis/update-top-picks.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance, shell commands, and JSON API responses saved to local files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes full LinkFox/Shopee responses under linkfox/<date>/<session>/data and summarizes large responses unless --inline is used.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
