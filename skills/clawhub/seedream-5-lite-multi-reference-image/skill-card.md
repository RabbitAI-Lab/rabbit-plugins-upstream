## Description:

使用 Seedream 5.0 Lite 根据来源谱系合并两张或更多授权参考图，追踪每个身份、物体、结构、材质、构图和色板来自哪里。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, designers, and developers use this skill to guide multi-reference Seedream 5.0 Lite image generation with explicit source-lineage rules for people, products, spaces, materials, composition, and palettes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected reference images, prompts, and generation parameters are sent to AI Hive.

Mitigation: Use only approved assets, avoid sensitive inputs, and confirm rights or consent before generation.

Risk: The source-lineage rules are guidance and are not guaranteed to be technically enforced by the helper script.

Mitigation: Review the prompt, input files, lineage table, task ID, and generated result before relying on the output.

Risk: A local AI Hive API key is required and may be stored on the user's machine.

Mitigation: Protect the key like any credential, prefer environment-based secret handling where appropriate, keep local config permissions restricted, and rotate the key if exposed.

Risk: Generated image fusion can create unauthorized or misleading people, brand, logo, artwork, or product representations.

Mitigation: Do not use unlicensed or unauthorized references, and reject outputs that mix protected identities, logos, text, product facts, or factual claims across sources.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/seedream-5-lite-multi-reference-image)
- [AI Hive API endpoint referenced by the skill](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup page referenced by the skill](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown with inline bash code blocks and downloaded image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires at least two user-selected reference images for generation; generated assets are downloaded by the helper script unless download is disabled.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
