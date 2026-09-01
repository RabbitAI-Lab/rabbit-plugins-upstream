## Description:

Autonomous AI Marketing & Ads Manager for OpenAI Ads API v1. End-to-end management for ChatGPT Ads: campaigns, context hints, interactive chat_cards, CAPI, custom audiences, product feeds, and insights.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rafacpti23](https://clawhub.ai/user/rafacpti23)

### License/Terms of Use:

MIT

## Use Case:

External marketers, growth teams, and developers use this skill to plan, create, manage, and analyze ChatGPT advertising campaigns through the OpenAI Ads API. It supports campaign setup, chat_card creative drafting, audience and feed workflows, conversion tracking, and performance reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create live advertising assets, affect spend, and configure tracking or lead-data flows without enough safety guardrails.

Mitigation: Review this skill before installing in a real ads account, start with sandbox or minimal-budget campaigns, and require explicit approval before creating, publishing, pausing, scaling, tracking, uploading audiences, or wiring lead webhooks to a CRM.

Risk: Ads API credentials and configurable API hosts can expose production accounts or route requests to unintended endpoints.

Mitigation: Use restricted ads API keys, verify the API host, and avoid setting OPENAI_ADS_BASE_URL unless intentionally testing.

Risk: Audience uploads, click tokens, lead data, and conversion events may include sensitive marketing or customer data.

Mitigation: Treat hashed emails, phone numbers, click tokens, lead data, and conversion events as sensitive data subject to consent and privacy obligations.

## Reference(s):

- [OpenAI Ads API Reference](references/api_reference.md)
- [ChatGPT Ads & Chat Card Best Practices](references/chat_card_best_practices.md)
- [ClawHub Skill Page](https://clawhub.ai/rafacpti23/skills/openai-ads)
- [OpenAI Ads API Base URL](https://api.ads.openai.com/v1)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python CLI commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May perform live ads-account actions when scripts are run with an ads API key.]

## Skill Version(s):

1.0.0 (source: frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
