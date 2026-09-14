## Description:

Autonomous AI Marketing & Ads Manager for OpenAI Ads via Habilis MCP Gateway (https://xvix.com.br). End-to-end campaign orchestration, chat_cards synthesis, catalog feeds, and performance telemetry.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rafacpti23](https://clawhub.ai/user/rafacpti23)

### License/Terms of Use:

MIT

## Use Case:

Marketing operators, developers, and external agents use this skill to configure Habilis MCP access, create and inspect OpenAI Ads campaigns, generate chat_card creatives, and review performance telemetry.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Powerful ad-provider credentials may be sent through a third-party gateway during MCP tool calls.

Mitigation: Use least-privilege, revocable credentials and rotate them regularly.

Risk: Campaign creation or activation can spend advertising budget.

Mitigation: Set strict budget limits and require manual confirmation before creating or activating campaigns.

Risk: Conversion identifiers or telemetry may include sensitive marketing or customer-derived data.

Mitigation: Review conversion payloads before sending them and avoid unnecessary identifiers.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/rafacpti23/skills/openai-ads)
- [Habilis MCP Gateway](https://xvix.com.br/api/mcp)
- [ChatGPT Ads & Chat Card Best Practices](references/chat_card_best_practices.md)
- [Stateless Client-Supplied Credentials Architecture](references/client-supplied-credentials.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, API calls]

**Output Format:** [Markdown with inline YAML and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose MCP tool calls for account inspection, campaign creation, chat_card creation, and performance insights.]

## Skill Version(s):

1.1.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
