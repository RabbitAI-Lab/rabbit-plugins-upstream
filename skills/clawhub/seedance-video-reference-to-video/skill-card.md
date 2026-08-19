## Description:

Helps creators generate Seedance reference-to-video outputs by using AI Hive to upload selected media, submit video generation tasks, track progress, and download completed video files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, video editors, post-production teams, and advertising or e-commerce teams use this skill to create Seedance reference-video-based videos from selected prompts and media assets. It is suited for product videos, ads, TVC concepts, social commerce, short drama, comic drama, and social media content workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary reports a broad activation scope for a workflow that uploads user media.

Mitigation: Invoke the skill only when the user has explicitly selected the media files and the Seedance reference-video generation task.

Risk: The security guidance warns that media is uploaded to AI Hive or object storage.

Mitigation: Use only files the user is comfortable uploading to AI Hive or related object storage, and avoid sensitive or confidential media unless approved.

Risk: The security summary notes that the skill stores an API key.

Mitigation: Prefer environment variables or ensure any local AI Hive configuration file remains permission-restricted and is not shared.

Risk: The security guidance calls out cost monitoring before batch jobs.

Mitigation: Check pricing and task volume before batch generation, and avoid repeated submissions when a task ID can be queried.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/seedance-video-reference-to-video)
- [AI Hive chat and API key setup](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, API calls, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands; runtime output includes JSON task responses and downloaded video files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an AI Hive API key and user-selected local media; generated media is downloaded to the configured output directory.]

## Skill Version(s):

1.0.0 (source: server release evidence, released 2026-08-16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
