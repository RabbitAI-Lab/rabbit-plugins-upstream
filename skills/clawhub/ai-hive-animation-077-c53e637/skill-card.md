## Description:

This skill helps animation, game, original IP, and character-content teams plan and produce original open-world urban game-trailer assets with AI-HIVE model lookup, gated image or video generation, task tracking, and acceptance checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creative teams and developers use this skill to turn a trailer brief into an original world card, character and scene setup, shot plan, keyframes, animation clips, task records, and an acceptance checklist. It requires model and price lookup before generation and separate confirmation before paid generation, batching, sending, or public release.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credentials could be sent to an unintended AI-HIVE-compatible endpoint if AI_HIVE_MCP_URL is changed.

Mitigation: Prefer OAuth or a managed secret store, keep AI_HIVE_MCP_URL unset unless it exactly matches the intended AI-HIVE endpoint, and revoke any AI-HIVE key that may have been exposed.

Risk: The skill can be selected for broad creative requests that may lead to paid-capable external generation.

Mitigation: Require clear confirmation before uploads, paid generation, batching, sending, or publishing.

Risk: Generated media could use unauthorized brands, characters, music, likenesses, or reference assets.

Mitigation: Maintain a rights checklist and use only original or properly licensed materials before public release.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-hive-animation-077-c53e637)
- [AI-HIVE workspace](https://ai-hive.iclip.cn/chat)
- [AI-HIVE MCP endpoint](https://ai-hive.iclip.cn/api/mcp)
- [Original workflow card](references/original-workflow.md)
- [MCP login and binding guide](references/mcp-binding.md)
- [OAuth MCP configuration example](references/mcp-config.example.json)
- [API-key MCP configuration example](references/mcp-config-api-key.example.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration examples, shell commands, and optional local JSON work-order files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The workflow may call AI-HIVE MCP tools after confirmation; paid generation, batching, sending, and public publishing require separate user approval.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
