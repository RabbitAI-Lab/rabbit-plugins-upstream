## Description:

面向新手卖家的卖家精灵选品推荐专家，帮助筛选保守条件、易操作细分市场、低门槛商品机会，并提供选品指导和卖家精灵数据支撑。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and marketplace operators use this agent to find beginner-friendly product opportunities using SellerSprite product-search data, exclusion-first filtering, optional scoring, Excel exports, and scheduled recurring searches.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release was flagged as suspicious because the bundle includes broader account, payment, upload, scheduling, and agent-modification capabilities beyond product scouting.

Mitigation: Install only when the LinkFox ecosystem is trusted, review enabled subskills before use, and limit execution to the product-search, scoring, export, and scheduling workflows needed for the task.

Risk: The skill uses an API key and may create paid-plan or order flows.

Mitigation: Use a dedicated LinkFox API key, keep credentials out of chat and logs, and require explicit user confirmation before account, payment, or order-related actions.

Risk: Subskills may store product-search state locally, create or delete remote scheduled tasks, or expose local files through public upload when invoked.

Mitigation: Confirm file paths, uploaded content, and task identifiers before running upload or scheduler actions, and review existing scheduled tasks before update or deletion.

Risk: Environment-controlled gateway URLs can redirect requests to untrusted hosts.

Mitigation: Do not set LINKFOX_TOOL_GATEWAY or related base-url environment variables to untrusted hosts; use the default LinkFox gateway unless a trusted test endpoint is required.

Risk: Agent-modification and response I/O helper scripts can affect broad files or process untrusted paths if misused.

Mitigation: Avoid broad patching modes such as patch_scoring_to_agent.py --all and do not run response_io.py against untrusted paths.

## Reference(s):

- [SellerSprite Product Search API Reference](artifact/skills/linkfox-sellersprite-product-search/references/api.md)
- [SellerSprite Product Search Parameter Catalog](artifact/skills/amazon-product-scout-agent/references/api-params-catalog.md)
- [Dynamic ASIN Scoring Example Expectations](artifact/skills/amazon-asin-dynamic-scoring/references/example_expectations.json)
- [LinkFox Task Scheduler API Reference](artifact/skills/linkfox-task-scheduler/references/api.md)
- [ClawHub Skill Release Page](https://clawhub.ai/linkfox-ai/skills/linkfox-expert-beginner-sellersprite-scout)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown conversation output with product-preview tables, Excel file paths, JSON command inputs, and shell command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Primary product-search and scoring deliverables are Excel files; conversational output is limited to summaries, previews, paths, and next-step guidance.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
