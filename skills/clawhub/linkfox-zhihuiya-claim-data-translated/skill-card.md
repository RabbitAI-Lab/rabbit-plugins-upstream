## Description:

从智慧芽专利数据库获取翻译后的专利权利要求，支持按专利 ID 或公开号查询中文、英文或日文权利要求文本。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and patent-analysis agents use this skill to retrieve translated patent claim text for known patent IDs or publication numbers, including optional family-patent substitution when original claims are unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill contacts LinkFox/PatSnap services with an API key and patent query identifiers.

Mitigation: Use a key intended for this service, confirm identifiers and language before calling, and avoid sending sensitive patent lists unless the data-sharing path is acceptable.

Risk: Full patent-query results are saved locally in the current workspace.

Mitigation: Run the skill from an appropriate workspace and review or remove saved LinkFox result and cache files when they contain sensitive information.

Risk: Authentication and billing recovery can involve account login, OTP handling, API-key generation, and payment-order creation.

Mitigation: Only enter OTP codes or create payment orders when intentionally managing a LinkFox account, and prefer a secure secret store for API keys.

Risk: Queries consume LinkFox credits based on returned patent-claim result count.

Mitigation: Tell the user before additional calls that credits may be consumed, especially for batch queries or retries.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-claim-data-translated)
- [API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with JSON API responses and saved JSON result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes full patent-query responses under a local linkfox session directory; large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.8 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
