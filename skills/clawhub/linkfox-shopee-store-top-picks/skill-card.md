## Description:

Helps agents manage Shopee Top Picks collections through LinkFox's developerProxy wrapper for list, add, update, and delete operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Shopee store operators and their agents use this skill to inspect and manage authorized store Top Picks collections, including listing, creating, updating, and deleting collections through LinkFox.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires trust in LinkFox for Shopee store operations, API key use, phone/SMS login, and billing workflows.

Mitigation: Install only for trusted LinkFox accounts and keep LinkFox API keys scoped, rotated, and stored in environment variables rather than shared text.

Risk: Endpoint environment variables can redirect requests away from the default LinkFox hosts.

Mitigation: Before use, verify LinkFox endpoint environment variables point to official LinkFox hosts.

Risk: Add, update, delete, and payment-order commands can change store state or initiate billing flows.

Mitigation: Require explicit user approval before running mutating Top Picks commands or payment-order commands.

Risk: Full API responses are saved locally and may include store or account data.

Mitigation: Review the local linkfox output directory, restrict workspace access, and remove saved response files when they are no longer needed.

## Reference(s):

- [Shopee Top Picks API overview](references/api.md)
- [Add Top Picks API](references/apis/add-top-picks.md)
- [Delete Top Picks API](references/apis/delete-top-picks.md)
- [Get Top Picks List API](references/apis/get-top-picks-list.md)
- [Update Top Picks API](references/apis/update-top-picks.md)
- [Authentication and billing onboarding](references/onboarding.md)
- [Shopee Open Platform Top Picks documentation](https://open.shopee.com/documents/v2/v2.top_picks.get_top_picks_list?module=100&type=1)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-top-picks)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON, Files]

**Output Format:** [Markdown guidance with Python command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are saved under a local linkfox session data directory; small responses print JSON, while larger responses print a summary unless --inline is used.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
