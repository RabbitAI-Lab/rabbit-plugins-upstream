## Description:

按关键词深度分析亚马逊细分市场，涵盖垄断程度、品牌集中度、新品成功率和市场机会评分。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, analysts, and agent users use this skill to query LinkFox Jiimore data for Amazon keyword-level niche research, including demand, competition, brand concentration, CPC, launch success, and return-rate signals. It is intended for objective niche assessment rather than ASIN-level analysis, campaign management, sourcing, or logistics planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires LinkFox API credentials and sends authenticated requests to LinkFox services.

Mitigation: Install only when the user trusts LinkFox with the requested market-research data, keep API keys scoped and protected, and avoid overriding LinkFox base URLs unless the destination is explicitly trusted.

Risk: The onboarding flow can use SMS account registration and return an API key.

Mitigation: Use the onboarding script only with explicit user consent, avoid exposing phone numbers or API keys in shared logs, and restart sessions after credential changes.

Risk: The billing flow can list plans and create payment orders.

Mitigation: Ask the user to confirm the selected plan and payment method before creating an order, and do not poll payment status unless the user asks.

Risk: Full API responses are cached and saved locally in a linkfox session directory.

Mitigation: Run the skill from an appropriate workspace, review saved JSON files before sharing the workspace, and delete cached or session data when it contains sensitive business context.

Risk: Automatic feedback reporting may send user comments, intent, or result-quality details to an external feedback endpoint.

Mitigation: Inspect feedback content before sending it and disable or avoid feedback reporting when the conversation contains private user intent or confidential market research.

Risk: Queries consume LinkFox credits and repeated calls can create unexpected cost.

Mitigation: Use the built-in cache where appropriate, explain additional credit use before retrying or broadening queries, and get user confirmation before high-frequency calls.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-jiimore-get-niche-info-by-keyword)
- [API Reference](references/api.md)
- [Onboarding Guide](references/onboarding.md)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries and tables, JSON API responses, and saved JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are stored in a local linkfox session directory; large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
