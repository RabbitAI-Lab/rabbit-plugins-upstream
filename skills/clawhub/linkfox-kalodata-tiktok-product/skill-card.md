## Description:

Looks up TikTok Shop product leaderboards and product details through Kalodata, including market, currency, language, date-range, price, sales, revenue, commission, launch date, and shop fields.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to browse TikTok Shop product rankings and retrieve detailed analytics for a selected product ID. It is intended for product discovery and e-commerce analysis, not keyword search or non-product TikTok entities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product queries, API tokens, phone/SMS login information, and payment-order requests may be sent to LinkFox/Kalodata during normal use or account recovery.

Mitigation: Install only when that data sharing is acceptable, use trusted LinkFox endpoint environment values, and complete account setup or payment directly on the provider site when the agent should not handle credentials or billing.

Risk: Full API responses are persisted locally in a linkfox session data directory and cache files, which may include product research data that should not be committed.

Mitigation: Run the skill outside repositories where saved response JSON could be committed, review generated linkfox data before sharing, and avoid committing local cache or response files.

Risk: Each ranking or detail request consumes credits, and valid empty responses may still be billed.

Mitigation: Confirm parameters before repeated calls, rely on the default 24-hour cache for duplicate requests, and ask before continuing when additional pages or retries would incur more cost.

## Reference(s):

- [Kalodata-TikTok商品搜索与详情 API Reference](references/api.md)
- [Authentication and Billing Onboarding](references/onboarding.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-kalodata-tiktok-product)
- [Publisher profile](https://clawhub.ai/user/linkfox-ai)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, JSON files]

**Output Format:** [Markdown guidance with shell commands and JSON API responses; scripts persist full response JSON and print either full JSON or a summary.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Ranking and detail calls consume credits, use a 24-hour local cache by default, and write response JSON under a linkfox session data directory.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
