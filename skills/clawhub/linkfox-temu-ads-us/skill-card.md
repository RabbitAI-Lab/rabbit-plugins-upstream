## Description:

Provides LinkFox gateway scripts and references for Temu US ecommerce advertising APIs, including ad creation and modification, ROAS prediction, reports, logs, detail queries, file download, and token guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and developers use this skill to manage Temu US advertising workflows through LinkFox gateway scripts. It supports creating and modifying ads, checking eligible goods, querying ad reports/details/logs, predicting ROAS, downloading signed files, and setting up LinkFox and Temu tokens.

### Deployment Geography for Use:

United States (Temu US site)

## Known Risks and Mitigations:

Risk: The skill handles LinkFox API keys, Temu access tokens, and Temu seller advertising data.

Mitigation: Install only when LinkFox is trusted for the relevant Temu seller data, treat all API keys and access tokens as secrets, and avoid exposing tokens in prompts, logs, or shared files.

Risk: Generic proxy and file-download scripts can forward broad Temu requests or retrieve signed resources.

Mitigation: Prefer the task-specific advertising scripts when possible, review the request body and Temu API type before execution, and use generic proxy or file-download scripts only when necessary.

Risk: The skill can make live advertising changes such as creating ads, changing status, budgets, or ROAS settings.

Mitigation: Require explicit user approval before campaign creation, modification, budget changes, ROAS changes, payment-order creation, or other operations that could affect spend.

Risk: Full responses and local Temu access tokens may be retained on disk.

Mitigation: Review and clean local files under the linkfox response directory and ~/.linkfox, and use secure file permissions or an alternate token store path where appropriate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-ads-us)
- [API reference](references/api.md)
- [Temu access token guide](references/access-token.md)
- [Partner US Ads catalog](references/partner-us-catalog.md)
- [Temu Partner US Ads documentation](https://partner-us.temu.com/documentation?menu_code=1e72b5cceef545ec8f9652b9e56dd054&sub_menu_code=7bc9231776304158a895e41a816b7805)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance, shell command examples, JSON API responses, and local JSON response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts save full gateway responses under a local linkfox session data directory; small responses print JSON directly and large responses print summaries unless --inline is used.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
