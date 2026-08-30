## Description:

Helps cross-border sellers, TikTok Shop teams, and content operators decompose authorized TikTok Shop commerce videos into human-reviewable hooks, pacing, UGC scripts, subtitle plans, regional adaptation guidance, prompts, commands, and acceptance checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External commerce and marketing teams use this skill to turn authorized reference media, product facts, target markets, and compliance constraints into differentiated TikTok Shop production plans. It supports video-structure analysis, script and prompt drafting, AI-HIVE generation commands, local video-editing commands, and review checklists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can use API keys, upload local media files, and call AI-HIVE generation services that may incur cost.

Mitigation: Before running commands, confirm which files will be uploaded, which route and parameters will be used, where outputs will be written, and whether any generation cost is acceptable.

Risk: Generated marketing content can contain unsupported product claims, copied reference-video elements, or inappropriate language for the target workflow.

Mitigation: Use the skill's review checkpoints to confirm authorization, factual product claims, visible differentiation from references, and whether Chinese output or regional adaptation is appropriate.

Risk: API keys could be exposed through files, logs, screenshots, or version control if handled carelessly.

Mitigation: Use environment variables or the local AI-HIVE config flow, keep example keys as placeholders, and review outputs before sharing or committing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/tiktok-shop-viral-video-decomposer-ai-hive)
- [AI-HIVE chat](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task records such as routing mode, model, pricing snapshot, taskId, status, and local output paths when generation is executed.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
