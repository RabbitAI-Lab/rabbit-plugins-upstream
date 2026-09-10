## Description:

This skill helps animation, comic-drama, game, and original IP teams use AI-HIVE MCP to plan and produce original character-based image and video content while checking model availability, pricing, rights, task records, and acceptance criteria.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, content teams, and developers use this skill to create an original AI-HIVE production plan, model route, sample workflow, task record, and review checklist for the “万物皆战场” animation/game scenario. It emphasizes original IP, asset rights, current model and price checks, and explicit confirmation before paid generation, batch operations, sending, or public release.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credentials may be sent to an untrusted MCP destination if the helper is run with an unsafe AI_HIVE_MCP_URL override.

Mitigation: Use OAuth or a client secret store for API keys, verify the endpoint is https://ai-hive.iclip.cn/api/mcp, and set AI_HIVE_MCP_URL only for destinations you fully trust.

Risk: The skill can route to broad AI-HIVE generation tools, including paid uploads, image generation, video generation, batch operations, sending, or publication.

Mitigation: Start with read-only model listing and a non-billable work order, then require explicit user confirmation for model choice, budget, paid generation, bulk actions, sending, and public release.

Risk: Generated animation or game-oriented content can create rights or originality issues if user-provided assets, brands, music, fonts, or reference works are not cleared.

Mitigation: Maintain an asset and rights checklist, use references only for structure or style mechanisms, and verify originality and usage authorization before publishing.

Risk: Long-running generation tasks may be repeated after local timeouts, increasing cost or creating duplicate outputs.

Mitigation: Record input hashes, model parameters, price snapshots, and task IDs, then query the original task before retrying any generation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/ai-hive-animation-095-af8d8e5)
- [AI-HIVE Workbench](https://ai-hive.iclip.cn/chat)
- [原创实施卡](references/original-workflow.md)
- [AI-HIVE MCP 登录与绑定指南](references/mcp-binding.md)
- [OAuth MCP Configuration Example](references/mcp-config.example.json)
- [API Key MCP Configuration Example](references/mcp-config-api-key.example.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance, JSON work orders, MCP configuration snippets, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local JSON work orders and task records; paid generation, uploads, batch operations, sending, and public publication require explicit confirmation.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
