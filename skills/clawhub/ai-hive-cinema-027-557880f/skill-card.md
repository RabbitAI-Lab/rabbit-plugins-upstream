## Description:

Helps creative teams plan and execute an AI-HIVE workflow for original long-take cinematic shorts by turning abstract visual style goals into composition, color, lighting, camera movement, narrative rhythm, sample generation, task tracking, and acceptance checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External directors, cinematographers, advertising creatives, brand visual teams, and content creators use this skill to create an original AI-HIVE production plan, rights checklist, model-routing plan, sample, image or video tasks, and acceptance report for a gaze-oriented long-take film short. The workflow emphasizes user confirmation before paid generation, batch operations, sending, or public release.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access broad AI-HIVE remote tools, including uploads and paid image or video generation.

Mitigation: Use OAuth or a fixed trusted MCP configuration, query models and prices before generation, and require explicit confirmation before uploads, paid generation, batch operations, sending, or publishing.

Risk: The helper script can send API keys or bearer tokens to an endpoint controlled by AI_HIVE_MCP_URL.

Mitigation: Do not set AI_HIVE_MCP_URL in normal use; revoke and rotate any API key used with an untrusted endpoint.

Risk: Generated film assets may rely on references, people, brands, music, fonts, images, or video without sufficient rights.

Mitigation: Keep a rights checklist, use only owned or authorized source material, avoid requests to copy living creators or protected IP, and review copyright risk before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-hive-cinema-027-557880f)
- [AI-HIVE workspace](https://ai-hive.iclip.cn/chat)
- [AI-HIVE MCP endpoint](https://ai-hive.iclip.cn/api/mcp)
- [Original workflow card](artifact/references/original-workflow.md)
- [MCP login and binding guide](artifact/references/mcp-binding.md)
- [OAuth MCP configuration example](artifact/references/mcp-config.example.json)
- [API-key MCP configuration example](artifact/references/mcp-config-api-key.example.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration examples and optional local JSON work-order files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference AI-HIVE task IDs, model and price snapshots, rights notes, and acceptance criteria when the agent executes the workflow.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
