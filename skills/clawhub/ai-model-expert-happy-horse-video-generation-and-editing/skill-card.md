## Description:

Helps creators and production teams use AI-HIVE to generate or edit HappyHorse videos from text and optional image, video, or audio references, then track tasks and download results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, e-commerce teams, video editors, and agents use this skill to prepare prompts and media, submit HappyHorse video generation or editing jobs through AI-HIVE, monitor task status, and retrieve finished media.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys may be exposed if pasted into chats, screenshots, or repositories.

Mitigation: Keep credentials in the AI_HIVE_API_KEY environment variable or a local config file with restricted permissions, and do not include real keys in shared prompts or source files.

Risk: Private or rights-sensitive media may be uploaded to AI-HIVE for generation or editing.

Mitigation: Use the skill only with media the user is authorized to process, and confirm consent and usage rights before upload.

Risk: Generation jobs can consume paid credits, especially for batch or long-running media tasks.

Mitigation: Confirm cost-sensitive tasks before submission, review the current pricing snapshot, and reuse saved task IDs for follow-up polling instead of resubmitting timed-out jobs.

## Reference(s):

- [AI-HIVE homepage](https://ai-hive.iclip.cn/chat)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-model-expert-happy-horse-video-generation-and-editing)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls, Files]

**Output Format:** [Markdown guidance with shell command examples; runtime commands return JSON task status and downloaded media files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can upload user-provided media, submit paid AI-HIVE generation tasks, poll task status, and download generated video outputs.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
