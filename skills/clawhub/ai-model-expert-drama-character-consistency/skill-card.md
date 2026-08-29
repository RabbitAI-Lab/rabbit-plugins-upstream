## Description:

Helps short-drama and comic-drama teams turn character, scene, story, and brand requirements into reusable visual assets and AI-HIVE image/video generation workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External short-drama writers, comic-drama studios, brands, ecommerce merchants, growth teams, and overseas release teams use this skill to plan consistent characters and scenes, generate reusable boards or keyframes, and produce follow-on image or video generation commands through AI-HIVE.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill requires storing an AI-HIVE API key locally.

Mitigation: Store the key in the documented local configuration or environment variable, keep file permissions restricted, and rotate or revoke the key if it may have been exposed.

Risk: Generation commands can upload selected reference media to AI-HIVE.

Mitigation: Review all referenced file paths and confirm rights to use any images, video, audio, likenesses, brands, or copyrighted source material before upload.

Risk: Image and video generation tasks may incur costs.

Mitigation: Check model choices, routing mode, pricing snapshots, batch size, and output settings before submitting tasks; retain task IDs to avoid unnecessary duplicate submissions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-model-expert-drama-character-consistency)
- [AI-HIVE homepage](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON blueprints, configuration snippets, and generated media task results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May upload user-selected reference media, read local AI-HIVE API key configuration, submit AI-HIVE image/video generation tasks, poll task status, and optionally download generated image or video files.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
