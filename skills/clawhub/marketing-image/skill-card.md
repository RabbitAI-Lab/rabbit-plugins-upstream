## Description:

使用 Nano Banana 2 生成 Campaign 母版及发布会、活动、线索收集、节日促销和多渠道社媒变体的营销图片底稿。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams, designers, and agents use this skill to create approved marketing image bases and channel variants while preserving campaign identity, brand assets, safe text areas, and reviewable source relationships.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected reference images and prompts are sent to AI Hive during generation.

Mitigation: Use only approved, licensed, and non-sensitive marketing assets and prompts.

Risk: The helper stores or reads an AI Hive API key locally.

Mitigation: Install only when local key storage is acceptable and keep the configuration file access-restricted.

Risk: Generated results are saved under ~/Downloads/AiHive by default.

Mitigation: Set --output-dir when outputs should be written to a controlled project or review location.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/marketing-image)
- [AI Hive API](https://ai-hive.iclip.cn/api)
- [AI Hive API key help](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash command examples and generated image files from the helper script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses selected reference images and prompts, fixed AI Hive API routing, local API-key configuration, and optional output directory selection.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
