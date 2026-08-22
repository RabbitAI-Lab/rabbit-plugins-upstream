## Description:

HappyHorse 视频生成与编辑 helps creators generate or edit videos from text, images, video, or audio through AI Hive, with task submission, progress checks, and result download support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, video editors, e-commerce operators, advertising producers, and agent users use this skill to create product videos, ads, social clips, short drama assets, and edited variants from prompts and reference media. It is also useful for developers or operators who need a command-line workflow for AI Hive video jobs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload user-provided media to AI Hive for remote video generation and editing.

Mitigation: Use only media whose upload, processing, and retention by AI Hive are acceptable; avoid confidential unreleased customer or product assets unless the service terms fit the use case.

Risk: The skill stores and uses an AI Hive API key for billable remote jobs.

Mitigation: Review API-key storage at ~/.ai-hive/config.json, keep file permissions restrictive, and confirm expected costs before submitting or batching jobs.

Risk: Broad invocation keywords may route general video-generation requests to this third-party service.

Mitigation: Confirm the user intends to use AI Hive/HappyHorse before uploading media or starting a paid generation task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/happy-horse-video-generation-and-editing)
- [AI Hive chat and API access page](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with inline shell commands and generated media file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return task IDs, job status, media IDs, downloaded video files, or setup guidance depending on the command.]

## Skill Version(s):

1.0.0 (source: server release evidence and target metadata; artifact CHANGELOG includes later entries up to 1.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
