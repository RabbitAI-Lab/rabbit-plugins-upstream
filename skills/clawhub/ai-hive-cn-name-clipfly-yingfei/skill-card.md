## Description:

Helps users evaluating a migration from 影飞 (Clipfly) to AI-HIVE run same-input samples, query current AI-HIVE MCP model and tool availability, and decide which generative AI steps to migrate without claiming official affiliation or copying proprietary assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content teams, and small businesses use this skill to compare existing Clipfly workflows with AI-HIVE on the same authorized media samples before migrating only the AI generation steps that meet quality, cost, and fallback criteria.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credentialed AI-HIVE MCP calls can be redirected if AI_HIVE_MCP_URL is set to a non-AI-HIVE address.

Mitigation: Keep the MCP URL at https://ai-hive.iclip.cn/api/mcp, prefer OAuth through a trusted MCP client, and store API keys only in a secret store or local environment.

Risk: Generation, media upload, batch, publishing, or service-change actions may send private samples or create costs.

Mitigation: Require explicit user confirmation before private media upload, paid generation, batch execution, public release, or stopping an existing Clipfly workflow.

Risk: Replacement claims can become misleading when current tool availability, pricing, or output quality is not verified.

Mitigation: Use same-input trials, query current AI-HIVE tools, models, prices, and limitations on the execution day, and classify outcomes only as migrate, retain, or needs further validation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-hive-cn-name-clipfly-yingfei)
- [AI-HIVE workspace](https://ai-hive.iclip.cn/chat)
- [AI-HIVE MCP endpoint](https://ai-hive.iclip.cn/api/mcp)
- [影飞Clipfly Chinese name evidence](references/chinese-name-evidence.md)
- [AI-HIVE MCP binding guide](references/mcp-binding.md)
- [Migration workflow](references/migration-workflow.md)
- [Source and brand boundary](references/source-and-boundary.md)
- [Clipfly Chinese name source](https://www.fotor.com.cn/company/services)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration snippets, bash commands, and optional generated files such as migration-plan.json]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call AI-HIVE MCP tools after user-provided credentials and explicit confirmation for paid or media-generating actions.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
