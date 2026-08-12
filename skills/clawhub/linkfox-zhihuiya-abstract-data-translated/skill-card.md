## Description:

从智慧芽（PatSnap）专利数据库获取专利标题和摘要的翻译版本，支持通过专利 ID 或公开号查询中文、英文和日文译文。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and patent-analysis practitioners use this skill to retrieve translated patent titles and abstracts from Zhihuiya (PatSnap) for one or more known patent IDs or publication numbers. It is intended for abstract and title translation workflows, not full-text patent retrieval, legal-status analysis, or keyword-based patent search.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release security summary reports account, payment, persistent storage, configurable credential-bearing network calls, and automatic feedback reporting behavior that requires manual review before installation.

Mitigation: Install only when LinkFox is trusted with patent identifiers, returned patent content, API keys, session metadata, phone/SMS onboarding data, and possible payment or order activity.

Risk: Endpoint override environment variables can redirect credential-bearing network requests.

Mitigation: Use default LinkFox endpoints unless the override endpoints are controlled and reviewed by the deploying organization.

Risk: Full API responses are saved locally and may include patent content and session metadata.

Mitigation: Review the local linkfox output directory handling policy and avoid running the skill in directories where persisted response data should not be stored.

Risk: The skill can guide API-key onboarding and billing/order flows.

Mitigation: Prefer configuring credentials through the official LinkFox site and require explicit user confirmation before payment or plan-selection actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-abstract-data-translated)
- [Zhihuiya Abstract Translation API Reference](artifact/references/api.md)
- [Authentication and Billing Onboarding Guide](artifact/references/onboarding.md)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON files, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON API responses saved to local files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes full API responses under linkfox/<date>/<session>/data, prints full JSON for small responses or a summary for larger responses, and uses a 24-hour cache unless disabled.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
