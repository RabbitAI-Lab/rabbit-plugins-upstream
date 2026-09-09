## Description:

Helps brand, ecommerce, agency, retail, and content marketing teams plan and produce original toy-inspired IP advertising assets through AI-HIVE model routing, confirmed paid generation, task tracking, and acceptance checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External brand marketing, ecommerce, advertising, retail, and content teams use this skill to turn product facts, audience details, rights constraints, and budget limits into an AI-HIVE advertising workflow. It produces plans, sample directions, task records, and acceptance checks before any paid generation, batch action, sending, or public publishing is confirmed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials can be sent to an environment-selected AI-HIVE MCP URL.

Mitigation: Prefer OAuth or a client-managed secret, set AI_HIVE_MCP_URL only when the endpoint is intentionally chosen, and keep API keys out of prompts, logs, screenshots, and repositories.

Risk: AI-HIVE upload, generation, batch, send, and publishing actions may have cost, privacy, or publication impact.

Mitigation: Confirm the model, price snapshot, inputs, generation count, batch actions, sending, and public publishing before execution; use read-only model listing and task lookup for checks where possible.

Risk: Advertising outputs may rely on brand, product, music, image, video, font, or likeness material that the user is not authorized to use.

Mitigation: Maintain a rights checklist, distinguish owned and licensed assets from analysis-only references, and avoid unlicensed logos, characters, music, likenesses, and protected IP.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-hive-advertising-086-b4c7674)
- [AI-HIVE workbench](https://ai-hive.iclip.cn/chat)
- [Original workflow reference](artifact/references/original-workflow.md)
- [AI-HIVE MCP login and binding guide](artifact/references/mcp-binding.md)
- [OAuth MCP configuration example](artifact/references/mcp-config.example.json)
- [API-key MCP configuration example](artifact/references/mcp-config-api-key.example.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON work orders, shell commands, and MCP configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The local planning script can write a JSON work order; AI-HIVE generation, upload, batch, send, and publish actions require explicit user confirmation.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
