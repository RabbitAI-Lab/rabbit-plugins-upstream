## Description:

Helps creators and commerce teams generate Seedance 2.5 first-and-last-frame videos through AI Hive by uploading source media, submitting a video task, polling progress, and downloading the result.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, advertising and marketing teams, e-commerce operators, and short-form drama teams use this skill to turn a prompt plus first and last frame images into generated video assets through AI Hive. It is intended for product videos, ads, social media content, and storyboards where the user wants task submission, progress tracking, and result download handled by the skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security evidence marks the release suspicious because its activation text and bundled script are broader than a narrow Seedance first-and-last-frame generator.

Mitigation: Review the skill before installing and use it only when the intended workflow is AI Hive Seedance video generation rather than generic product discovery or competitor comparison.

Risk: The workflow uploads user-provided media to AI Hive.

Mitigation: Use only media that is appropriate to upload to AI Hive and check applicable content, privacy, and customer-data requirements before submission.

Risk: The workflow requires an AI Hive API key that may be stored locally or passed through the environment or command line.

Mitigation: Protect the API key, keep local configuration permissions restricted, and rotate or revoke the key if it may have been exposed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/seedance-2-5-first-last-frame-to-video)
- [AI Hive chat and API key portal](https://ai-hive.iclip.cn/chat)
- [AI Hive API base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with bash command examples, JSON configuration, task identifiers, and downloaded video files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill can upload user media to AI Hive, submit generation jobs, poll by taskId, and save generated media to a local output directory.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
