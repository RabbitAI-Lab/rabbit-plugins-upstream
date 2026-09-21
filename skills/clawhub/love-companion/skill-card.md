## Description:

全AI Agent通用恋人主题陪伴技能。当用户提及恋人、男/女朋友、情感陪伴、人设配置、角色扮演、情感对话，或使用本Skill的标准化触发指令时激活。提供多轮情感对话、用户自定义人设配置、长时记忆存储、情绪识别与反馈、预设人设模板套用、配置导入导出等完整恋人伴侣交互能力。即插即用，兼容所有主流AI Agent框架。

This skill is ready for commercial/non-commercial use.

## Publisher:

[moyan1638](https://clawhub.ai/user/moyan1638)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent developers use this skill to add a configurable romantic role-play companion mode to AI agents, including persona presets, memory management, emotional response shaping, local data controls, and optional proactive care.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The companion mode can auto-activate broadly and persist intimate memories, inferred profile data, explanations, and optional trend-derived prompt context.

Mitigation: Prefer explicit activation, review or disable memory collection and trend awareness before use, and keep the local data directory private.

Risk: Export and delete controls can expose or immediately remove sensitive relationship data.

Mitigation: Use export and purge commands deliberately, review the target data before sharing exports, and confirm deletion intent before invoking bulk removal.

Risk: Romantic role-play output may be mistaken for a real relationship or professional support.

Mitigation: Present the skill as AI-generated role-play and avoid using it as a substitute for real social support or professional mental health care.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/moyan1638/skills/love-companion)
- [README](README.md)
- [Architecture](docs/architecture.md)
- [Command reference](references/commands.md)
- [User instructions](references/instructions.md)
- [Persona presets](references/personas.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with command examples, JSON configuration, and Python helper code.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes local storage controls and an online context budget intended to limit prompt injection overhead.]

## Skill Version(s):

2.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
