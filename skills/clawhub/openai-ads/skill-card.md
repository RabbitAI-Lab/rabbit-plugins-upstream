## Description:

Autonomous AI Marketing & Ads Manager for OpenAI Ads API v1. End-to-end management for ChatGPT Ads: campaigns, context hints, interactive chat_cards, CAPI, custom audiences, product feeds, and insights.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rafacpti23](https://clawhub.ai/user/rafacpti23)

### License/Terms of Use:

MIT

## Use Case:

Marketing teams, growth operators, and agents use this skill to plan, create, preview, track, and optimize ChatGPT ad campaigns through the OpenAI Ads API v1. The skill supports campaign structure, context hints, chat_card creatives, lead capture, product feeds, conversion tracking, and performance reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create campaigns, change budgets, publish ads, pause or scale campaigns, and configure tracking with a valid ads API key.

Mitigation: Use a least-privileged ads API key and require explicit per-action approval for campaign creation, budget changes, publishing, pausing, scaling, and tracking setup.

Risk: Credential handling is sensitive because the skill relies on client-supplied OpenAI Ads credentials.

Mitigation: Keep credentials local, rotate keys regularly, avoid server-side persistence, and use a fixed trusted API origin.

Risk: Lead webhooks, CRM sync, pixels, and CAPI events can process personal or conversion data.

Mitigation: Enable those integrations only after confirming consent, data minimization, retention rules, destination security, and key-rotation procedures.

Risk: Budget values are expressed in micros, which can lead to costly mistakes if reviewed casually.

Mitigation: Review micros conversions before execution and use protective spend-limit windows for campaign and account changes.

## Reference(s):

- [OpenAI Ads API v1 endpoint reference](references/api_reference.md)
- [ChatGPT Ads and chat_card best practices](references/chat_card_best_practices.md)
- [Client-supplied credentials architecture](references/client-supplied-credentials.md)
- [ClawHub skill release page](https://clawhub.ai/rafacpti23/skills/openai-ads)
- [Publisher profile](https://clawhub.ai/user/rafacpti23)
- [Publisher homepage](https://portal.sthub.com.br)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, API calls, guidance]

**Output Format:** [Markdown guidance with Python CLI commands, JSON API responses, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses client-supplied OpenAI Ads credentials and can perform live ad account operations when invoked with valid credentials.]

## Skill Version(s):

1.1.0 (source: evidence.release.version and target metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
