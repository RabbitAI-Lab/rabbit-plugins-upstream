## Description:

Turns Seedance AI video direction requests into a reviewable Chinese production workflow, storyboard prompts, runnable AI-HIVE commands, generation task records, and quality checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creative teams, directors, producers, and brand marketing teams use this skill to turn scripts, brand goals, authorized media, scene constraints, duration, and budget into Seedance-ready video production plans and AI-HIVE generation tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an AI-HIVE API key for generation tasks.

Mitigation: Use environment or local config storage for credentials, avoid logging real keys, and do not commit shared files containing secrets.

Risk: Generation can upload user-selected images, video, or audio to AI-HIVE.

Mitigation: Confirm media rights, privacy constraints, and user authorization before upload or reference-based generation.

Risk: Image or video generation can incur cost.

Mitigation: Review prompts, routing mode, model configuration, and price snapshot before submitting tasks; run small samples before batch jobs.

Risk: Local video processing depends on ffmpeg and can overwrite output paths selected by the user.

Mitigation: Verify ffmpeg availability, preserve original media, and choose explicit output paths before running local edits.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/wubin1836/skills/seedance-video-director-ai-hive)
- [AI-HIVE entry point](https://ai-hive.iclip.cn/chat)
- [AI-HIVE OpenAPI base endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and generated JSON or media task records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local blueprint JSON, AI-HIVE task records, and downloaded media files when the user authorizes generation.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
