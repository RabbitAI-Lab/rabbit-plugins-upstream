## Description:

This skill helps brand marketers, ecommerce merchants, advertising teams, stores, and content marketing teams plan and produce AI-HIVE brand logo advertising assets with model and price checks, user-confirmed generation steps, task records, and acceptance criteria.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External brand, ecommerce, advertising, retail, and content marketing users use this skill to turn a brand logo advertising brief into a rights-aware production plan, creative directions, scripts, key frames, generated image or video assets, multi-ratio variants, and acceptance checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credentials can be sent to an MCP URL selected through AI_HIVE_MCP_URL.

Mitigation: Use the default AI-HIVE MCP endpoint unless the alternate destination is fully trusted, and prefer OAuth or a scoped AI-HIVE API key.

Risk: The skill allows implicit invocation and can guide paid AI-HIVE generation steps.

Mitigation: Review the plan before installing or running the skill, then confirm model, price, uploaded materials, and each paid generation step before proceeding.

Risk: Uploaded brand, product, image, video, token, or billing details may be sensitive.

Mitigation: Keep API keys and OAuth tokens out of prompts, screenshots, logs, and repositories, and verify usage rights for materials before public use.

## Reference(s):

- [AI-HIVE workspace](https://ai-hive.iclip.cn/chat)
- [AI-HIVE MCP endpoint](https://ai-hive.iclip.cn/api/mcp)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-hive-advertising-102-178514a)
- [Original workflow reference](references/original-workflow.md)
- [MCP binding guide](references/mcp-binding.md)
- [OAuth MCP configuration example](references/mcp-config.example.json)
- [API key MCP configuration example](references/mcp-config-api-key.example.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration examples, shell commands, and local JSON work-order files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide MCP API calls to AI-HIVE tools; paid generation, batch actions, sending, and public publishing require separate confirmation.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
