## Description:

Guides agents through an AI-HIVE workflow for font-motion advertising, from audience and rights checks through model lookup, creative planning, image and video generation, task tracking, and acceptance checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Brand marketers, ecommerce sellers, agencies, stores, and content marketing teams use this skill to plan and produce font-motion ad assets with AI-HIVE while preserving product facts, source rights, budget controls, task records, and acceptance criteria.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can send credentials to an MCP endpoint selected through the AI_HIVE_MCP_URL environment variable.

Mitigation: Use only the official AI-HIVE endpoint unless the destination is fully trusted, and keep API keys or OAuth tokens in a controlled secret store.

Risk: The skill can lead to paid generation, uploads, batch work, sending, or public publication.

Mitigation: Require explicit user confirmation after reviewing model choice, parameters, budget, and expected call count before any paid or externally visible action.

Risk: Broad auto-triggering could route unrelated advertising, image, video, or short-form content requests into this workflow.

Mitigation: Confirm that the user intends to create a font-motion advertising workflow before invoking AI-HIVE tools or preparing production assets.

Risk: Advertising outputs can contain unsupported claims or materials without sufficient rights.

Mitigation: Maintain a product fact card and source-rights checklist, and review final assets for factual, brand, rights, and channel compliance before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-hive-advertising-138-6a5a4a8)
- [AI-HIVE workspace](https://ai-hive.iclip.cn/chat)
- [AI-HIVE MCP binding guide](references/mcp-binding.md)
- [Original workflow implementation card](references/original-workflow.md)
- [OAuth MCP configuration example](references/mcp-config.example.json)
- [API-key MCP configuration example](references/mcp-config-api-key.example.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON work orders, shell commands, configuration snippets, and references to generated image/video task outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires explicit confirmation before paid generation, batch work, uploads, sending, or publication.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
