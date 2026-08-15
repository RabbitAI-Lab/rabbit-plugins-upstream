## Description:

Searches and analyzes TikTok Shop seller and store data across 16 marketplaces with filters for region, category, GMV, sales trend, listing date, seller type, and sales channel.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External cross-border ecommerce sellers, marketers, and analysts use this skill to discover, compare, and benchmark TikTok Shop stores by sales, GMV, region, category, and store attributes. It is intended for store-level market research and competitor analysis, not order, logistics, ads, product, creator, or video management.

### Deployment Geography for Use:

Global; data queries are limited to the 16 supported TikTok Shop marketplaces listed in the skill.

## Known Risks and Mitigations:

Risk: The skill requires a LinkFox API key and may guide account setup when credentials are missing.

Mitigation: Prefer self-service account setup, avoid sharing unnecessary phone or SMS-code data through the agent, and rotate or revoke the API key if exposure is suspected.

Risk: Queries make paid external API calls and the skill documents a 5-credit cost per use.

Mitigation: Confirm cost expectations before repeated calls, pagination, or changed filters; avoid automatic retries or broad parameter sweeps without user approval.

Risk: Full API responses are saved under a local linkfox directory and may include detailed seller research outputs.

Mitigation: Review saved files after use, delete data that is no longer needed, and avoid running the skill in workspaces where persistent response files are inappropriate.

Risk: Custom LinkFox endpoint environment variables can redirect requests away from default services.

Mitigation: Set custom endpoint variables only to trusted endpoints that the user controls or has explicitly approved.

Risk: Embedded onboarding and billing helpers can create orders or display payment flows.

Mitigation: Use self-service billing where possible and verify plan, payment method, and order details before invoking billing commands.

## Reference(s):

- [EchoTik-TikTok店铺列表 API 参考](artifact/references/api.md)
- [解决认证和积分问题](artifact/references/onboarding.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-echotik-list-seller)
- [LinkFox Skills guide](https://skill.linkfox.com/linkfoxskills/guide.htm)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown tables or JSON response summaries, with full JSON responses saved to local files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a 24-hour local cache for repeated parameter sets; large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
