## Description:

Guides agents through an AI-HIVE workflow for planning, sampling, generating, tracking, and reviewing original wuxia and folk-fantasy action short films with explicit confirmation before paid generation, batching, sending, or public release.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, directors, cinematographers, advertising teams, brand visual teams, and content creators use this skill to turn a wuxia and folk-fantasy action short-film brief into an original AI-HIVE production plan, rights checklist, model-routing plan, keyframes, video generation tasks, task records, and acceptance review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The included helper can send stored AI-HIVE credentials to an arbitrary endpoint selected through AI_HIVE_MCP_URL.

Mitigation: Prefer OAuth through a trusted MCP client; if using AI_HIVE_API_KEY or AI_HIVE_ACCESS_TOKEN, keep AI_HIVE_MCP_URL unset or set only to https://ai-hive.iclip.cn/api/mcp, and revoke any key used with an untrusted endpoint.

Risk: Image and video generation, batching, sending, or public release can create cost, publication, or rights exposure.

Mitigation: Require separate user confirmation before paid generation, batch actions, sending, or publication; keep task IDs, price snapshots, source-material rights records, and acceptance checks.

Risk: Short-film outputs may misuse brands, likenesses, music, fonts, source footage, or protected creative material.

Mitigation: Maintain a rights checklist that separates owned, licensed, analysis-only, and prohibited material, and generate original characters, brands, and assets unless rights are documented.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-hive-cinema-024-bd33891)
- [AI-HIVE workspace](https://ai-hive.iclip.cn/chat)
- [AI-HIVE MCP endpoint](https://ai-hive.iclip.cn/api/mcp)
- [Original workflow](artifact/references/original-workflow.md)
- [MCP login and binding guide](artifact/references/mcp-binding.md)
- [OAuth MCP configuration example](artifact/references/mcp-config.example.json)
- [API-key MCP configuration example](artifact/references/mcp-config-api-key.example.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration examples, Python helper scripts, and optional local JSON work orders]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call AI-HIVE MCP tools after user confirmation; the local planning script produces a non-billable JSON work order.]

## Skill Version(s):

1.0.0 (source: evidence release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
