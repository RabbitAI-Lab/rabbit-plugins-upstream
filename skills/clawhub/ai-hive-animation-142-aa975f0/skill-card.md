## Description:

This skill helps animation, webcomic, game, original IP, and character-content teams plan and produce AI-HIVE game-demo video assets with model and price checks, original character constraints, task tracking, and explicit confirmation before paid generation or publishing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, game teams, and character-content teams use this skill to turn a brief into an original game-demo video workflow with story planning, rights checks, model routing, sample generation, task records, and acceptance criteria. Developers can also use the included scripts and MCP configuration examples to connect an agent to AI-HIVE for read-only model checks and confirmed generation tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-HIVE credentials could be sent to an untrusted MCP endpoint if the runtime MCP URL is overridden.

Mitigation: Use OAuth or an API key only with the documented AI-HIVE endpoint, and set AI_HIVE_MCP_URL only when the target server is fully trusted.

Risk: Image or video generation can create unexpected charges.

Mitigation: Query current models and pricing first, create only a minimal sample, and require explicit confirmation before paid, batch, sending, or publishing actions.

Risk: Local timeout or retry behavior can duplicate paid generation work.

Mitigation: Record taskId values and use ai_hive_get_task to check the original task before resubmitting.

Risk: Reference works or supplied media can create rights or IP issues.

Mitigation: Maintain a rights list, use references only for structure or mechanics, and confirm permission for characters, brands, music, fonts, images, and video before public use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-hive-animation-142-aa975f0)
- [AI-HIVE workspace](https://ai-hive.iclip.cn/chat)
- [Original workflow guide](references/original-workflow.md)
- [AI-HIVE MCP binding guide](references/mcp-binding.md)
- [OAuth MCP configuration example](references/mcp-config.example.json)
- [API-key MCP configuration example](references/mcp-config-api-key.example.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance, JSON work orders, shell commands, and MCP configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires explicit user confirmation before paid generation, batch actions, sending, or public publishing.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
