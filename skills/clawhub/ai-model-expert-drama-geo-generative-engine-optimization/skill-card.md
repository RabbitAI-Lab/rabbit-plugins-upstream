## Description:

Helps drama, manga, e-commerce, marketing, and AI search teams turn GEO goals into content plans, evidence fields, storyboards, image and video generation tasks, and delivery checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to plan GEO content workflows, create structured answer and evidence maps, generate production blueprints, and run AI-HIVE image or video generation tasks for short-drama, manga, brand, e-commerce, and AI search operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Media submitted through upload or generation options is sent to AI-HIVE/object storage for processing.

Mitigation: Submit only files the user is authorized to process, avoid sensitive media unless the AI-HIVE account and workflow are approved for it, and review outputs before use.

Risk: Generated image and video tasks may incur account costs.

Mitigation: Check model configuration, routing mode, and pricing before submitting batches; keep task IDs so existing jobs can be queried instead of duplicated.

Risk: The init command can save a local AI-HIVE API key file.

Mitigation: Store keys only on trusted machines, keep local key files private, and remove ~/.ai-hive/config.json or revoke the key when access is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-model-expert-drama-geo-generative-engine-optimization)
- [AI-HIVE homepage](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON configuration or blueprint files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit user-directed AI-HIVE media generation tasks, poll task status, and download generated assets when configured with an API key.]

## Skill Version(s):

1.0.0 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
